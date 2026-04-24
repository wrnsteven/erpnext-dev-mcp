**问题：** 我们在 Sales Order 中跟踪客户的采购订单号（PO Number）和采购订单日期（PO Date）字段。为了让这些值也能被获取到 Sales Invoice 中，我们在 Sales Invoice 中插入了自定义字段（Custom Field）。然而，当从 Sales Order 创建 Sales Invoice 时，客户的采购订单信息没有被获取。

**回答：** 当数据从一个单据获取到另一个单据时，数据的映射是基于字段名称进行的。如果两个单据中的字段名称完全相同，那么它们的值就会被映射。

例如，如果您希望将客户的采购订单号和采购订单日期从 Sales Order 获取到 Sales Invoice，那么您应该确保在 Sales Invoice 中添加的自定义字段与 Sales Order 中的字段名称完全一致。

**Sales Order（标准字段）**

![图片](../../images/227_customize-fetch-data-1.png)

**Sales Invoice（自定义字段）**

![图片](../../images/227_customize-fetch-data-2.png)

由于 Sales Order 和 Sales Invoice 中客户采购订单相关字段的名称相同，当从 Sales Order 创建 Sales Invoice 时，这些字段的值会自动获取。

![图片](../../images/227_customize-fetch-data-3.png)
![图片](../../images/227_customize-fetching-data.gif)

---
original_url: https://docs.frappe.io/erpnext/fetching-data-from-a-document
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---