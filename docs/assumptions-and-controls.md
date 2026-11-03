# Assumptions and controls

## Assumptions

- TechGiant Inc., banks, accounts, counterparties, transactions, FX rates, and balances are fictional.
- FX rates are illustrative USD-per-local-currency training assumptions, not market quotes.
- Closing cash equals opening balance plus bank-statement movement.
- Closing cash is not adjusted for unresolved reconciliation exceptions.
- Forecast inflows and outflows are editable scenarios, not historical forecast accuracy evidence.

## Controls

- Bank-to-GL matching uses reference, account, and currency.
- Duplicate GL references are flagged before any amount is accepted as reconciled.
- Missing bank-side postings and GL-only postings are reported separately.
- Amount mismatch uses a USD/local-currency variance tolerance of `0.01`.
- Account and currency references must exist in the master data.
- The validator compares source-derived results with the expected and Tableau-ready CSV outputs.
- No live credentials, bank files, client data, or production integrations are included.
