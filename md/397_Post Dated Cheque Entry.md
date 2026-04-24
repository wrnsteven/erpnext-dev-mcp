期票是一种注明未来日期的支票。当事方通常提供期票作为预付款。这张支票只有在支票日期到来时才会被兑现。

在 ERPNext 中，为期票创建 Payment Entry。

#### 新建 Payment Entry

要打开新的付款凭证，请前往：

> `Accounting > Payment Entry > New`

#### 设置过账日期

假设您的支票日期是 2016 年 12 月 31 日（或任何未来日期）。因此，您银行账本中的这笔过账将显示在更新后的过账日期上。

![图片](../../images/397_Screenshot_2024-07-30_at_1_12.33.43_PM.png)

注意：Payment Entry 参考日期应等于或小于过账日期。

#### 保存并提交

输入所需信息后，保存并提交该 Payment Entry。

#### 调整期票凭证

您可以通过 [Payment Reconciliation Tool](/erpnext/payment-reconciliation) 将期票 Payment Entry 与发票进行核销。

当支票兑现时，即在支票的实际日期，您可以通过 [Bank Reconciliation Tool](/erpnext/bank-reconciliation) 更新其兑现日期。

在科目表中，您可能会发现该 Payment Entry 的值已反映在银行账户中。您应查看账户模块中的 **Bank Reconciliation Statement**（银行对账单），这是一份用于了解系统银行余额与银行对账单实际余额之间差异的报告。

---
original_url: https://docs.frappe.io/erpnext/post-dated-cheque-entry
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---