**Item Price 是用于记录商品销售价和采购价的凭证。**

新建 Item Price 表单有两种方式：

**销售/采购/库存 > 商品及定价 > Item Price > 新建**。

或者

**库存 > 商品 > 点击商品旁的 "+" > Item Price**。

2. 选择商品。系统将自动提取商品名称、计量单位和描述。
3. 选择 Price List，无论是销售价、采购价还是您自行创建的其他 Price List。
4. 在"单价"字段中输入实际价格。
5. 保存。
![图片](../../images/295_item-price.png)

### 1.1 选择 Price List

在 ERPNext 中，您可以为同一商品创建多个 Price List，分别追踪其销售价和采购价。此外，如果商品的销售价因地区或其他条件而异，您可以为其创建多个销售 Price List。

选择 Price List 后，系统会自动提取其货币以及适用类型（仅销售、仅采购或两者兼顾）。若希望在销售或采购交易中自动获取 Item Price，应在交易的"货币和 Price List"部分选择相应的"Price List"。

若要查看所有 Item Price，请前往：

**库存 > 库存报表 > Item Price Stock**

访问 [Price Lists](/erpnext/price-lists) 页面了解更多详情。

## 2. 功能特性

### 2.2 Unit of Measurement (UOM)

价格始终与特定 UOM 相关联。例如，$1 *每千克* 或 $80 *每小时*。默认情况下，**Item Price** 会获取商品的*默认计量单位*。您也可以将其更改为商品 UOM 表中的任意其他计量单位。

例如，如果大米以 1 千克和 500 克包装销售，您可以在 **Item Price** 中指定 UOM（"千克"或"克"），系统将根据交易中选择的 UOM 自动应用正确的价格。

### 2.3 Packing Unit

指每单位计量所需购买或销售的数量。例如，如果 Packing Unit 为 2，UOM 为 1，则交易数量为 2 件。默认值为 0；您可以使用非整数计量单位，如 1 个 Packing Unit 对应 1.5 千克燕麦。如果您将其保留为 0，则不会对任何交易产生影响。

### 2.4 Minimum quantity

指应用此价格并将其更新到 Item Price 列表所需的最小交易数量。

### 2.5 将 Price List 应用于特定客户/供应商

如果您选择销售 Price List，将出现一个客户字段，您可以在此为特定客户分配此 Item Price。同样，如果您选择采购 Price List，将出现一个供应商字段，您可以在此选择特定供应商。

### 2.6 将 Price List 应用于特定批次

您还可以将特定批次链接到 Item Price，在交易中选择该批次时，系统将应用该特定批次的商品价格。

### 2.7 Validity

此处有两个字段："生效日期"和"有效至"。生效日期默认为您创建 Item Price 的日期；您也可以设置有效至日期，届时 Item Price 将自动失效。

### 2.8 Lead Time in days

指产品到达仓库所需的大致天数。您可以根据同一产品从不同供应商处到达所需时间的不同，设置不同的 Item Price。

### 2.9 Note

您可以在此字段中添加关于 Item Price 的任何备注信息。

---
original_url: https://docs.frappe.io/erpnext/item-price
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---