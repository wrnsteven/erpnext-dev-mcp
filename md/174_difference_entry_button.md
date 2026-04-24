---
original_url: https://docs.frappe.io/erpnext/difference-entry
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# Difference Entry

As per accounting standards, debit in a accounting entry must be equal to credit. If not, system does allow submission of accounting transaction, thereby stops ledger posting. In ERPNext, on saving accounting entry, system validates if debit and credit is tallying.

![](/files/journal-entry-message.png)

To have entry balanced, you should one more row, select another account, and update different amount in it. Or you can add difference amount in one of the Account's row itself.

On clicking 'Make Difference Entry' button, new Row will be added under Journal Entry Accounts table, with difference amount. You can edit that row to select appropriate Account.

![](/files/difference-entry.gif)

On selecting account under new row, debit and credit an entry will be tallying, and you should be able to submit Journal Entri correctly.
