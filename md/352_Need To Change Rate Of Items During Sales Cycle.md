---
original_url: https://docs.frappe.io/erpdocs/need-to-change-rate-of-items-during-sales-cycle
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

有时，Sales Invoice 中物品的税率可能与 Sales Order 中声明的税率不同。您可以按照以下步骤在 ERPNext 中进行此配置：

进入 **Selling Settings**，确保取消勾选 **"Maintain Same Rate Throughout Sales Cycle"**（在整个销售周期保持相同税率）复选框。此设置将允许您在不同的销售交易（Sales Order、Delivery Note、Sales Invoice 等）中为同一物品设置不同的税率。
![图片](../../images/352_SzkWIfA.png)

进入 **Accounts Settings**，设置 **Over Billing Allowance (%)**（超额开票允许百分比）。
![图片](../../images/352_xOc0kCY.png)

通过以上两个设置，您可以在销售交易中更改物品的税率。