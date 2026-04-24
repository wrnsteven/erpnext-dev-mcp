对于每个物料，您分配的编码可能与供应商对该物料给出的编码不同。ERPNext 允许您在物料主数据中跟踪 Supplier's Item Code。您还可以在采购交易中获取 Supplier's Item Code，以便供应商能够轻松识别与其 Item Code 相关的物料。

#### 1. 在物料中更新 Supplier Item Code

在物料主数据的"Supplier Details"部分，输入供应商为该物料分配的 Item Code。

![图片](../../images/317_supplier-item-code.png)

#### 2. 交易中的 Supplier's Item Code

每个采购交易的物料明细表中都有一个字段，用于获取 Supplier's Item Code。此字段在表单和 Standard print format 中都是隐藏的。您可以通过在 [Customize Form](/erpnext/customize-form.html) 中更改此字段的属性来使其可见。

进入打印视图，点击菜单 > customize，输入新的打印格式名称，找到 Items 表格，点击其中的 **Select columns** 按钮。您将看到以下界面。现在选中"Supplier Part Number"复选框。

![图片](../../images/317_supplier-item-code-print-format.png)

只有在采购交易中选定的供应商和 Item Code 都与物料主数据中记录的值相匹配时，Supplier Item Code 才会被获取到采购交易中。

![图片](../../images/317_supplier-item-code-in-purchase-order.png)

---
original_url: https://docs.frappe.io/erpnext/maintaining-suppliers-part-no-in-item
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---