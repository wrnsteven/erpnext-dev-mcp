---
original_url: https://docs.frappe.io/erpnext/bom_costing_in_different_currency
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 不同货币的 BOM 成本核算

用户可以在提交之前更改 BOM 中的货币。系统根据价格列表货币计算成本。你可以通过在 BOM 中更改货币来检查特定货币的制造成本。

假设你从日本进口塑料作为原材料，销售发票使用日元。你的公司货币是印度卢比，但你希望以日元进行 BOM 成本核算。当将"原材料单价依据"设置为"价格列表"时，BOM 中使用的原材料也将以日元设置单价。这些单价从你为日本创建的价格列表中获取。在这种情况下，它是一个名为"日本进口"的采购价格列表。

![](/files/bom-currency.png)

如果你将"原材料单价依据"设置为"评估单价"或"最近采购单价"，价格将分别从产品主数据或销售发票中获取。在产品主数据的情况下，你需要以**你的**货币输入评估单价。在 BOM 中，评估单价将转换为 BOM 中设置的货币。

![](/files/bom-currency-1.png)
