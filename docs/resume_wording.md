# Resume and interview wording

## Safe to use now

**Global Treasury Cash Visibility & Bank-to-GL Reconciliation | Excel, Python | Independent case study**

- Built a multi-currency cash-position and liquidity-headroom model for five synthetic bank accounts across four legal entities and four currencies using documented illustrative FX assumptions.
- Developed bank-to-GL control logic that classified 20 bank transactions into 17 matched records, one amount mismatch, one missing GL posting and one duplicate GL reference; separately identified one GL-only journal for review.
- Created formula-driven Excel checks and a four-week scenario forecast, with 10 workbook control cases showing `PASS`.
- Reviewed Kyriba Developer Portal documentation for payment-data integration concepts; no live Kyriba or SAP integration was performed.

## Add only after native files and outputs are verified

**Alteryx:** Built and ran a native workflow that prepares bank and GL data, aggregates duplicate keys, joins the streams and exports reconciled and exception outputs. Add only when the `.yxmd`, output files and counts have been checked against the canonical CSVs.

**Tableau:** Built and validated a current-dataset Tableau workbook showing cash, headroom, movements and reconciliation exceptions. Add only when a verified `.twb` or `.twbx` and current USD screenshots exist.

## 60-second explanation

I built an independent treasury case study around a simple control problem: bank activity and GL postings arrive separately, but treasury needs one cash view and a reliable way to identify breaks. I used synthetic data for five accounts across four entities and four currencies. I aggregated GL rows by reference, account and currency before matching them to bank activity, which exposed one amount mismatch, one missing posting, one duplicate GL reference and one separate GL-only journal. I calculated closing cash and reserve headroom independently from the bank movements, then added a four-week scenario forecast. The Excel model and Python checks are reproducible here; Alteryx and Tableau are documented as evidence or proposed rebuilds, not presented as live integrations.

## 3-minute explanation

Start with the business question: how much cash is visible, and how much confidence do we have in the bank-to-book support? Explain the composite key and why GL aggregation must happen before the join. Walk through BT003, BT004, BT014 and GL999, then explain that unresolved exceptions are not netted into closing cash. Finish with the implementation view: requirements, field mapping, control totals, test scenarios, migration rehearsal and cutover planning are documented as proposed design, while the actual completed artefacts are the Excel workbook, source-derived Python validation, tests and current CSV extracts.
