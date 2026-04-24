在许多制造业中，存在一种常见的场景：使用一种原材料（RM）生产多种成品。大多数化工制造业都能看到这种业务用例。那么如何在 ERPNext 中实现这种场景呢？让我们以石油制造业为例，从原油中可以产出汽油、燃气、柴油、煤油等多种产品。

首先，创建一个物料主数据，其中原油作为原材料（RM），而汽油、燃气、柴油、煤油等作为成品（FG）。这里每种产品也可以使用不同的计量单位（UOM）。

创建物料主数据后，为任意一种要用原油（RM）生产的成品（FG）创建物料清单（BOM）。这里我为 25 升汽油创建了物料清单，其中将使用 100 升原油（RM）。其他成品如燃气、柴油和煤油我添加到了废料（Scrap）部分。

![图片](../../images/263_1VHaiPf.png)
![图片](../../images/263_mg68Dbr.png)

在创建物料清单时，您也可以添加工序，并据此运行您的生产周期（工单）。

工单完成后，在后冲（Back-flush）过账时，您的原材料将被消耗，而您将获得多种成品。

---
original_url: https://docs.frappe.io/erpnext/how-to-handle-a-scenario-of-1-raw-material-multiple-finish-goods
translated_by: AI (Claude Code)
translation_date: 2026-04-18