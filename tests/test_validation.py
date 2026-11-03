import csv
import subprocess
import sys
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class TreasuryValidationTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_project.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("source-derived TechGiant treasury validation succeeded", result.stdout)

    def test_forecast_totals(self):
        rows = read_csv(ROOT / "data" / "four_week_forecast.csv")
        expected = {
            "2026-11-08": (Decimal("3833851.50"), Decimal("3208101.50")),
            "2026-11-15": (Decimal("3803301.50"), Decimal("3177551.50")),
            "2026-11-22": (Decimal("3885551.50"), Decimal("3259801.50")),
            "2026-11-29": (Decimal("3867451.50"), Decimal("3241701.50")),
        }
        for week, (cash, headroom) in expected.items():
            subset = [row for row in rows if row["Week_End"] == week]
            self.assertEqual(sum(Decimal(row["Projected_Closing_USD"]) for row in subset), cash)
            self.assertEqual(sum(Decimal(row["Liquidity_Headroom_USD"]) for row in subset), headroom)

    def test_known_exception_references(self):
        rows = read_csv(ROOT / "data" / "expected_bank_reconciliation.csv")
        by_ref = {row["Bank_Ref"]: row for row in rows}
        self.assertEqual(by_ref["BT003"]["Reconciliation_Status"], "Amount mismatch")
        self.assertEqual(Decimal(by_ref["BT003"]["Variance_Bank_Less_GL"]), Decimal("-500"))
        self.assertEqual(by_ref["BT004"]["Reconciliation_Status"], "Missing in GL")
        self.assertEqual(by_ref["BT014"]["Reconciliation_Status"], "Duplicate in GL")


if __name__ == "__main__":
    unittest.main()
