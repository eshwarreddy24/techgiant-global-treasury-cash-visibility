# START HERE — TechGiant Global Treasury Cash Visibility Case Study

## 1. What this project is

An independent, simulated Finance Transformation / Treasury Management System case study for a fictional multinational company, TechGiant Inc. The objective is to build a consolidated cash view, reconcile bank movements to general-ledger (GL) postings, prepare a short-term liquidity forecast, and document how a TMS such as Kyriba could support the process.

**Scope and honesty:** This project uses synthetic company, bank, transaction and FX data. The data is not from TechGiant, a real client or a real bank. Excel is used for the financial model, Alteryx for data preparation and reconciliation, and Tableau for visual reporting. Kyriba is used for product/API documentation research only unless an authorised sandbox/API execution is separately completed and evidenced. This project is not a live Kyriba implementation or a production integration.

## 2. Files to open first

1. `TechGiant_Global_Cash_Visibility_Project.xlsx` — main calculation model and control test cases.
2. `data/bank_transactions.csv` — synthetic bank statement movements.
3. `data/gl_transactions.csv` — synthetic GL cash postings, including deliberate exceptions.
4. `data/account_master.csv` — account, entity, currency and reserve data.
5. `data/fx_rates.csv` — illustrative exchange rates to USD.
6. `documentation/Alteryx_Workflow_Guide.md` — exact Alteryx build steps.
7. `documentation/Tableau_Dashboard_Guide.md` — exact Tableau build steps.
8. `documentation/Kyriba_API_Research_Log.md` — what to inspect and record in the Kyriba portal.
9. `documentation/Interview_Notes.md` — explanation of the case and its limitations.

## 3. Recommended end-to-end sequence

### Phase A — Excel model (start here)

1. Open the workbook and read `00_ReadMe`.
2. Review `01_Account_Master` and `02_FX_Rates`.
3. Review `03_Bank_Transactions` and `04_GL_Transactions`.
4. In `05_Reconciliation`, review BT003, BT004 and BT014.
5. In `05B_GL_Only_Check`, review GL999.
6. Review `06_Cash_Position`, `07_Dashboard` and `08_4W_Forecast`.
7. Open `09_Control_Test_Cases`; the supplied model should show 10 PASS checks. If any check fails after you edit an input, investigate before proceeding.

Core formulas:

- Net bank movement (local currency) = SUM of bank cash impacts for an account.
- Closing cash (local currency) = Opening balance + Net bank movement.
- Closing cash (USD) = Closing cash (local currency) × USD-per-local-currency FX rate.
- Liquidity headroom (local) = Closing cash − Minimum reserve.
- Liquidity headroom (USD) = Local headroom × FX rate.
- Reconciliation variance = Bank cash impact − GL cash impact.

A positive or negative variance is not automatically a loss; it is an exception to investigate. Do not offset or hide exception records.

### Phase B — Alteryx workflow

Build a workflow called `TechGiant_Bank_GL_Reconciliation.yxmd` using the input files in `data/`.

1. Add Input Data for `bank_transactions.csv` and `gl_transactions.csv`.
2. On the GL branch, use Summarize: Group By `GL_Ref`, `Account_ID`, `Currency`; Sum `GL_Cash_Impact_Local` as `GL_Amount_Total`; Count `GL_Ref` as `GL_Tx_Count`.
3. Join bank transactions (left input) to summarized GL (right input) on three keys: Bank `Bank_Ref` = GL `GL_Ref`, plus `Account_ID`, plus `Currency`.
4. On the Join J output, use Formula to calculate `Variance_Local = [Cash_Impact_Local] - [GL_Amount_Total]`.
5. Add `Reconciliation_Status` using this priority: if `GL_Tx_Count > 1`, `Duplicate in GL`; else if `Abs([Variance_Local]) > 0.01`, `Amount mismatch`; otherwise `Matched`.
6. On Join L (bank-side unmatched), set GL amount and count to zero, set variance equal to bank impact, and label `Missing in GL`.
7. Union the J and L branches by field name and write `outputs/bank_side_reconciliation.csv`.
8. On Join R (GL-side unmatched), add `Review_Status = "GL-only: investigate"` and write `outputs/gl_only_review.csv`.
9. Run the workflow and save the `.yxmd` file plus a screenshot of the successful run and output counts.

Expected counts: Bank input 20; GL input 21; J output 19; L output 1; R output 1; combined bank-side reconciliation 20. Final bank-side statuses: 17 Matched, 1 Missing in GL, 1 Amount mismatch, 1 Duplicate in GL. One separate GL-only record.

### Phase C — Tableau dashboard

Use the curated CSVs in `tableau/`. Connect each through Tableau's **Text File** connector. Build at least four worksheets:

1. Closing cash by account (USD) — bar chart.
2. Liquidity headroom by account (USD) — bar chart.
3. Daily net cash movement (USD) — date-based bar chart with receipts positive and payments negative.
4. Reconciliation exceptions by status — bar chart.
5. Optional: Four-week projected closing cash (USD) — line chart.

Create a dashboard around 1200 × 800 or Automatic. Place cash/headroom at the top, movement/exceptions below, and forecast if completed. Add a note: “Independent simulated case study; synthetic data and illustrative FX rates; no live Kyriba or bank connection.” Save a `.twb` or `.twbx` and export a dashboard image if your Tableau edition supports it.

### Phase D — Kyriba Developer Portal research

