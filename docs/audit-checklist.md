# Repository audit checklist

Completed during the portfolio correction pass:

- [x] Recalculated account, entity, currency, bank, GL, forecast, reserve, and headroom counts from CSV source data.
- [x] Recalculated bank-to-GL matching using reference, account, and currency.
- [x] Verified BT003 amount mismatch, BT004 missing GL posting, BT014 duplicate GL reference, and GL999 GL-only posting.
- [x] Verified the cash-position boundary: opening balance plus bank movement, without adjustment for unresolved reconciliation items.
- [x] Verified the four-week forecast row count and arithmetic.
- [x] Compared expected reconciliation outputs and Tableau-ready extracts with source-derived calculations.
- [x] Added duplicate-ID, account-reference, currency-reference, column, numeric, and credential-pattern checks.
- [x] Inspected the supplied Tableau artifact and quarantined it because it was XML with a `.twbx` extension, not a verified packaged workbook.
- [x] Documented that no native Alteryx `.yxmd` workflow is included.
- [x] Documented Kyriba as research/design only, with no live authentication, endpoint execution, bank connection, or production payment.
- [x] Added implementation status, assumptions, data dictionary, Tableau status, and publishing guidance.

The validator is the repeatable acceptance check:

```bash
python scripts/validate_project.py
```
