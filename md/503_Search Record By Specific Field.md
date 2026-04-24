在创建任何 DocType 时，您可能希望将某个字段链接到另一个 DocType。例如，在 Sales Order DocType 中，'Customer' 字段允许您选择现有的客户。这类字段被称为[链接字段](/erpnext/field-types#link)。

使用链接字段，您可以创建

假设您希望在 Sales Order 中查看 Item 及其 Item Group。具体步骤如下：

#### 第 1 步：进入自定义表单

> 首页 > 自定义化 > 表单自定义化 > 自定义表单

#### 第 2 步：选择需要在搜索字段中显示多个字段的文档

这里我们选择 Item 文档。

#### 第 3 步：搜索字段

在"Search By"字段中更新 Warehouse 字段名称。

![图片](../../images/503_customize-search-record-1.png)
![图片](../../images/503_customize-search-record-2.png)

更新这些设置后，在创建 Sales Order 时，选择 Item 时，您也将能够看到该仓库。

![图片](../../images/503_customize-search-record-3.png)

---
original_url: https://docs.frappe.io/erpnext/search-record-by-specific-field
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---