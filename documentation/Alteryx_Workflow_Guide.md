# Alteryx Workflow Guide — Bank-to-GL Reconciliation

## Objective

Recreate the workbook's bank-to-GL reconciliation in Alteryx Designer using the synthetic CSVs. The objective is to demonstrate data preparation, summarization, matching, duplicate identification and exception outputs.

## Input files

- `data/bank_transactions.csv`
- `data/gl_transactions.csv`

Use full paths when selecting files in Input Data. Keep both files in the same extracted project folder.

## Workflow layout

```text
Bank_Transactions.csv ------------------------------                                                      Join (L / J / R)
GL_Transactions.csv -> Summarize GL -----------------/
                                     |
                                     +-- J -> Formula (variance/status) --                                     |                                    Union -> Output bank_side_reconciliation.csv
                                     +-- L -> Formula (Missing in GL) ----/
                                     |
                                     +-- R -> Formula (GL-only) -> Output gl_only_review.csv
```

## Build steps

### 1. Add two Input Data tools

- Drag an Input Data tool to the canvas and select `bank_transactions.csv`.
- Add a second Input Data tool and select `gl_transactions.csv`.
- Run once to confirm 20 bank rows and 21 GL rows are read.
- Confirm the matching key fields are strings: Bank_Ref/GL_Ref, Account_ID and Currency.
- Confirm Cash_Impact_Local and GL_Cash_Impact_Local are numeric.

### 2. Summarize the GL stream

Connect the GL Input Data tool to Summarize.

In Summarize configuration:
- `GL_Ref` → Group By
- `Account_ID` → Group By
- `Currency` → Group By
- `GL_Cash_Impact_Local` → Sum; rename output `GL_Amount_Total`
- `GL_Ref` → Count; rename output `GL_Tx_Count`

The purpose is to aggregate duplicate GL references into one row while preserving their count. BT014 should have `GL_Tx_Count = 2` and `GL_Amount_Total = -240000`.

### 3. Join bank transactions to summarized GL

Connect:
- Bank transaction stream to the Join tool's L (left) input.
- Summarized GL stream to the Join tool's R (right) input.

Configure three join keys:
- Left `Bank_Ref` = Right `GL_Ref`
- Left `Account_ID` = Right `Account_ID`
- Left `Currency` = Right `Currency`

Use string fields on both sides. Alteryx Join supports joining on one or more common fields; field types must be compatible. See the official Join documentation: https://help.alteryx.com/current/en/designer/tools/join/join-tool.html

### 4. Configure the J output (references found on both sides)

Connect the Join tool's J output to a Formula tool.

Create `Variance_Local` as a Double:
```text
[Cash_Impact_Local] - [GL_Amount_Total]
```

Create `Reconciliation_Status` as a V_String:
```text
IF [GL_Tx_Count] > 1 THEN "Duplicate in GL"
ELSEIF Abs([Variance_Local]) > 0.01 THEN "Amount mismatch"
ELSE "Matched"
ENDIF
```

Expected J output:
- 17 Matched rows
- BT003: Amount mismatch, variance -500
- BT014: Duplicate in GL, GL count 2, aggregated GL amount -240000, variance +120000

### 5. Configure the L output (bank references not found in GL)

Connect the Join tool's L output to another Formula tool.

Add:
- `GL_Amount_Total` (Double) = `0`
- `GL_Tx_Count` (Int32) = `0`
- `Variance_Local` (Double) = `[Cash_Impact_Local]`
- `Reconciliation_Status` (V_String) = `"Missing in GL"`

Expected L output:
- 1 row: BT004, variance -850, status Missing in GL.

### 6. Union the J and L results

Connect both Formula outputs to a Union tool.
- Choose Auto Config by Name (or the equivalent by-name option in your version).
- Check that one combined bank-side output has 20 rows.
- Output to `outputs/bank_side_reconciliation.csv`.

If field types differ between J and L, use Select tools before Union to align names and data types.

### 7. Configure the R output (GL references not found in bank data)

Connect the Join tool's R output to a Formula tool.
Add `Review_Status` (V_String):
```text
"GL-only: investigate"
```
Output to `outputs/gl_only_review.csv`.

Expected R output:
- 1 row: GL999, amount -42,000 USD.

### 8. Add a status summary (optional if time permits)

From the Union output, connect a Summarize tool:
- `Reconciliation_Status` → Group By
- `Bank_Ref` → Count
- Output a status-count CSV.

## Acceptance checks

| Check | Expected |
|---|---:|
| Bank input rows | 20 |
| GL input rows | 21 |
| J rows | 19 |
| L rows | 1 |
| R rows | 1 |
| Union bank-side rows | 20 |
| Matched | 17 |
| Missing in GL | 1 |
| Amount mismatch | 1 |
| Duplicate in GL | 1 |
| GL-only | 1 |

If counts differ, inspect the Join keys and data types first. Do not deduplicate BT014 before the Summarize step; its duplicate is a deliberate test condition.
