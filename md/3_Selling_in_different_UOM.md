---
original_url: https://docs.frappe.io/erpnext/Selling-in-different-UOM
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 以不同单位销售

销售单价单位（UOM）是你为商品定价所使用的单位。你可以为任何库存商品设置多个销售单价单位。但是，当客户下单时，商品的单位可能会发生变化。

例如，商品 Pen 以个数（Nos）库存，但以盒（Box）销售。因此，我们将以盒为单位为 Pen 创建销售订单。

**步骤 1：**
在商品主数据中，在"单位"部分，你可以列出商品的所有可能单位及其单位转换系数。更新单位转换系数
如果一盒中有 10 支笔，则单位转换系数为 10。

![Item Unit of Measure](images/3_Item-UOM.png)

**步骤 2：**
在销售订单中，你会看到两个单位字段：

1. UoM
2. Stock UoM

在这两个字段中，商品的默认单位将默认被获取。你应该编辑 UoM 字段，并选择销售单位（本例中为 Box）。更新销售单位主要用于客户的参考。在打印格式中，你将以销售单位看到商品数量。

![Sale Order Unit of Measure](images/3_Sale-Order-UOM.png)

根据数量和转换系数，数量将根据商品的库存单位计算。如果你只销售一盒，那么按库存单位计算的数量将设置为 10。

**库存账本分录**

无论销售订单中选择了什么销售单位，库存账本分录都将以商品的默认单位进行。因此，在以不同单位销售商品时，应确保转换系数输入正确。

![UOM in Stock Ledger](images/3_uom-in-stock-ledger.png)
