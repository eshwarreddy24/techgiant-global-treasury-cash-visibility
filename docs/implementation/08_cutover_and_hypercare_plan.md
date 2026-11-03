# Proposed cutover and hypercare plan

This is a proposed plan for a future implementation. No go-live or hypercare activity has taken place.

## Cutover checklist

- Confirm source files, mappings and control totals.
- Complete open data-quality and reconciliation reviews.
- Confirm roles, access and approval paths.
- Rehearse the opening-balance and first-day transaction load.
- Compare parallel outputs before cutover.
- Record go/no-go decision and unresolved risks.
- Preserve rollback and support contacts.

## Proposed severity model

| Severity | Example | Response expectation |
|---|---|---|
| Critical | Cash position unavailable or materially misstated | Immediate incident ownership and management escalation |
| High | Bank feed or GL exchange fails for a key entity | Same-day investigation and controlled workaround |
| Medium | One account or exception report is delayed | Resolve within agreed support window |
| Low | Label, formatting or documentation defect | Schedule for the next release |

## Hypercare exit criteria

Exit would require stable daily loads, reconciled control totals, no unresolved critical issues, accepted exception ownership and a documented hand-off to business-as-usual support. These are proposed criteria, not completed sign-off.
