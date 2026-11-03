# Risks, assumptions and dependencies

| Area | Risk or assumption | Treatment |
|---|---|---|
| Data | All records are synthetic and may not reflect production bank formats | Validate against approved source specifications |
| FX | Rates are illustrative and not market quotations | Replace with governed rates before live reporting |
| Connectivity | No bank, ERP, SAP, Kyriba or TMS connection is present | Treat interfaces as future design scope |
| Matching | Reference, account and currency are assumed to form a reliable key | Confirm business key and exception policy |
| Timing | File capture dates and cut-off rules are simplified | Define operational calendar and late-arrival handling |
| Security | No access model or credential flow is implemented | Complete security and segregation-of-duties review |
| Ownership | Exception owners are not assigned in the sample | Define roles and escalation paths |
| Migration | No production migration has been performed | Rehearse with approved source data and control totals |
| Reporting | Forecast is scenario-based and not back-tested | Add historical actuals before measuring forecast accuracy |
