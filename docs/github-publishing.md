# GitHub publishing checklist

## Recommended repository

`techgiant-global-treasury-cash-visibility`

Use the `TechGiant_Global_Treasury_Case_Study` folder as the repository root so the GitHub landing page opens directly on the portfolio README.

## Before publishing

1. Run `python scripts/validate_project.py`.
2. Open the Excel workbook and confirm the control-test sheet is still passing.
3. Add screenshots to `evidence/` only for Alteryx/Tableau work you personally completed.
4. Review the repository for credentials, tokens, private connection strings, or real personal/company data.
5. Keep the synthetic-data and “not a live Kyriba implementation” statements in the README.

## Upload with Git

From inside `TechGiant_Global_Treasury_Case_Study`:

```bash
git init
git add .
git commit -m "Add TechGiant treasury cash visibility case study"
git branch -M main
git remote add origin https://github.com/<your-username>/techgiant-global-treasury-cash-visibility.git
git push -u origin main
```

Create the empty GitHub repository first, then replace `<your-username>` with your account name. Do not initialize the new repository with another README, license, or `.gitignore`, because this folder already contains them.

## Suggested GitHub description

> Independent synthetic treasury case study demonstrating global cash visibility, bank-to-GL reconciliation, liquidity forecasting, exception controls, and TMS implementation thinking using Excel, Alteryx, Tableau, and Kyriba API research.

## Suggested topics

`treasury-management` `cash-visibility` `bank-reconciliation` `liquidity-forecasting` `finance-transformation` `alteryx` `tableau` `excel` `kyriba` `tms-implementation`
