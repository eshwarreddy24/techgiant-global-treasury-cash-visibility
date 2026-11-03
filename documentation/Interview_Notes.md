# Interview Notes — TechGiant Global Treasury Case Study

## 60-second project explanation

I developed an independent functional design and controls case study for a fictional multinational company called TechGiant Inc. The scenario involved five bank accounts across USD, GBP, EUR and INR. I used synthetic bank statement and general-ledger data to build a consolidated cash position, translate balances into USD using illustrative FX assumptions, and identify bank-to-book exceptions. I also built a four-week scenario forecast and documented a proposed TMS implementation lifecycle. Historical Alteryx and Tableau prototype evidence was reviewed, but no native Alteryx workflow or current-dataset Tableau workbook is included. I used Kyriba's Developer Portal documentation as a reference for the TMS/API context; I did not claim a live Kyriba implementation.

## Why this project?

It connects my prior experience with SAP-related enterprise workflows, project budgets, vendor/invoice information and financial record reconciliation to the treasury activities I am learning: cash visibility, liquidity, bank data, payment controls and financial reporting.

## Key terms to explain

- **Cash position:** The available cash balance at a specified point in time, based on the balances included in the model.
- **Liquidity headroom:** Cash above a defined minimum reserve; not the same as total cash.
- **Bank-to-book reconciliation:** Comparing bank statement movements with corresponding general-ledger records and investigating missing, duplicate or differing entries.
- **Cash forecasting:** Estimating future cash inflows and outflows using assumptions; it is not the same as the current cash position.
- **FX translation:** Converting local-currency balances into a reporting currency using an explicitly stated exchange-rate assumption.
- **TMS:** A system used to support treasury processes such as cash management, liquidity, payments and connectivity.

## Known case-study results

- 5 bank accounts / 4 currencies
- 20 bank statement transactions
- 21 GL rows
- 17 matched bank transactions
- 1 missing GL entry: BT004, -850 USD
- 1 amount mismatch: BT003, bank -90,000 USD vs GL -89,500 USD; variance -500 USD
- 1 duplicate GL reference: BT014, two GL rows total -240,000 EUR vs bank -120,000 EUR; variance +120,000 EUR
- 1 GL-only entry: GL999, -42,000 USD
- Consolidated closing cash: USD 3,776,601.50
- Liquidity headroom: USD 3,150,851.50

## Limitations to state proactively

- All company, transaction and FX data are synthetic.
- FX rates are illustrative, not market quotes.
- Cash is calculated from opening balances plus bank statement movements and is not adjusted for unresolved reconciliation exceptions.
- The forecast is based on editable scenario assumptions, not historical forecast accuracy.
- No live Kyriba tenant, bank connection, production payment, or API execution is represented unless separately performed and documented.
