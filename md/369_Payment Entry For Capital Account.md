```markdown
---
original_url: https://docs.frappe.io/erpnext/payment-entry-for-capital-account
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

**问题：**

如何创建一笔股东投资资本的 Payment Entry。金额应添加到公司的银行账户中。

**答案：**

您也可以为股东创建 Payment Entry。一旦您在 ERPNext 中添加了股东，您可以在 Payment Entry 中选择他们。

![图片](../../images/369_Etxow8j.png)

唯一需要与您的会计确认的是 Account Paid From。如果您从 Payment Entry 创建此条目（这是基于应计项目设计用于接收付款的），您将需要定义一个 Debtor 或 Creditor 账户，以便在 Account Paid From 字段中进行选择。

### 通过 Journal Entry 创建 Payment Entry

如果上述方法无法满足您的需求，您也可以通过 Journal Entry 来管理这种情况。简单的 Journal Entry 如下：

Cr. 股东账户 …………………… XXX
Dr. 银行账户 …………………… XXX

在 Journal Entry 中，您同样可以使用 Reference No. 和 Date 等字段来追踪客户的支票详细信息。
```