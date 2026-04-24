---
original_url: https://docs.frappe.io/erpnext/accounting-period
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 会计期间

**会计期间定义了一个时间段，在该时间段内记录财务报表。**

在 ERPNext 中，会计期间是一个时间范围，超出该时间范围将不允许创建选定的可提交交易（如销售/采购发票、库存过账、工资单过账、日记账分录等）。换句话说，选定的交易只允许在定义的会计期间内创建。

**为什么需要会计期间？**

当交易被提交时，它们会影响分类账和处理分类账数据的报告。这可能在为当局审计或结算财年的会计账簿而需要生成财务报告时造成问题。

这里会计期间可用于限制提交交易的时间段，以保持相应报告的完整性。

1. 如何创建会计期间

---

### 1.1 "关闭"选项用于所选交易的用途是什么？

![Accounting Period Child Table](images/11_accounting-period-closed.png)

交易 DocTypes 子表中的"关闭"选项用于选择会计期间结束后要限制的交易。

请注意，如果会计期间结束，并且子表中选定的任何交易未勾选"关闭"，则它们在会计期间结束后不会被限制。

1. 输入会计期间的名称。
2. 通过设置开始和结束日期来定义时间范围。
3. 从表中添加或删除交易。请注意，表中所有勾选了"关闭"选项的交易将在会计期间结束后被限制。
4. 保存并提交。![Accounting Period](images/11_accounting-period.png)

如果你尝试在会计期间结束后保存已关闭的交易，你将看到一条验证错误，防止你这样做。![Accounting Period](images/11_accounting-period-closed-for-transaction.png)

> 注意：没有任何角色可以保存或提交会计期间中定义的交易，即使是在[账户设置](/erpnext/accounts-settings)中设置的"允许设置冻结账户和编辑冻结条目的角色"。

2. 相关主题

---

- [会计期间如何用于关闭会计账簿](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
- [期间结束凭证](/erpnext/period-closing-voucher)
