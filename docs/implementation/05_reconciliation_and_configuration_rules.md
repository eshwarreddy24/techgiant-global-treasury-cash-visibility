# Reconciliation and configuration rules

## Matching key

Use the composite key:

```text
(reference, account_id, currency)
```

The bank reference is matched to `GL_Ref`; account and currency must also agree.

## Processing order

1. Validate nonblank keys and compatible data types.
2. Aggregate GL rows by the composite key.
3. Retain `GL_Amount_Total` and `GL_Match_Count`.
4. Match bank rows to the aggregated result.
5. Classify duplicate keys before evaluating amount variance.
6. Run a reverse completeness check for GL rows without a bank reference.

## Classification

| Condition | Status |
|---|---|
| `GL_Match_Count > 1` | Duplicate in GL |
| `GL_Match_Count = 0` | Missing in GL |
| `abs(Bank_Cash_Impact - GL_Amount_Total) > 0.01` | Amount mismatch |
| Otherwise | Matched |

The current tolerance is 0.01 in local currency. It is a case-study control assumption and would require business approval in a real implementation.

## Sign convention

Receipts are positive and payments are negative. Variance is calculated as:

```text
Bank cash impact - aggregated GL cash impact
```

Closing cash is calculated independently from opening balance plus bank statement movement. Reconciliation exceptions are not netted into the reported cash position.

## Rerun controls

A rerun should record the source file names, capture date, row counts, rejected rows, duplicate keys, status totals and final control totals. The current validator provides the source-derived checks; it does not provide production workflow approvals.
