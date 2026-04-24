---
original_url: https://docs.frappe.io/erpnext/setting-workflows-on-masters
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

## 在主数据上设置工作流程

工作流程通常设置在可提交的单据上。一旦单据获得批准，它会根据设定的工作流程自动提交。然而，有时企业确实需要对主数据（如 Item、Item Price、Pricing Rule 等）进行审批。

在 ERPNext 中，这些主数据是不可提交的。因此，即使被拒绝，它们有时仍然处于激活状态，您仍可以在交易中使用它们。在本文中，我们以 Item master 为例，介绍如何设置简单的工作流程，使其仅在获得批准后才处于激活状态。请按照以下步骤操作：

- 确保您要设置工作流程的主数据包含启用/禁用复选框。如果默认没有此字段，您需要通过 Customize Form 创建一个，并按如下方式设置默认值：

  - 如果复选框为"禁用"，则值为 0

  - 如果复选框为"启用"，则值为 1

在我们的示例中，Item master 有一个名为"Disabled"的复选框。我们已在 Item DocType 的 Customize Form 中将默认值设置为 1，如下图所示。

![图片](../../images/529_ubLZfPq.png)

这意味着，每次创建新 Item 时，它默认处于禁用状态，除非获得批准（如下图所示）。

![图片](../../images/529_yPOQ2fT.png)

- 接下来，设置工作流程。

在 States 表格中，审批通过时，确保将"Disabled"（或 Enabled）复选框更新为 0（或启用时为 1），如下图所示。

![图片](../../images/529_Qf3QXyo.png)

这样可以确保，每当 Item 获得批准时，该 Item 将自动启用，您就可以在交易中使用它了。

请查看下面的 GIF 以详细了解工作流程：

![图片](../../images/529_olzpAk2.gif)