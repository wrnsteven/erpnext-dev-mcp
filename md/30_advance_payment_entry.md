---
original_url: "https://docs.frappe.io/erpnext/advance-payment-entry"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 预付款

<strong>在发票发出之前由客户/供应商支付的款项称为预付款。</strong>

通常，预付款用于高价值交易。考虑这样一个案例：客户 Jane D'souza 下单购买一件价值 24,000 的豪华家具，被要求在家具商开始生产她的订单之前支付一些预付款。她支付了 10,000 现金。

在 ERPNext 中，预付款条目使用 Payment Entry 创建。如果存在 Sales Order，您可以直接针对预付款金额创建 Payment Entry。否则，您也可以为客户创建单独的 Payment Entry。同样的方式，您也可以通过 Purchase Order 为供应商创建预付款 Payment Entry。

<img src="/images/30_payment-option-in-sales-order.png" alt="Payment Entry From Sales Order" />

> 注意：如果付款未链接到发票，则被视为预付款。预付款会反映在应收账款和应付账款报告中。

1. 先决条件

<hr />

要创建预付款条目，需要先创建以下内容：

- Party（客户/供应商）
- 付款账户（银行或现金账户）

2. 如何创建预付款条目

<hr />

提交 Sales Order 或 Purchase Order 后，您将找到针对其创建 Payment 的选项。您也可以创建新的 Payment Entry 并手动选择值（如 Party 和付款账户）。以下是针对 Sales Order 创建预付款的步骤。

1. 转到 Sales Order 并点击 <strong>Make > Payment Entry</strong>。
2. 设置/检查账户。
3. 保存并提交。

任何未链接到发票的 Payment Entry 都会被 ERPNext 系统视为预付款。

如果客户支付了 5,000 美元作为现金预付款，它将作为客户应收账款账户的贷方条目记录。根据复式记账系统，为平衡账目，5,000 美元会记入公司现金账户的借方。

### 2.2 在发票中分配预付款

创建发票时，您可以检查该 Party 是否有预付款。

<img src="/images/30_fetch-advance-payments-in-invoice.png" alt="Fetch Advance Payments in Sales Invoice" />

点击 <strong>Get Advance Received</strong> 按钮后，系统会获取该 Party 的预付款条目。获取预付款条目后，您可以将预付款金额分配到此发票。分配将立即减少该发票的应付金额。

保存并提交 Sales Invoice。

### 3. 相关主题

1. <a href="/erpnext/sales-invoice">Sales Invoice</a>
2. <a href="/erpnext/journal-entry">Journal Entry</a>
3. <a href="/erpnext/payment-entry">Payment Entry</a>
4. <a href="https://docs.erpnext.com/docs/user/manual/en/advance-in-separate-party-account">Advance under Liability/Asset</a>
