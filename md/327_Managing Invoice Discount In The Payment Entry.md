**问题**：有时客户不会全额支付发票，他希望我们给他折扣。例如，发票总额是 54 欧元，但他只支付 50 欧元，将 4 欧元作为折扣。在这种情况下，如何在系统中进行登记，以便发票显示为已付款，同时我们能够知道该发票存在折扣？

**回答**：

在 Payment Entry 中，按如下方式输入数值：

- **Paid Amount（已付金额）** 填写 50 EUR

- **Against the Invoice（关联发票）** 分配 54 EUR

- 这将产生 **Difference Amount（差额金额）** 4 EUR

- 在 **Deductions and Additional Charges（扣减和附加费用）** 表中，选择 Income account（收入账户）或 Discount Expense Account（折扣费用账户）（根据您的偏好），将 4 EUR 记入该账户

![图片](../../images/327_El01OoO.gif)

---
original_url: https://docs.frappe.io/erpnext/managing-invoice-discount-in-the-payment-entry
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---