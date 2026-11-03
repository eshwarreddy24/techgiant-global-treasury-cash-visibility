"""Validate the synthetic TechGiant treasury portfolio pack.

This script intentionally uses only the Python standard library so a reviewer
can run it without installing a data-science stack.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TABLEAU = ROOT / "tableau"


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def money(value: str) -> float:
    return float(value.replace(",", "").strip())


def main() -> int:
    required = [
        ROOT / "README.md",
        ROOT / "START_HERE.md",
        ROOT / "TechGiant_Global_Cash_Visibility_Project.xlsx",
        DATA / "account_master.csv",
        DATA / "bank_transactions.csv",
        DATA / "gl_transactions.csv",
        DATA / "cash_position.csv",
        DATA / "four_week_forecast.csv",
        TABLEAU / "tableau_cash_position.csv",
        TABLEAU / "tableau_exception_summary.csv",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        print("FAIL: missing required files:")
        print("\n".join(f"  - {item}" for item in missing))
        return 1

    accounts = read_csv("account_master.csv")
    bank = read_csv("bank_transactions.csv")
    gl = read_csv("gl_transactions.csv")
    cash = read_csv("cash_position.csv")
    with (TABLEAU / "tableau_exception_summary.csv").open(
        newline="", encoding="utf-8-sig"
    ) as handle:
        exceptions = list(csv.DictReader(handle))

    assert len(accounts) == 5, f"expected 5 accounts, found {len(accounts)}"
    assert len(bank) == 20, f"expected 20 bank rows, found {len(bank)}"
    assert len(gl) == 21, f"expected 21 GL rows, found {len(gl)}"
    assert len(cash) == 5, f"expected 5 cash-position rows, found {len(cash)}"

    bank_refs = {row["Bank_Ref"]: row for row in bank}
    gl_by_ref: dict[str, list[dict[str, str]]] = {}
    for row in gl:
        gl_by_ref.setdefault(row["GL_Ref"], []).append(row)

    assert len(gl_by_ref["BT014"]) == 2, "BT014 duplicate control is not present"
    assert "BT004" not in gl_by_ref, "BT004 should be missing from GL"
    assert "GL999" in gl_by_ref, "GL999 GL-only control is not present"
    assert money(bank_refs["BT003"]["Cash_Impact_Local"]) == -90000
    assert sum(money(row["GL_Cash_Impact_Local"]) for row in gl_by_ref["BT003"]) == -89500

    status_counts = {row["Status"]: int(row["Count"]) for row in exceptions}
    expected = {
        "Matched": 17,
        "Missing in GL": 1,
        "Amount mismatch": 1,
        "Duplicate in GL": 1,
        "GL-only: investigate": 1,
    }
    assert status_counts == expected, f"unexpected exception summary: {status_counts}"

    closing_cash = sum(money(row["Closing_Balance_USD"]) for row in cash)
    headroom = sum(money(row["Liquidity_Headroom_USD"]) for row in cash)
    assert round(closing_cash, 2) == 3776601.50, closing_cash
    assert round(headroom, 2) == 3150851.50, headroom

    suspicious = re.compile(r"(^|/)(\.env|.*secret.*|.*credential.*|.*token.*)$", re.I)
    flagged = [
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file() and suspicious.search(path.relative_to(ROOT).as_posix())
    ]
    assert not flagged, f"possible secret files found: {flagged}"

    print("PASS: TechGiant treasury portfolio structure and control totals are valid.")
    print(f"  Accounts: {len(accounts)} | Bank rows: {len(bank)} | GL rows: {len(gl)}")
    print(f"  Closing cash: USD {closing_cash:,.2f}")
    print(f"  Liquidity headroom: USD {headroom:,.2f}")
    print(f"  Exception summary: {status_counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
