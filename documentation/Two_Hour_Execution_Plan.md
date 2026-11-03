# Two-Hour Execution Plan

## Goal for this sprint

Finish a credible, evidence-backed **simulated Treasury Cash Visibility & Reconciliation case study**. The Excel model is already prepared. Your local work is to validate it, build and run the Alteryx workflow, create a Tableau dashboard, record Kyriba Developer Portal research, and publish the project.

**Do not claim live Kyriba configuration or API execution.** Your actual working platforms are Excel, Alteryx and Tableau. The Kyriba Developer Portal is a documentation/research source unless your account separately provides an authorised sandbox.

## Files to start with

- `TechGiant_Global_Cash_Visibility_Project.xlsx`
- `data/bank_transactions.csv`
- `data/gl_transactions.csv`
- `data/account_master.csv`
- `data/fx_rates.csv`
- `tableau/tableau_cash_position.csv`
- `tableau/tableau_daily_cash_flows.csv`
- `tableau/tableau_exception_summary.csv`
- `tableau/tableau_four_week_forecast.csv`

Extract the ZIP to a normal working folder such as `Documents/TechGiant_Treasury_Project`.

## Time-boxed plan

### 00–15 minutes: Excel model review

1. Open the Excel workbook.
2. Read `00_ReadMe`.
3. Inspect `01_Account_Master`, `02_FX_Rates`, `03_Bank_Transactions` and `04_GL_Transactions`.
4. Open `05_Reconciliation` and identify BT003, BT004 and BT014.
5. Open `05B_GL_Only_Check` and identify GL999.
6. Open `06_Cash_Position`, `07_Dashboard`, `08_4W_Forecast` and `09_Control_Test_Cases`.
7. Confirm all 10 controls show PASS.

Expected controls:
- Closing cash USD: 3,776,601.50
- Liquidity headroom USD: 3,150,851.50
- Bank transactions: 20
- Bank-side exceptions: 3
- GL-only items: 1
- Reconciliation: 17 matched, 1 missing, 1 amount mismatch, 1 duplicate

### 15–50 minutes: Build the Alteryx reconciliation workflow

Use Alteryx Designer. Detailed tool-by-tool steps and expressions are in `Alteryx_Workflow_Guide.md`.

Minimum workflow:
1. Input Data: `data/bank_transactions.csv`.
2. Input Data: `data/gl_transactions.csv`.
3. GL branch: Summarize GL by `GL_Ref`, `Account_ID`, `Currency`; create `GL_Amount_Total` (Sum of `GL_Cash_Impact_Local`) and `GL_Tx_Count` (Count of `GL_Ref`).
4. Join bank data (left) to summarized GL (right) using three keys: `Bank_Ref` = `GL_Ref`, `Account_ID` = `Account_ID`, and `Currency` = `Currency`.
5. J output: calculate variance and status; it should capture matched, amount mismatch and duplicate references.
6. L output: label bank transactions with no GL reference as `Missing in GL`.
7. Union the J and L results by field name and write `outputs/bank_side_reconciliation.csv`.
8. R output: label unmatched GL records `GL-only: investigate` and write `outputs/gl_only_review.csv`.
9. Run the workflow and verify record counts and exceptions.

Alteryx tool references:
- Join: https://help.alteryx.com/current/en/designer/tools/join/join-tool.html
- Summarize: https://help.alteryx.com/current/designer/summarize-tool
- Formula: https://help.alteryx.com/designer/current/en/tools/preparation/formula-tool.html

### 50–85 minutes: Build the Tableau dashboard

Follow `Tableau_Dashboard_Guide.md`.

Build at least these four views:
1. Closing cash by account (USD).
2. Liquidity headroom by account (USD).
3. Daily net cash movement (USD).
4. Reconciliation exception count by status.

If time permits, add the four-week forecast line chart. Assemble the views into one dashboard and save a Tableau workbook or packaged workbook if supported by your version.

### 85–100 minutes: Kyriba Developer Portal research

1. Sign in to https://developer.kyriba.com/.
2. Search the portal catalogue for cash balance/position, bank transactions/statements, payments and ERP integration.
3. Record the exact API title, version, method/path if the portal displays them, and important response fields in `10_Kyriba_API_Research` or `Kyriba_API_Research_Log.md`.
4. Capture one screenshot of the documentation page with all tokens, credentials and private account data hidden.
5. If you do not have an authorised sandbox, record “documentation reviewed only”. Do not claim API execution.

Kyriba's official overview describes the Developer Portal as providing an API catalogue, Swagger documentation, Postman examples, changelogs and use cases: https://www.kyriba.com/resources/fact-sheets/kyriba-marketplace/

### 100–120 minutes: GitHub and evidence

1. Create a public repository named `techgiant-global-treasury-cash-visibility`.
2. Upload the workbook, `data/`, `tableau/` and `documentation/`.
3. Add the root README.
4. Add screenshots of the Alteryx workflow run, Tableau dashboard and Excel dashboard.
5. Review the README's scope statement and keep the simulated-project disclaimer.

## Minimum acceptance criteria

- Excel: all 10 control tests PASS; no formula errors.
- Alteryx: output has 20 bank-side rows; 17 matched, 1 missing, 1 mismatch, 1 duplicate; separate output has one GL-only item.
- Tableau: at least four clear views on one dashboard.
- Kyriba: exact documentation details recorded only if you inspect them; no invented endpoint names.
- GitHub: README, workbook, source data, workflow and dashboard evidence uploaded.

If you cannot complete Tableau or Alteryx in the two-hour window, do not pretend it is complete. Finish Excel validation and the Alteryx workflow first; save unfinished items as pending.
