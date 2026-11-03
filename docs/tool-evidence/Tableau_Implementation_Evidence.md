# Tableau implementation evidence

## What the evidence shows

The supplied Tableau reference PDF shows an earlier dashboard prototype with separate worksheets for:

- Cash movement
- Bank outflows
- Reconciliation status
- ERP-only exceptions
- KPI cards and a treasury dashboard layout

That evidence demonstrates practical worksheet and dashboard work: connecting a source, placing dimensions and measures, building bar charts, arranging KPI views and assembling a dashboard for treasury users.

## Historical versus current data

The reviewed screenshots are dated from an earlier project iteration and display INR-denominated values. The current repository uses a different, audited synthetic dataset with USD reporting outputs. The screenshots are therefore treated as historical prototype evidence and are not used for the current KPI figures.

- [`tableau/`](../../tableau/) — current validated CSV extracts.
- [`Tableau_Dashboard_Guide.md`](../../documentation/Tableau_Dashboard_Guide.md) — instructions for rebuilding the current dashboard.

## Current dashboard build path

The current extracts support:

1. Closing cash by account.
2. Liquidity headroom by account.
3. Daily cash movement.
4. Reconciliation exceptions by status.
5. Four-week projected closing cash.

The values are source-derived and can be checked against `scripts/validate_project.py`. The repository does not include fresh screenshots from a corrected Tableau dashboard, so the historical PDF is not presented as the current USD dashboard.

## Status

No verified native `.twb` or `.twbx` file is present. The old XML artifact was removed from the public repository because it was not portable and contained local paths. The next genuine Tableau deliverable would be a rebuilt workbook opened and checked in Tableau Desktop against the current CSV extracts.
