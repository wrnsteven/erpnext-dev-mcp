---
original_url: https://docs.frappe.io/erpnext/bank
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 银行

在 ERPNext 中，保存不同的银行可以让你上传 Excel 表格并将交易映射到分类账。交易被创建为银行交易。这些交易可以用于参考和报表。这通过 [Bank Reconciliation](erlnext/bank-reconciliation) 完成。

要访问银行，请前往：

> 首页 > 会计 > 银行对账单 > 银行

![银行](/files/bank.png)

## 1. 如何创建银行

创建银行很简单，前往银行列表，点击新建，然后输入名称。

## 1.1 为银行配置数据导入

1. 在"银行交易字段"下，选择要在"银行对账单交易条目"表单中更新的字段。
2. 在"银行文件中的列"下，输入从银行导出的 Excel 文件中的列。

设置完成后，[Bank Reconciliation](erpnext/bank-reconciliation) 可以顺利进行。

## 2. 相关主题

1. [Bank Account](erpnext/bank-account)
