# Repository audit

## Issues found

- The project needed a clearer functional-design and TMS implementation narrative.
- Existing documentation was spread across `docs/` and `documentation/` without a single implementation pack.
- Alteryx screenshots support historical workflow development, but no native `.yxmd` or generated output files are present.
- The Tableau XML artifact was not a portable packaged workbook and exposed local paths.
- The supplied reference PDFs were not necessary for reproducible validation and could expose screenshot-local paths.
- The GL completeness extract contains every GL row with a status, so it is broader than a GL-only exception list.

## Changes made

- Added the proposed implementation lifecycle documents under `docs/implementation/`.
- Added source-to-target mapping, test scenarios and requirements traceability CSVs.
- Added resume and interview wording with evidence boundaries.
- Added GitHub profile metadata guidance.
- Kept the current source-derived validator and test suite as the executable quality gate.
- Removed public raw reference PDFs and the invalid legacy Tableau XML artifact from the repository.
- Updated evidence and status documentation to distinguish completed, proposed and not-performed work.

## Validation

The final validation should include:

```text
python scripts/validate_project.py
python -m unittest discover -s tests -v
git diff --check
```

The validator does not recalculate Excel formulas, execute Alteryx or open Tableau. Those application checks remain manual and are not represented as completed.

## Remaining manual work

- Build and save a genuine Alteryx `.yxmd` using repository-relative inputs.
- Export and commit the Alteryx output files after reconciling counts to 20 bank rows and 21 GL rows.
- Rebuild the current USD Tableau workbook and verify it in Tableau Desktop.
- Add sanitised current screenshots only after the workbook is checked.
- Replace illustrative FX and scenario assumptions with governed inputs before treating the model as operational.
