# Process Deferred Accounting

Process Deferred Accounting 是一个日志，在每次处理递延收入或递延费用时创建。

Process Deferred Accounting 记录在记账递延收入或递延费用时自动创建。这是通过后台作业完成的，但用户也可以为手动递延收入或递延费用记账创建记录。

要访问 Process Deferred Accounting 列表，请转到：

> 首页 > 会计 > 总账 > Process Deferred Accounting

## 1. 前置条件

在创建和使用 Process Deferred Accounting 之前，建议先创建并了解以下内容：

- [Deferred Revenue](/erpnext/deferred-revenue)

- [Deferred Expense](/erpnext/deferred-expense)

## 2. 如何创建 Process Deferred Accounting

- 进入 Process Deferred Accounting 列表，点击"新建"。

- 输入公司。

- 选择递延会计处理类型。选择"收入"记账递延收入，或选择"费用"记账递延费用。

- 展开过账日期。

- 输入服务开始日期和结束日期。

- 保存并提交。

![图片](../../images/409_process-deferred-accounting.png)

## 3. 功能

### 3.1 提交时

提交 Process Deferred Accounting 文档时，将为服务开始日期和结束日期之间的所有发票创建递延收入或费用记账的 GL 条目。

如果只需为特定的递延收入或递延费用账户记账，请输入该账户。

### 3.2 启用自动递延会计

要启用自动递延会计，请在"会计设置"中启用"自动处理递延账户分录"复选框。

要访问会计设置，请转到：

> 首页 > 会计 > 会计主数据 > 会计设置

![图片](../../images/409_deferred-accounting-settings.png)

---

original_url: https://docs.frappe.io/erpnext/process-deferred-accounting
translated_by: AI (Claude Code)
translation_date: 2026-04-18