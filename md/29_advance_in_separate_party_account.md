---
original_url: "https://docs.frappe.io/erpnext/advance-in-separate-party-account"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 独立往来账户中的预付款

从版本 15 开始，ERPNext 支持将客户预付款计入负债，将供应商预付款计入资产。<strong>这些只能通过 Payment Entry 实现</strong>。

## 注意：预付款账户仅限于公司货币

1. 先决条件

<hr />

要使用此功能，需要先创建以下内容：

- 在负债下创建"应收"类型账户用于客户，在资产下创建"应付"类型账户用于供应商
- 在 <strong>Company -> Accounts -> Advance Payments</strong> 部分维护上述账户

2. 如何在负债/资产下创建预付款

<hr />

提交 Sales Order 或 Purchase Order 后，您将找到创建付款的选项。您也可以创建新的 Payment Entry 并手动选择值（如 Party 和付款账户）。以下是针对 Sales Order 创建预付款的步骤。

- 转到 Sales Order 并点击 <strong>Make > Payment Entry</strong>。
- 设置所需详情并保存
  1. 保存后，系统将使用公司主数据中维护的预付款账户更新"Paid To"/"Paid From"账户。
- 提交

3. 分配预付款到发票

<hr />

分配方式与普通预付款类似。请参阅<a href="https://docs.erpnext.com/docs/user/manual/en/advance-payment-entry#2-2-allocating-advance-payment-in-invoice">预付款分配</a>

### 局限性

目前，这种类型的预付款仅支持客户和供应商两种往来方类型。

### 相关内容

1. <a href="https://docs.erpnext.com/docs/user/manual/en/advance-payment-entry">Normal Advance Payment</a>
