# Tableau deliverables

This folder contains Tableau-ready CSV extracts and dashboard preview images are stored at the project root.

## Current status

The repository does **not** contain a verified native Tableau workbook. The previously supplied file named `.twbx` was actually Tableau XML rather than a packaged ZIP workbook, and it referenced an older schema/path. It has been quarantined under `tableau/legacy/` as:

`TechGiant_Global_Treasury_Dashboard.legacy.twb`

Do not present that legacy file as a working `.twbx`. Use the CSV extracts and [`documentation/Tableau_Dashboard_Guide.md`](../documentation/Tableau_Dashboard_Guide.md) to build a native workbook in Tableau Desktop, then save and test the resulting `.twb` or `.twbx` before adding it to the repository.

## Extracts

- `tableau_cash_position.csv`
- `tableau_daily_cash_flows.csv`
- `tableau_exception_summary.csv`
- `tableau_four_week_forecast.csv`

The validator checks these extracts against the source-derived data.
