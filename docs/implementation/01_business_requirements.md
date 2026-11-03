# Business requirements register

The register below is a proposed portfolio baseline for the fictional TechGiant scenario. No stakeholder workshop or approval is claimed.

| ID | Requirement | Rationale | Priority | Owner role | Acceptance criteria |
|---|---|---|---|---|---|
| BR-001 | Consolidate account balances across five accounts, four entities and four currencies | Give treasury one view of cash | High | Treasury operations | Account, currency and entity totals reconcile to the account master |
| BR-002 | Import bank transactions with validated reference, account, currency and amount fields | Prevent incomplete source records | High | Bank connectivity / data analyst | Invalid or blank keys are rejected and reported |
| BR-003 | Exchange ERP/GL cash postings for reconciliation | Compare bank activity with book records | High | Finance systems | GL rows retain source reference, account, currency and cash impact |
| BR-004 | Aggregate GL records by reference, account and currency before matching | Prevent duplicate keys from multiplying bank rows | High | Reconciliation analyst | BT014 is classified as Duplicate in GL |
| BR-005 | Classify missing, mismatched and duplicate records | Create an actionable review queue | High | Treasury control owner | 20 bank rows classify as 17 matched, 1 mismatch, 1 missing and 1 duplicate |
| BR-006 | Run a reverse GL completeness check | Find book entries without bank support | High | Finance control owner | GL999 appears as GL-only review |
| BR-007 | Calculate closing cash and reserve headroom in USD | Support liquidity review | High | Treasury analyst | Results equal the source-derived cash and reserve calculations |
| BR-008 | Provide a four-week scenario forecast | Support short-term planning | Medium | Treasury analyst | Forecast rolls forward from the prior scenario closing balance |
| BR-009 | Retain evidence and control totals for reruns | Support review and handover | Medium | Project analyst | Validator, workbook and source files can be rerun from the repository |

