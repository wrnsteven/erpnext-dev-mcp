---
original_url: https://docs.frappe.io/erpnext/change-valuation-method
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# Change Valuation Method

In ERPNext, users can change the valuation method from FIFO to Moving Average, but not from Moving Average to FIFO, for items with existing stock transactions.

If a user changes the valuation method from FIFO to Moving Average for any item, the system will use the Moving Average method for new outward transactions. Additionally, if the user creates backdated transactions, all transactions created after that backdated entry will be reposted using the Moving Average method. This may result in changes to the closing balance value of earlier transactions.

To prevent this, users can freeze stock transactions before a specific date by setting the "Stock Frozen Up To" date in the stock settings.

![](/files/Screenshot%202025-04-29%20at%204.38.39%20PM.png)
