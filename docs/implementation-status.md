# Implementation status

| Capability | Status | Evidence in this repository |
|---|---|---|
| Synthetic Excel cash model | Included as supplied case-study workbook | `TechGiant_Global_Cash_Visibility_Project.xlsx` |
| Source-derived Python validation | Completed | `scripts/validate_project.py` |
| Bank-to-GL reconciliation logic | Recalculated and validated in Python; Alteryx recreation documented | `data/expected_bank_reconciliation.csv`, `documentation/Alteryx_Workflow_Guide.md` |
| Alteryx tool evidence | Historical screenshots reviewed; raw PDFs are not published | `docs/tool-evidence/Alteryx_Implementation_Evidence.md` |
| Native Alteryx workflow | Not included | No `.yxmd` or `.yxzp` artifact is claimed |
| Tableau-ready extracts | Included and validated | `tableau/*.csv` |
| Tableau prototype evidence | Historical screenshots reviewed; values are not current USD KPIs | `docs/tool-evidence/Tableau_Implementation_Evidence.md` |
| Native Tableau workbook | Not verified | Invalid XML artifact removed from the public repository |
| Excel preview images | Included as supplied references | `TechGiant_Dashboard_Preview.png`, `TechGiant_Forecast_Preview.png` |
| Kyriba integration | Documentation research/design only | `documentation/Kyriba_API_Research_Log.md` |
| Live bank, ERP, SAP, or Kyriba connection | Not implemented | No production credentials or connections are included |

This status table is intentionally conservative. Resume claims should describe only work supported by the corresponding artifacts.
