# Tableau Dashboard Guide — Treasury Cash Visibility

## Data files

Connect to these CSVs in the `tableau/` folder:
- `tableau_cash_position.csv`
- `tableau_daily_cash_flows.csv`
- `tableau_exception_summary.csv`
- `tableau_four_week_forecast.csv`

In Tableau Desktop, under Connect choose Text File and select the relevant CSV. Tableau's official connector instructions are here: https://help.tableau.com/current/pro/desktop/en-us/examples_excel.htm (the same Connect workflow applies to Excel; for CSV choose Text File).

## Worksheet 1 — Closing Cash by Account (USD)

Data source: `tableau_cash_position.csv`

1. Drag `Account_ID` to Rows.
2. Drag `Closing_Balance_USD` to Columns.
3. Select Bar in Show Me if Tableau does not automatically choose a bar.
4. Drag `Currency` to Color.
5. Drag `Closing_Balance_USD` to Label.
6. Format the axis as USD currency.
7. Rename the worksheet `Closing Cash by Account (USD)`.

## Worksheet 2 — Liquidity Headroom by Account (USD)

Same data source.

1. Duplicate Worksheet 1.
2. Replace `Closing_Balance_USD` with `Liquidity_Headroom_USD`.
3. Keep `Account_ID` on Rows and `Currency` on Color.
4. Format as USD and rename the worksheet.

Interpretation: headroom is cash above the account's synthetic minimum reserve, not the same as total cash.

## Worksheet 3 — Daily Net Cash Movement (USD)

Data source: `tableau_daily_cash_flows.csv`.

1. Drag `Value_Date` to Columns and make it a continuous Day or Exact Date.
2. Drag `Cash_Impact_USD` to Rows.
3. Select Bar.
4. Drag `Flow_Type` to Color.
5. Format the y-axis as USD.
6. Rename `Daily Net Cash Movement (USD)`.

Receipt rows are positive; payment rows are negative. Do not change negative cash impacts to positive for this chart.

## Worksheet 4 — Reconciliation Exceptions

Data source: `tableau_exception_summary.csv`.

1. Drag `Status` to Rows.
2. Drag `Count` to Columns.
3. Select Bar.
4. Drag `Exception_Type` to Color.
5. Show labels and sort by Count.
6. Rename `Reconciliation Exceptions by Status`.

Expected counts: Matched 17; Missing in GL 1; Amount mismatch 1; Duplicate in GL 1; GL-only 1. The first four statuses include 20 bank-side transactions; GL-only is reported separately.

## Worksheet 5 — Four-Week Cash Forecast (optional but recommended)

Data source: `tableau_four_week_forecast.csv`.

1. Set `Week_End` to Date if it imports as text.
2. Drag `Week_End` to Columns.
3. Drag `Projected_Closing_USD` to Rows.
4. Use Line marks.
5. This measure is the sum across five accounts after translation to USD.
6. Rename `Four-Week Projected Closing Cash (USD)`.

## Dashboard assembly

1. Create a new Dashboard. Choose a fixed size around 1200 x 800 or Automatic.
2. Place the closing cash and headroom views side by side.
3. Place the daily cash movement and exception status views below.
4. Add the forecast view if completed.
5. Add a text note: “Synthetic training case study; illustrative FX rates; not a live Kyriba or bank connection.”
6. Add dashboard title: `TechGiant Inc. | Global Treasury Cash Visibility`.
7. Check titles, labels and currency formatting; avoid clutter.

## Expected values to use for a top-line text/KPI note

- Consolidated closing cash: USD 3,776,601.50
- Consolidated liquidity headroom: USD 3,150,851.50
- Bank transactions: 20
- Bank-side exceptions: 3
- GL-only items: 1

Do not imply these are actual TechGiant or Kyriba client figures. They are calculated from the synthetic case-study workbook.
