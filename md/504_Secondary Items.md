> **注意**
> **仅在 ERPNext 第 16 版中可用**

从第 16 版开始，BOM DocType 中的 Scrap Items（废料项目）表已更名为 Secondary Items（副产品）表。副产品表现在包含 3 种更多类型的项目：`Co-Product`（联产品）、`By-Product`（副产物）和 `Additional Finished Good`（额外成品）。使用此表，用户现在可以基于百分比系统指定所有产出的成本（或原材料成本）分配。

让我们首先了解 `Scrap`、`Co-Product`、`By-Product` 和 `Additional Finished Good` 之间的区别。

- **Scrap（废料）**：与成品一起生产的产品，在大多数情况下没有太大价值。
- **Co-Product（联产品）**：与主成品一起计划生产的具有重要价值的产品。
- **By-Product（副产物）**：与成品一起生产但非计划内的产品。该产品可能具有或不具有重要价值。
- **Additional Finished Good（额外成品）**：这是计划内的产品，具有重要价值。它通常通过额外材料、剩余产能或进一步加工单独生产。

在 ERPNext 中，这些副产品的价值和数量计算方式实际上没有区别。不同的名称仅用于区分目的。

您可以在表中指定每个副产品的工艺损耗百分比和成本分配百分比。

![图片](../../images/504_image01125b.png)

在这个例子中，我们假设在生产汽油时，10% 的产出（原材料）成本应分配给 LPG，5% 分配给沥青。剩余的 85% 将分配给实际成品（汽油）。

让我们来看看实际效果：

![图片](../../images/504_CleanShot%202026-03-11%20at%2012.31.02@2x.png)

这里，产出成本为 100 卢比。100 的 10% 是 10，分配给 LPG；5% 是 5，分配给沥青。由于我们为沥青指定了 5% 的工艺损耗，其数量计算为 9.5（`10 - (5% * 10)`）。

> **注意**
> **如果您是从早期版本的 ERPNext 迁移而来，废料项目表将保持原样。那些废料项目将被标记为** `legacy`**，制造单据和分包收据中的计算将与迁移前保持一致。**

---
original_url: https://docs.frappe.io/erpnext/secondary-items
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---