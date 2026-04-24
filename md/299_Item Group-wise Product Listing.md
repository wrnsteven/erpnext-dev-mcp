# Item Group-wise Product Listing

与位于 `/all-products` 的[产品列表](/erpnext/product-listing)类似，ERPNext 也提供按物料组划分的产品列表。您可以将这些页面链接到您的落地页，以便轻松引导用户。

## 设置物料组页面

要为物料组（例如 Products）提供产品列表页面，请前往：

> 物料组列表 &gt; Products

- 启用**显示在网站**。

- 向下滚动到**网站筛选器**部分，添加类似于电商设置的字段和属性筛选器。

- 您还可以在富文本编辑器中添加描述，该描述将作为横幅显示在产品列表上方。

现在，如果您点击左上角当前文档图片上方的**在网站上查看**链接，将被重定向到 **Products** 物料组的列表页面。

### 产品可见性

假设物料组 **Products** 包含子物料组 **Mobile Services** 和 **Mobiles**。

将在 **Products** 页面上可见的网站物料包括：

- 将 **Products** 作为其物料组的物料

- 在其**网站物料组**表格中将 **Products** 作为物料组的物料

将其物料组设为 **Mobile Services** 或 **Mobiles** 的网站物料将在各自的页面上可见。这些页面将链接在 **Products** 页面上。

> 子物料组（如 **Mobile Services** 和 **Mobiles**）将在 **Products** 页面的搜索栏上方显示为标签页。

![图片](../../images/299_item-group-page.png)

---
original_url: https://docs.frappe.io/erpnext/item_group_wise_product_listing
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---