# Data dictionary and source controls

All data in this folder is synthetic and created for the portfolio case study. The CSVs are the source-of-truth inputs and derived control outputs used by the validator.

| File | Role |
|---|---|
| `account_master.csv` | Account, legal entity, bank, currency, opening balance, and reserve assumptions |
| `fx_rates.csv` | Illustrative USD-per-local-currency rates |
| `bank_transactions.csv` | Synthetic bank statement movements |
| `gl_transactions.csv` | Synthetic ERP/GL postings |
| `expected_bank_reconciliation.csv` | Source-derived bank-to-GL control output |
| `expected_gl_only_review.csv` | Source-derived GL completeness output |
| `cash_position.csv` | Source-derived account cash and liquidity view |
| `four_week_forecast.csv` | Four-week scenario forecast by account |

The Python validator recalculates reconciliation and cash logic from the raw bank, GL, account, and FX files. It then compares the checked outputs and Tableau extracts to those calculations.

## Matching key

Bank and GL records are matched on:

```text
Bank_Ref = GL_Ref
Account_ID
Currency
```

Duplicate GL references remain visible. They are classified as **Duplicate in GL** and are not treated as a confirmed duplicate payment.
