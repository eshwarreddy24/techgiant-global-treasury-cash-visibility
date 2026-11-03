# Kyriba Developer Portal Research Log

## Purpose

Use the user's authorised Developer Portal access to understand how a treasury platform may expose cash, bank transaction, payment and integration data. This is research and documentation, not proof of a live integration.

Official portal overview: https://www.kyriba.com/resources/fact-sheets/kyriba-marketplace/  
Developer Portal: https://developer.kyriba.com/

Kyriba describes the Developer Portal as a hub for client/developer access to an API catalogue, Swagger API documentation, Postman samples, changelogs, use cases and support resources.

## What to capture

For each API area, record only details visibly shown in your own portal account:
- Exact API/product/resource title
- Version
- HTTP method and path, if displayed
- Purpose
- Important request parameters
- Important response fields
- Required authentication method (describe it; never paste keys/tokens)
- Whether a sandbox or execution environment is available
- Date reviewed
- Screenshot filename with sensitive data hidden

## Research areas

### 1. Cash balances / positions
Search terms: cash balance, bank account, account balance, cash position.
Business question: How might treasury retrieve account-level cash information for a consolidated cash position?
Fields to look for if present: account identifier, currency, balance amount, balance type, as-of/value date, bank or entity identifier.

### 2. Bank transactions / statements
Search terms: bank transaction, statement, transaction details, bank reporting.
Business question: How might bank movements be made available for reconciliation?
Fields to look for if present: transaction reference, account, currency, value date, amount, debit/credit indicator, bank status, counterparty.

### 3. Payments
Search terms: payment, payment status, payment instruction.
Business question: How might a treasury team monitor a payment lifecycle?
Fields to look for if present: payment ID, amount, currency, beneficiary reference, status and timestamps.

### 4. ERP integration
Search terms: integration, ERP, connector, data exchange, API.
Business question: What source-to-target mappings may be needed between ERP financial records and treasury data?

### 5. Authentication, errors and limits
Review the actual portal documentation for supported authentication, scopes, response codes, pagination and rate limits. Do not guess. Do not store credentials in project files.

## Evidence standard

- If you only read API documentation: write “API documentation reviewed; no API execution performed.”
- If you use a sanctioned sandbox: document the exact test performed and use sanitized request/response examples.
- If the portal has no accessible sandbox: record “Documentation-only access; sandbox/API execution not available in my current access.”
- Never claim live bank connectivity, production payments, or live Kyriba implementation.

## Proposed architecture (design only)

ERP / bank data source → data preparation and validation (Alteryx) → treasury platform (Kyriba, proposed) → treasury reporting (Tableau).

This is an illustrative architecture. The project does not connect these systems.