Sign in to `https://developer.kyriba.com/`. Search the portal catalogue and documentation for actual resources related to cash balances/positions, bank transactions/statements, payments and ERP integration. For each relevant resource, record only what the portal visibly shows:

- Exact resource/API title and version.
- HTTP method and path, if shown.
- Purpose and key request parameters.
- Important response fields.
- Authentication approach (describe only; never store credentials).
- Whether a sandbox/API execution option is actually available.
- Review date and sanitized screenshot filename.

Do not invent endpoint paths, API field names, authentication schemes, permissions or sandbox access. If you only read documentation, state: “API documentation reviewed; no API execution performed.” The official Kyriba overview describes the Developer Portal as providing an API catalogue, Swagger documentation, Postman samples, change logs and use cases: https://www.kyriba.com/resources/fact-sheets/kyriba-marketplace/

### Phase E — GitHub publication

Create a repository named `techgiant-global-treasury-cash-visibility` and upload:

- Root `README.md` and this `START_HERE.md`.
- The Excel workbook.
- `data/` source CSVs.
- `tableau/` curated CSVs.
- `documentation/` guides and interview notes.
- `outputs/` Alteryx output CSVs after your workflow runs.
- `evidence/` screenshots of Excel checks, Alteryx workflow/run and Tableau dashboard.
- `TechGiant_Bank_GL_Reconciliation.yxmd`.
- Your Tableau workbook `.twb` or `.twbx` if your edition allows saving it.

Before making the repository public, inspect every file for credentials, tokens, personal information or real company data. Never upload Kyriba API keys/tokens, private connection strings or confidential screenshots.

## 4. Synthetic example data

Account master:

| Account | Legal entity | Bank | Currency | Opening balance | Minimum reserve |
|---|---|---|---|---:|---:|
| TG-US-001 | TechGiant US Inc. | NorthStar Bank | USD | 1,250,000 | 200,000 |
| TG-US-002 | TechGiant US Inc. | Metro Capital Bank | USD | 780,000 | 150,000 |
| TG-UK-001 | TechGiant UK Ltd. | Crown Union Bank | GBP | 450,000 | 75,000 |
| TG-DE-001 | TechGiant GmbH | RheinBank | EUR | 620,000 | 100,000 |
| TG-IN-001 | TechGiant India Pvt Ltd. | Western Peninsula Bank | INR | 35,000,000 | 5,000,000 |

Illustrative FX rates (not market data): USD 1.00; GBP 1.33; EUR 1.16; INR 0.012, all expressed as USD per one unit of local currency.

Sample bank transactions:

| Bank ref | Account | Currency | Description | Cash impact |
|---|---|---|---|---:|
| BT001 | TG-US-001 | USD | Customer receipt | +220,000 |
| BT002 | TG-US-001 | USD | Supplier payment | −140,000 |
| BT003 | TG-US-001 | USD | Payroll payment | −90,000 |
| BT004 | TG-US-001 | USD | Bank service fee | −850 |
| BT009 | TG-UK-001 | GBP | Customer receipt | +95,000 |

Designed reconciliation cases:

- BT003: Bank impact −90,000 USD versus GL impact −89,500 USD; variance −500 USD.
- BT004: Bank service fee −850 USD has no matching GL posting.
- BT014: Bank payment −120,000 EUR has two GL entries totalling −240,000 EUR; flag as duplicate GL reference (do not treat the aggregate as an accepted match).
- GL999: GL-only posting −42,000 USD with no matching bank reference.

Current model outputs, based on synthetic data:

- Five accounts across four currencies.
- 20 bank transactions and 21 GL rows.
- 17 matched bank transactions; one missing GL, one amount mismatch and one duplicate GL reference.
- One separate GL-only item.
- Consolidated closing cash of USD 3,776,601.50.
- Liquidity headroom above minimum reserves of USD 3,150,851.50.

The closing cash is calculated from opening balances plus bank statement movements. It is not adjusted for unresolved reconciliation exceptions. Exception counts must therefore be shown separately and unresolved items must be investigated before real-world reliance.

## 5. Definition of done

The project is ready to describe as completed only when:

- The Excel model has been reviewed and the 10 control tests pass.
- The Alteryx workflow has been built, run and saved; counts and exception results agree with expected outputs.
- The Tableau dashboard has been created and saved with the required views.
- Kyriba API research records exact information seen in the user's portal, or transparently states that only documentation was available.
- GitHub contains the workbook, synthetic data, saved workflows, dashboard evidence and clear limitations.

## 6. Resume wording (only after corresponding work is complete)

**Global Treasury Cash Visibility & Reconciliation | Excel, Alteryx, Tableau | Independent Simulated Case Study**

- Built a multi-currency cash-position model using synthetic bank transaction data across five accounts in USD, GBP, EUR and INR, translating balances into USD using documented illustrative FX assumptions.
- Built and ran an Alteryx workflow to aggregate GL postings, match bank and GL datasets on transaction reference/account/currency, and produce matched and exception outputs.
- Developed a Tableau dashboard to present closing cash, liquidity headroom, daily cash movement and reconciliation exceptions.
- Reviewed Kyriba Developer Portal documentation for cash visibility and integration concepts; no live Kyriba implementation or API execution claimed unless separately tested and evidenced.

Use only the bullets for the work you actually completed. If Excel is the only completed component, use the Excel-only wording in `documentation/Resume_Wording_After_Completion.md`.
