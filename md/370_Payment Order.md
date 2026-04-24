**付款订单是一份内部文档，用于记录针对供应商的批量付款。**

在大中型企业中，付款给供应商的决策通常由采购经理等人员做出，而实际的付款操作则由会计人员（账户用户）执行。

付款订单是采购经理与会计之间的沟通桥梁，通知会计人员执行付款操作。

在 ERPNext 中，通过付款订单，您可以获取针对某个供应商的多个付款请求。

## 1. 前置条件

在创建和使用付款订单之前，建议先创建以下内容：

- [采购订单](/erpnext/purchase-order)

或

- [采购发票](/erpnext/purchase-invoice)

## 2. 如何创建付款订单

- 进入付款订单列表，点击"新建"。

- 选择公司银行账户。

点击 **获取自** 按钮，选择付款请求。如有需要可应用筛选条件，然后选择付款请求。
![图片](../../images/370_payment-order-fetch.png)

付款请求将被获取到付款订单中。
![图片](../../images/370_payment-order.png)

保存并提交付款订单后，您将看到一个用于批量创建付款条目的按钮。
![图片](../../images/370_payment-order-submit.png)

---
original_url: https://docs.frappe.io/erpnext/payment-order
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---