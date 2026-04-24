---
original_url: https://docs.frappe.io/erpnext/auto-creation-of-material-request
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 自动创建物料请求

为防止库存短缺，你可以跟踪商品的再订货水平。当库存水平低于再订货水平时，采购经理会收到通知并被指示启动该商品的采购流程。

在 ERPNext 中，你可以在商品主数据中更新商品的再订货水平和再订货数量。如果同一商品有不同的再订货水平，你也可以按仓库更新再订货水平和再订货数量。

![reorder level](images/56_reorder-request-1.png)

通过再订货水平，你还可以定义下一个操作应该是什么。是新采购还是从另一个仓库调拨。根据商品主数据中的设置，目的也将更新在物料请求中。

![reorder level next action](images/56_reorder-request-2.png)

当商品的库存达到再订货水平时，物料请求会自动创建。你可以从此处启用此功能：

`Stock > Setup > Stock Settings`

![active auto-material request](images/56_reorder-request-3.png)

每个商品将创建单独的物料请求。具有采购经理角色的用户将收到有关这些物料请求的电子邮件提醒。

如果自动创建物料请求失败，具有采购经理角色的用户将收到错误消息通知。最常见的错误消息之一是：

**在基于再订货水平创建物料请求时，某些商品发生了错误。日期 01-04-2016 不在任何会计年度中。**

错误的原因之一可能是会计年度。点击此处了解更多。

### 注意：

系统通过将集团仓库的预计数量与再订货水平进行比较来创建物料请求。如果未设置集团仓库，则系统将请求仓库的预计数量与再订货水平进行比较。如果预计数量大于再订货水平，则系统不会将该商品添加到物料请求中。
