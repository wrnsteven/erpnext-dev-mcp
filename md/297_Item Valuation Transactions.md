在 ERPNext 中，物料的库存估值会在创建以下单据时进行更新。

- Purchase Receipt

- Stock Entry 类型为 Material Receipt 的单据

- Stock Reconciliation（用于更新库存期初余额）

您可以根据估值方法来选择物料价值的计算方式。估值方法可以在 Stock Settings 中为所有物料设置全局默认值。

![图片](../images/297_item-valuation-1.png)

您也可以在 Item 主数据中单独设置估值方法，特别是当某个物料的估值方法与默认方法不同时，如下图所示。

![图片](../images/297_item-valuation-2.png)

请注意，一旦物料生成了账本条目，此选项将在 Item 表单中不再显示。

[点击此处了解 ERPNext 中可用的估值方法及其工作原理。](https://frappe.io/blog/erpnext-features/inventory-valuation-method-fifo-vs-moving-average)

### v16 新增功能

在 ERPNext v16 中，用户现在可以按公司级别选择估值方法，Company DocType 中新增了一个相应字段。Stock Settings 单 DocType 中的旧字段仍然保留，仅在某些引用文档不涉及任何公司的情况下使用（如 Batch）。估值方法将按以下顺序获取：

- `Item` 级别

- `Company` 级别

- `Manufacturing Settings`（全局）级别

请按照上述所有级别相应设置估值方法，以防止库存估值错误。

---
original_url: https://docs.frappe.io/erpnext/item-valuation-transactions
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---