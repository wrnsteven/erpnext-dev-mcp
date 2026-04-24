ERPNext中有三种类型的报表。

### 1. Report Builder

Report Builder 是 ERPNext 内置的报表自定义工具。它允许您定义表单中需要添加到报表中的特定字段，还可以设置所需的筛选条件、排序方式，并为报表指定首选名称。

<iframe allowfullscreen="" frameborder="0" src="https://www.youtube.com/embed/TxJGUNarcQs?rel=0">
</iframe>

### 2. Query Report

Query Report 使用 SQL 编写，从账户数据库中提取数值并显示在报表中。虽然 SQL 查询可以从前端编写，如 HTML 一样，但由于它允许没有特定报表访问权限的用户直接从数据库获取数据，因此对 ERPNext 云用户有所限制。

请查看库存模块中的"采购订单物料待收货"报表作为 Query Report 的示例。点击[此处](https://frappeframework.com/docs/user/en/desk/reports/query-report)了解如何创建 Query Report。

### 3. Script Report

Script Report 使用 Python 编写，存储在服务器端。这些是涉及逻辑和计算的复杂报表。由于这些报表是在服务器端编写的，因此无法从托管账户进行自定义。

请查看账户模块中的"财务分析"报表作为 Script Report 的示例。点击[此处](https://frappeframework.com/docs/user/en/desk/reports/script-report)了解如何创建 Script Report。

> 注意：**动态筛选器**功能在 Script Report 和 Query Report 中可用，但在 Report Builder 中不可用。

---
original_url: https://docs.frappe.io/erpnext/making-custom-reports
translated_by: AI (Claude Code)
translation_date: 2026-04-18