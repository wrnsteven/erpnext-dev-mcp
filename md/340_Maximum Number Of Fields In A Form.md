有时在创建自定义字段时，可能会遇到如下错误信息：

> Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs.

### 这是什么意思？

简单来说，这意味着您已达到了特定表单/DocType 的最大字段数限制。那么，最大字段数限制是多少呢？

在 MySQL 中，每个表有 4096 列的硬性限制，但给定表的实际最大列数可能更少。确切的限制取决于多个相互作用的因素。

每个表（无论使用何种存储引擎）的最大行大小为 65,535 字节。存储引擎可能会对此限制施加额外的约束，从而减少实际的最大行大小。

最大行大小限制约束了列的数量（以及可能的列大小），因为所有列的总长度不能超过此大小（65,535 字节）。例如，`utf8mb3` 字符每个字符最多需要 3 个字节，因此对于 `VARCHAR(140)` 列，服务器必须为每个值分配 `140 × 3 = 420` 字节。因此，一个表不能包含超过 `65,535 / 420 = 156` 个这样的列。

在 Frappe 框架中，会根据 "Data"、"Link"、"Select"、"Dynamic Link"、"Password" 和 "Read Only" 字段类型创建 `VARCHAR(140)` 类型的列。因此，您可以在系统中创建大约 156 个这样的列。

### 解决方案：

您可以进行一些更改来向系统添加更多字段。

- 将某些字段转换为 "Text"、"Small Text"、"Text Editor" 或 "Code" 类型字段。在 MySQL 中，BLOB 和 TEXT 列对行大小限制的贡献从 1 到 4 加上 8 个字节不等，因为它们的内容与行的其余部分分开存储。因此，转换为这些字段类型将释放一些空间，并允许添加更多字段。

- 在创建字段时将 "Length" 属性设置为较小的值，默认值为 140。系统根据此属性设置 `VARCHAR` 的长度并为这些列分配大小。因此，较小的长度可以添加更多字段。

- 自定义字段不会自动从数据库中删除。如果您确定不需要任何自定义字段的数据，可以使用 trim-tables 命令精简表：<https://frappeframework.com/docs/user/en/bench/reference/trim-tables>

---
original_url: https://docs.frappe.io/erpnext/maximum-number-of-fields-in-a-form
translated_by: AI (Claude Code)
translation_date: 2026-04-18