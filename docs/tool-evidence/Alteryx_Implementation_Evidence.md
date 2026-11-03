# Alteryx implementation evidence

## What the evidence shows

The supplied Alteryx reference PDF records a working session in Alteryx Designer. The visible workflow uses the familiar preparation and matching pattern for a bank-to-GL control:

1. Read bank statement and ERP/GL inputs.
2. Rename and select fields.
3. Standardise references, amounts and data types.
4. Apply Formula and Filter logic.
5. Join bank rows to summarised GL rows.
6. Use the left and right outputs to isolate missing and GL-only items.
7. Summarise and inspect the results.
8. Send the prepared outputs to files.

The screenshots show Input Data, Dynamic Rename, Select, Formula, Filter, Join, Summarize, Unique, Browse and Output Data tools. They are useful evidence of hands-on workflow development, but they are not a substitute for the native workflow file.

## Evidence location

- [`tab-13-reference.pdf`](../../evidence/reference-pdfs/tab-13-reference.pdf) — supplied Alteryx reference material.
- [`Alteryx_Workflow_Guide.md`](../../documentation/Alteryx_Workflow_Guide.md) — repository-relative rebuild instructions.
- [`scripts/validate_project.py`](../../scripts/validate_project.py) — reproducible Python control calculation.

The PDF contains personal machine-path details in some original screenshots. The repository retains the supplied reference artifact for traceability, but does not reproduce those paths in the README or project narrative.

## Row-count reconciliation

The current canonical CSVs contain 20 bank rows and 21 GL rows. The rebuild guide expects:

| Stage | Expected rows |
|---|---:|
| Bank input | 20 |
| GL input | 21 |
| Joined bank references | 19 |
| Left-only bank references | 1 |
| Right-only GL references | 1 |
| Unioned bank-side output | 20 |

The older screenshot evidence shows 22–23 records at an earlier input stage. The repository does not contain the native workflow or its earlier source workbook, so that difference cannot be proven to be a header, blank row, used-range row or prior dataset version. It is documented rather than silently forced to match the current CSVs.

## Status

No native `.yxmd` or `.yxzp` file is present in this repository. The Alteryx material is therefore described as historical execution evidence plus a reproducible rebuild guide. A future native workflow should use the current `data/` files, repository-relative paths and the Python validator as its control total.
