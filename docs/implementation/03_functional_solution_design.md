# Functional solution design

This is a proposed TMS-neutral design for the synthetic case study. It is not a configured Kyriba, FIS, SAP or bank environment.

## Functional scope

1. Receive bank statement and GL extracts.
2. Validate file structure, mandatory fields and control totals.
3. Standardise references, account IDs, currencies and signed cash impacts.
4. Aggregate GL rows by `(reference, account_id, currency)`.
5. Match bank rows to the aggregated GL result.
6. Route mismatches, missing postings, duplicate references and GL-only items for review.
7. Calculate account closing cash, reserves, headroom and the scenario forecast.
8. Produce management-ready extracts and an audit trail.

## Proposed data flow

The current repository implements the calculation and validation in CSV, Excel and Python. A future TMS would replace file hand-offs with governed interfaces and operational queues, subject to security, connectivity and ownership decisions.

## Exception handling

Each exception should retain the source reference, account, currency, bank amount, GL total, match count, variance, status, owner, review date and resolution note. Those operational fields are proposed; the current sample contains the source-side control facts but not a live workflow or approval history.

## Reporting

The current outputs support cash position, reserve headroom, daily movements, exception counts and a four-week scenario. Currency labels and the reporting date should remain visible in any future dashboard.

