# Sales Invoice without an Item

A Sales Invoice is a bill that you send to your Customers against which the Customer makes the payment.

有些情况下，用户需要创建没有物料编码的销售发票（例如杂项费用、一次性项目）。在 ERPNext 中有办法处理这类情况。

## **1. 先决条件**

在创建和使用 Sales Invoice 之前，建议先创建以下内容：

- [Item](https://docs.erpnext.com/docs/v13/user/manual/en/stock/item)

- [Customer](https://docs.erpnext.com/docs/v13/user/manual/en/CRM/customer)

可选：

- [Sales Order](https://docs.erpnext.com/docs/v13/user/manual/en/selling/sales-order)

- [Delivery Note](https://docs.erpnext.com/docs/v13/user/manual/en/stock/delivery-note)

## **2. 如何创建没有物料编码的 Sales Invoice**

- 进入 Sales Invoice 列表，点击新建。

- 选择 Customer。

- 设置付款到期日。

- 在明细表中，点击第一行的编辑，填写：

- Item Name

- Description

- Quantity

- UOM

- Rate

- Income Account

![图片](../../images/489_ezgif.com-crop (7).gif)

- 保存并提交。

同样，您也可以使用此方法创建没有物料的 Credit Note。额外步骤是启用"Is Return"并输入负数数量。

有关 [Sales Invoices](https://docs.erpnext.com/docs/user/manual/en/sales-invoice) 的所有其他功能保持不变。

---

original_url: https://docs.frappe.io/erpnext/sales-invoice-without-an-item
translated_by: AI (Claude Code)
translation_date: 2026-04-18