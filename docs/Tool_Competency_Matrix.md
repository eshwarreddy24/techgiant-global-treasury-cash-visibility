# Tool competency matrix

This project is presented as work I designed and documented independently. The table separates what is reproducible in this repository from what is supported by historical screenshots or design notes.

| Tool | Capability shown | Project activity | Deliverable | Supporting evidence | Status |
|---|---|---|---|---|---|
| Excel | Financial modelling and controls | Built linked sheets for bank activity, GL postings, reconciliation, cash, reserves and forecast | `TechGiant_Global_Cash_Visibility_Project.xlsx` | Workbook formulas and control sheets | Included |
| Python | Validation and repeatable checks | Recalculated mappings, reconciliation statuses, cash, reserves, forecast and Tableau extracts | `scripts/validate_project.py` and `tests/` | Passing local validator and regression tests | Included and tested |
| Alteryx | Data preparation and matching workflow | Worked through Input Data, field preparation, Formula, Filter, Join, Summarize, Unique, Browse and Output Data steps | Rebuild guide and historical screenshots in the supplied reference PDF | [`Alteryx evidence`](tool-evidence/Alteryx_Implementation_Evidence.md) | Screenshot evidence; native workflow not included |
| Tableau | Worksheet and dashboard design | Built an earlier cash movement, exception and KPI dashboard prototype | Tableau-ready CSV extracts and historical reference PDF | [`Tableau evidence`](tool-evidence/Tableau_Implementation_Evidence.md) | Historical prototype; current workbook not included |
| GitHub | Version control and reproducibility | Structured the project, added CI, documentation and source-derived checks | Repository, workflow and README | `.github/workflows/validate.yml` | Included |
| Kyriba | TMS integration research | Documented a possible API and reconciliation integration pattern | `documentation/Kyriba_API_Research_Log.md` | Research notes only | Design research |
| SAP | Future integration context | Mapped the likely ERP/GL handoff without claiming SAP execution | Architecture and assumptions documentation | No SAP connection or export is included | Future scope |

The project does not use a screenshot alone as proof that a native tool file can be rerun. That distinction is intentional and keeps the case study credible.
