---
original_url: https://docs.frappe.io/erpnext/discount-accounting
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# Discount Accounting

Discount Accounting is used to post additional ledger entries for discounts, under a separate Discount Account. This can be done for:

1. Discounts applied on individual Items
2. Additional Discounts applied on all the Items in an invoice

### Steps

1. Check the *Enable Discount Accounting* box in the *Accounts Settings* page.
![](/files/Enable%20Discount%20Accounting.png)

2. Create a Sales/Purchase Invoice as usual.

3. To post ledger entries for discounts applied on individual Items:

- Expand the row for that Item in the Items table
- Enter discount in the Discount and Margin section
- Scroll down to the Accounting Details section and enter the Discount Account
![](/files/Discount%20Account.png)

4. To post ledger entries for Additional Discounts applied on all the Items in an invoice:

- Go to the Additional Discount Section
- Enter the Additional Discount Amount/Percentage and the Additional Discount Account
![](/files/Additional%20Discount%20Account.png)

5. Save and submit the invoice to create ledger entries as shown below:

- *For Sales Invoices:*
![](/files/Discount%20Accounting%20for%20Sales%20Invoices.png)

- *For Purchase Invoices:*
![](/files/Discount%20Accounting%20for%20Purchase%20Invoices.png)

### Default Discount Account

Additionally, you could enter a Default Discount Account for an Item, which will be fetched automatically while creating the Invoice. The visibility for this field is also dependant on the Enable Discount Accounting checkbox in Accounts Settings.

1. Open the Item doc.

2. Go to the Item Defaults table in the *Sales, Purchase, Accounting Defaults* section.

3. Expand the row of your choice and enter the Default Discount Account for the Item
![](/files/Screenshot%202021-11-09%20at%208.46.41%20PM.png)