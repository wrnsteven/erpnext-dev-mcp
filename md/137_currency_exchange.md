---
original_url: https://docs.frappe.io/erpnext/currency-exchange
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# Currency Exchange

The Currency Exchange form in ERPNext stores exchange rates manually stored by the User. By default, ERPNext automatically fetched the current exchange rates for currencies as per the market. However, you can store fixed exchange rates and use them. You need to enable 'Allow Stale Exchange Rates' in Accounts Settings for using the exchange rates stored in the Currency Exchange form.

To access the Currency Exchange list, go to:

> Home > Accounting > Multi Currency > Currency Exchange

1. How to create a Currency Exchange
---
2. Go to the Currency Exchange list and click on New.
3. Enter a date from which this exchange rate will be valid. New Currency Exchange forms saved with newer dates will be used in transactions.
4. Set the From and To currency.
5. Enter the Exchange Rate, for example, 1 USD = 83.51 INR.
6. Select whether the exchange rate applies to selling, buying, or both transactions.
7. Save.

![](/files/Screenshot%202024-06-24%20at%201.16.07%20PM.png)

2. Related Topics
---

1. [Exchange Rate Revaluation](/erpnext/exchange-rate-revaluation)
2. [Multi Currency Accounting](/erpnext/multi-currency-accounting)
