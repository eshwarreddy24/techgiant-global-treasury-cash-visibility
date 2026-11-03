# Data migration and reconciliation approach

This is a proposed mock migration approach. No production data migration was performed.

## Sequence

1. Profile source files and confirm ownership, capture date, schema and row counts.
2. Map source account, entity, currency, reference and signed amount fields.
3. Reject blank keys, invalid currencies, unknown accounts and malformed numeric values.
4. Load a controlled sample into a staging area.
5. Compare opening balances, transaction counts, duplicate keys and signed totals.
6. Reconcile bank-side classifications and reverse GL completeness.
7. Obtain review sign-off for unresolved exceptions before any cutover decision.

## Control totals

The current case-study totals are 20 bank rows, 21 GL rows, 17 matched bank rows, one mismatch, one missing GL posting, one duplicate GL reference and one separate GL-only item. These totals are used as comparison points, not as evidence of a production migration.

## Reject handling

Rejected records should be retained with a reason code and source reference. They should not be silently dropped or included in management cash totals until corrected and rerun.

