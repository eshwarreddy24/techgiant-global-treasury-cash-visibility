"""Recalculate and validate the synthetic TechGiant treasury case study.

The validator derives reconciliation, cash-position, forecast, and Tableau
checks from the source CSVs. It does not use a hidden golden output.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TABLEAU = ROOT / "tableau"
TOLERANCE = Decimal("0.01")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def decimal(row: dict[str, str], field: str) -> Decimal:
    try:
        return Decimal(row[field].strip())
    except (KeyError, InvalidOperation) as exc:
        raise ValueError(f"{field} must be numeric: {row}") from exc


def require_columns(rows: list[dict[str, str]], name: str, required: set[str]) -> None:
    actual = set(rows[0]) if rows else set()
    missing = required - actual
    if missing:
        raise ValueError(f"{name} is missing columns: {', '.join(sorted(missing))}")


def assert_unique(rows: list[dict[str, str]], field: str, name: str) -> None:
    values = [row[field] for row in rows]
    duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
    if duplicates:
        raise ValueError(f"{name}.{field} has duplicate values: {duplicates}")


def key(row: dict[str, str], reference: str) -> tuple[str, str, str]:
    return row[reference], row["Account_ID"], row["Currency"]


def compare_rows(
    actual: list[dict[str, str]],
    expected: list[dict[str, str]],
    fields: list[str],
    name: str,
) -> None:
    actual_by_key = {tuple(row[field] for field in fields): row for row in actual}
    expected_by_key = {tuple(row[field] for field in fields): row for row in expected}
    if set(actual_by_key) != set(expected_by_key):
        raise ValueError(f"{name} keys do not match source-derived keys")
    for row_key, expected_row in expected_by_key.items():
        actual_row = actual_by_key[row_key]
        for field in expected_row:
            if field not in actual_row:
                raise ValueError(f"{name} is missing field {field}")
            numeric_fields = {
                "Bank_Cash_Impact",
                "GL_Cash_Impact",
                "Variance_Bank_Less_GL",
                "Opening_Balance_Local",
                "Net_Bank_Movement_Local",
                "Closing_Balance_Local",
                "Minimum_Reserve_Local",
                "Liquidity_Headroom_Local",
                "Closing_Balance_USD",
                "Liquidity_Headroom_USD",
                "Minimum_Reserve_USD",
                "Available_Cash_USD",
            }
            if field in numeric_fields:
                if abs(Decimal(actual_row[field]) - Decimal(expected_row[field])) > TOLERANCE:
                    raise ValueError(f"{name} value mismatch for {row_key}: {field}")
            elif actual_row[field] != expected_row[field]:
                raise ValueError(f"{name} value mismatch for {row_key}: {field}")


def main() -> int:
    required_files = [
        ROOT / "README.md",
        ROOT / "START_HERE.md",
        ROOT / "TechGiant_Global_Cash_Visibility_Project.xlsx",
        DATA / "account_master.csv",
        DATA / "bank_transactions.csv",
        DATA / "gl_transactions.csv",
        DATA / "fx_rates.csv",
        DATA / "cash_position.csv",
        DATA / "four_week_forecast.csv",
        DATA / "expected_bank_reconciliation.csv",
        DATA / "expected_gl_only_review.csv",
        TABLEAU / "tableau_cash_position.csv",
        TABLEAU / "tableau_daily_cash_flows.csv",
        TABLEAU / "tableau_exception_summary.csv",
        TABLEAU / "tableau_four_week_forecast.csv",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    if missing:
        raise ValueError("Missing required files:\n" + "\n".join(f"  - {item}" for item in missing))

    accounts = read_csv(DATA / "account_master.csv")
    bank = read_csv(DATA / "bank_transactions.csv")
    gl = read_csv(DATA / "gl_transactions.csv")
    fx = read_csv(DATA / "fx_rates.csv")
    cash = read_csv(DATA / "cash_position.csv")
    forecast = read_csv(DATA / "four_week_forecast.csv")
    expected_recon = read_csv(DATA / "expected_bank_reconciliation.csv")
    expected_gl_only = read_csv(DATA / "expected_gl_only_review.csv")
    tableau_cash = read_csv(TABLEAU / "tableau_cash_position.csv")
    tableau_flows = read_csv(TABLEAU / "tableau_daily_cash_flows.csv")
    tableau_summary = read_csv(TABLEAU / "tableau_exception_summary.csv")
    tableau_forecast = read_csv(TABLEAU / "tableau_four_week_forecast.csv")

    require_columns(accounts, "account_master", {"Account_ID", "Legal_Entity", "Currency", "Opening_Balance_Local", "Minimum_Reserve_Local"})
    require_columns(bank, "bank_transactions", {"Bank_Ref", "Value_Date", "Account_ID", "Currency", "Cash_Impact_Local", "FX_to_USD", "Cash_Impact_USD"})
    require_columns(gl, "gl_transactions", {"GL_Ref", "Posting_Date", "Account_ID", "Currency", "GL_Document", "GL_Cash_Impact_Local"})
    require_columns(fx, "fx_rates", {"Currency", "USD_per_1_Unit"})
    require_columns(cash, "cash_position", {"Account_ID", "Closing_Balance_Local", "Closing_Balance_USD", "Minimum_Reserve_USD", "Liquidity_Headroom_USD"})
    require_columns(forecast, "four_week_forecast", {"Account_ID", "Week_End", "Opening_Balance_Local", "Net_Flow_Local", "Projected_Closing_Local", "Projected_Closing_USD", "Liquidity_Headroom_USD"})

    assert_unique(accounts, "Account_ID", "account_master")
    assert_unique(bank, "Bank_Ref", "bank_transactions")
    assert_unique(gl, "GL_Document", "gl_transactions")
    assert_unique(fx, "Currency", "fx_rates")

    account_by_id = {row["Account_ID"]: row for row in accounts}
    fx_by_currency = {row["Currency"]: decimal(row, "USD_per_1_Unit") for row in fx}
    valid_currencies = set(fx_by_currency)
    if {row["Currency"] for row in accounts} != valid_currencies:
        raise ValueError("Account currencies and FX currencies do not match")
    for row in bank + gl:
        if row["Account_ID"] not in account_by_id:
            raise ValueError(f"Unknown account reference: {row['Account_ID']}")
        if row["Currency"] not in valid_currencies:
            raise ValueError(f"Unknown currency reference: {row['Currency']}")

    gl_groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in gl:
        gl_groups[key(row, "GL_Ref")].append(row)
    bank_keys = {key(row, "Bank_Ref") for row in bank}
    derived_recon = []
    for row in bank:
        matches = gl_groups.get(key(row, "Bank_Ref"), [])
        gl_total = sum((decimal(item, "GL_Cash_Impact_Local") for item in matches), Decimal("0"))
        variance = decimal(row, "Cash_Impact_Local") - gl_total
        if len(matches) > 1:
            status = "Duplicate in GL"
        elif not matches:
            status = "Missing in GL"
        elif abs(variance) > TOLERANCE:
            status = "Amount mismatch"
        else:
            status = "Matched"
        derived_recon.append({
            "Bank_Ref": row["Bank_Ref"],
            "Account_ID": row["Account_ID"],
            "Currency": row["Currency"],
            "Value_Date": row["Value_Date"],
            "Bank_Cash_Impact": str(decimal(row, "Cash_Impact_Local")),
            "GL_Cash_Impact": str(gl_total),
            "GL_Match_Count": str(len(matches)),
            "Variance_Bank_Less_GL": str(variance),
            "Reconciliation_Status": status,
        })
    compare_rows(derived_recon, expected_recon, ["Bank_Ref", "Account_ID", "Currency"], "expected_bank_reconciliation")

    derived_gl_only = []
    for row in gl:
        reference_count = sum(1 for bank_row in bank if key(bank_row, "Bank_Ref") == key(row, "GL_Ref"))
        derived_gl_only.append({
            "GL_Ref": row["GL_Ref"],
            "Posting_Date": row["Posting_Date"],
            "Account_ID": row["Account_ID"],
            "Currency": row["Currency"],
            "GL_Document": row["GL_Document"],
            "GL_Cash_Impact": str(decimal(row, "GL_Cash_Impact_Local")),
            "Bank_Reference_Count": str(reference_count),
            "Review_Status": "Reference found" if reference_count else "GL-only: investigate",
        })
    compare_rows(derived_gl_only, expected_gl_only, ["GL_Ref", "GL_Document"], "expected_gl_only_review")

    status_counts = Counter(row["Reconciliation_Status"] for row in derived_recon)
    status_counts["GL-only: investigate"] = sum(
        row["Review_Status"] == "GL-only: investigate" for row in derived_gl_only
    )
    expected_status_counts = {
        "Matched": 17,
        "Missing in GL": 1,
        "Amount mismatch": 1,
        "Duplicate in GL": 1,
        "GL-only: investigate": 1,
    }
    summary_counts = {row["Status"]: int(row["Count"]) for row in tableau_summary}
    if dict(status_counts) != summary_counts or dict(status_counts) != expected_status_counts:
        raise ValueError(f"Exception summary mismatch: derived={dict(status_counts)}, Tableau={summary_counts}")

    derived_cash = []
    movements: dict[str, Decimal] = defaultdict(lambda: Decimal("0"))
    for row in bank:
        movements[row["Account_ID"]] += decimal(row, "Cash_Impact_Local")
    for row in accounts:
        closing_local = decimal(row, "Opening_Balance_Local") + movements[row["Account_ID"]]
        fx_rate = fx_by_currency[row["Currency"]]
        reserve_local = decimal(row, "Minimum_Reserve_Local")
        derived_cash.append({
            "Account_ID": row["Account_ID"],
            "Legal_Entity": row["Legal_Entity"],
            "Bank_Name": row["Bank_Name"],
            "Currency": row["Currency"],
            "Opening_Balance_Local": str(decimal(row, "Opening_Balance_Local")),
            "Net_Bank_Movement_Local": str(movements[row["Account_ID"]]),
            "Closing_Balance_Local": str(closing_local),
            "Minimum_Reserve_Local": str(reserve_local),
            "Liquidity_Headroom_Local": str(closing_local - reserve_local),
            "Closing_Balance_USD": str(closing_local * fx_rate),
            "Liquidity_Headroom_USD": str((closing_local - reserve_local) * fx_rate),
            "Minimum_Reserve_USD": str(reserve_local * fx_rate),
            "Available_Cash_USD": str((closing_local - reserve_local) * fx_rate),
            "Liquidity_Status": "Within reserve" if closing_local >= reserve_local else "Below reserve",
        })
    compare_rows(derived_cash, cash, ["Account_ID"], "cash_position")
    compare_rows(derived_cash, tableau_cash, ["Account_ID"], "tableau_cash_position")

    if len(forecast) != 20 or len(tableau_forecast) != 20 or len({row["Week_End"] for row in forecast}) != 4:
        raise ValueError("Forecast must contain 20 rows: 5 accounts across 4 weeks")
    compare_rows(forecast, tableau_forecast, ["Account_ID", "Week_End"], "tableau_four_week_forecast")
    for row in forecast:
        if decimal(row, "Net_Flow_Local") != decimal(row, "Forecast_Inflows_Local") - decimal(row, "Forecast_Outflows_Local"):
            raise ValueError(f"Forecast net flow mismatch: {row['Account_ID']} {row['Week_End']}")
        if decimal(row, "Projected_Closing_Local") != decimal(row, "Opening_Balance_Local") + decimal(row, "Net_Flow_Local"):
            raise ValueError(f"Forecast closing balance mismatch: {row['Account_ID']} {row['Week_End']}")

    if bank != tableau_flows:
        raise ValueError("Tableau daily cash-flow extract does not match bank source data")
    closing_cash = sum((Decimal(row["Closing_Balance_USD"]) for row in cash), Decimal("0"))
    headroom = sum((Decimal(row["Liquidity_Headroom_USD"]) for row in cash), Decimal("0"))
    reserve = sum((Decimal(row["Minimum_Reserve_USD"]) for row in cash), Decimal("0"))
    if round(closing_cash, 2) != Decimal("3776601.50") or round(headroom, 2) != Decimal("3150851.50"):
        raise ValueError(f"Unexpected portfolio totals: closing={closing_cash}, headroom={headroom}")
    if round(reserve, 2) != Decimal("625750.00"):
        raise ValueError(f"Unexpected minimum reserve total: {reserve}")

    suspicious = re.compile(r"(^|/)(\.env|.*secret.*|.*credential.*|.*token.*)$", re.I)
    flagged = [str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file() and suspicious.search(path.relative_to(ROOT).as_posix())]
    if flagged:
        raise ValueError(f"Possible credential files found: {flagged}")
    if (TABLEAU / "TechGiant_Global_Treasury_Dashboard.twbx").exists():
        raise ValueError("A file named .twbx exists but has not been verified as a native Tableau package")

    print("PASS: source-derived TechGiant treasury validation succeeded.")
    print(f"  Accounts: {len(accounts)} | Entities: {len({row['Legal_Entity'] for row in accounts})} | Currencies: {len(valid_currencies)}")
    print(f"  Bank rows: {len(bank)} | GL rows: {len(gl)} | Forecast rows: {len(forecast)}")
    print(f"  Closing cash: USD {closing_cash:,.2f} | Minimum reserves: USD {reserve:,.2f} | Headroom: USD {headroom:,.2f}")
    print(f"  Exceptions: {dict(status_counts)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
