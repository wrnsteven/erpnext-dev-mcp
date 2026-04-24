**付款请求用于向客户请求支付销售订单或发票款项。**

付款请求通过电子邮件发送，如果已设置支付网关，将包含相应的支付链接。您可以通过销售订单或销售发票创建付款请求。付款请求也可以针对采购订单或采购发票创建，用于内部记录。随后，可以使用[付款订单](/erpnext/payment-order)进行批量处理付款。

访问付款请求，请前往：

> 首页 > 会计 > 应收账款 > 付款请求

## 1 前置条件

在创建和使用付款请求之前，建议先创建以下单据：

- [销售发票](/erpnext/sales-invoice)
- [采购发票](/erpnext/purchase-invoice)
- [销售订单](/erpnext/sales-order)
- [采购订单](/erpnext/purchase-order)

## 2 如何创建付款请求

付款请求无法手动创建，只能通过销售/采购订单或发票创建。

### 2.1 通过销售订单创建付款请求

在销售订单中，点击"创建"然后点击"付款"以进行预付款。关于预付款的更多信息，请访问[预付款录入](/erpnext/advance-payment-entry)页面。

![图片](../../images/372_payment-request-from-sales-order.png)

### 2.2 通过销售发票创建付款请求

在销售发票中，点击"创建"然后点击"付款"以支付发票款项。

![图片](../../images/372_payment-request-from-sales-invoice.png)

在付款请求中选择适当的付款网关账户用于过账。付款网关设置的科目将用于创建日记账分录。

> 注意：发票/订单的货币与"付款网关账户"的货币应保持一致。

![图片](../../images/372_payment-request-details.png)

### 2.3 通知客户

您可以使用[打印格式](/erpnext/print-format)通过付款请求通知客户。如果设置了客户联系邮箱，系统将自动获取。如未设置，您可以在付款请求中设置邮箱地址。

![图片](../../images/372_payment-request-recipient-details.png)

### 2.4 请求邮件

以下是一个请求邮件示例。如果您已设置相应的支付集成，系统将自动生成链接。如需了解更多集成信息，[请访问此页面](/erpnext/erpnext_integration)。

![图片](../../images/372_pr-email.png)

### 2.5 不使用任何支付网关的付款请求

如果您不想使用任何集成或支付网关，仅需发送通知，只需设置银行账户即可。您需要自行编写包含银行明细的邮件内容。然后相关方可以将款项汇入指定的银行账户。

---
original_url: https://docs.frappe.io/erpnext/payment-request
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---