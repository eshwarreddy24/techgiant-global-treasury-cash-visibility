# Data dictionary

## Master and source inputs

| File | Key fields | Purpose |
|---|---|---|
| `account_master.csv` | `Account_ID`, `Legal_Entity`, `Currency` | Account ownership, opening cash, and minimum reserve |
| `fx_rates.csv` | `Currency`, `USD_per_1_Unit` | Illustrative reporting-currency translation |
| `bank_transactions.csv` | `Bank_Ref`, `Account_ID`, `Currency` | Synthetic bank statement movement |
| `gl_transactions.csv` | `GL_Ref`, `Account_ID`, `Currency`, `GL_Document` | Synthetic ERP/GL cash postings |

## Derived control outputs

| File | Purpose |
|---|---|
| `expected_bank_reconciliation.csv` | Bank-side status, GL aggregate, match count, and variance |
| `expected_gl_only_review.csv` | GL completeness result for every GL row |
| `cash_position.csv` | Account cash, reserves, and USD headroom |
| `four_week_forecast.csv` | Four scenario weeks by account |

## Tableau extracts

The `tableau/` CSVs are presentation-ready copies of source-derived results. The validator compares them to the underlying calculations before a run is accepted.
