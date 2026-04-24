---
original_url: "https://docs.frappe.io/erpnext/adjusting-withhold-amount"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 调整预扣金额

假设一张 Sales Invoice 的应付金额为 20,000。当客户付款时，他们只支付 19,600。剩余的 400 需要计入预扣税账户。您可以按以下方式处理此场景。

## 步骤 1：设置预扣账户

在您的科目表中<a href="/erpnext/chart-of-accounts#1-how-to-createedit-accounts">创建一个预扣账户</a>。

## 步骤 2：付款条目

要创建 Payment Entry，请转到未付款的 Sales Invoice，然后点击"Make Payment"按钮。

### 步骤 2.1：输入付款金额

输入付款金额为 19,600。

<img src="/images/27_paid-amount-in-payment-entry.png" alt="Paid Amount in Payment Entry" />

### 步骤 2.2：分配到 Sales Invoice

在 Sales Invoice 上，分配 20,000（如下图所示）。

### 步骤 2.3：添加扣除/损失账户

您会注意到付款金额与分配到 Sales Invoice 的金额之间存在 400 的差额。您可以将此差额账户计入预扣账户。

<img src="/images/27_tax-withheld-adjustment-in-payment-entry.gif" alt="Tax Withheld Adjustment in Payment Entry" />

按照相同的步骤，您还可以处理因货币汇率变动而产生的差额。
