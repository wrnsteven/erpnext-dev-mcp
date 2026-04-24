### Payment Terms Status Report

Report to calculate status of Payment Terms based on the invoices created against that Sales Order. Invoice amount is split into the respective payment terms at runtime using FIFO method.
![图片](../../images/376_payment%20terms%20status.png)

##### Example:

Consider a Sales Order with total value of 7000₹ and a payment terms of 50-50.
![图片](../../images/376_Screenshot%202022-01-04%20at%206.33.53%20PM.png)

If a Sales Invoice is made against that SO for 4900₹.
![图片](../../images/376_payment%20terms%20invoice.png)

Then, the report will split the invoice amount into payment terms in FIFO method and display the statuses as 'Completed' for the first 50% and 'Partly Paid' for the second 50%.
![图片](../../images/376_Screenshot%202022-01-04%20at%206.27.56%20PM.png)

---
original_url: https://docs.frappe.io/erpnext/payment_terms_status_report
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---