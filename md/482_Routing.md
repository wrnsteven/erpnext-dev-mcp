**Routing 是 BOM 工序的模板。**

Routing 用于存储所有工序及其描述、小时费率、工序时间、批量大小等信息。当不同产品的制造使用相似的工序时，为 BOM 工序创建 Routing 非常有用。

### 前置条件

- [工序](/erpnext/operation)
- [工作站](/erpnext/workstation)

## 如何创建 Routing

- 进入 Routing 列表，点击"新建"。
- 输入 Routing 的名称。
- 在 BOM 工序表中输入工序：

  - 选择工序。
  - 将自动获取默认工作站。
  - 输入该工序运行的小时费率。
  - 输入工序时间（分钟）。
  - 输入批量大小，即该工序处理的单位数量。
  - 系统将根据小时费率和工序时间自动计算工序成本。
- 保存。

创建后，可以在 BOM 中选择 Routing 以获取其中存储的工序。

![图片](../images/482_CleanShot%202026-02-19%20at%2012.31.10@2x.png)

## Routing 中的序列 ID

![图片](../images/482_image2679eb.png)

序列 ID 要求用户通过工票按顺序完成工序。如果用户尝试在完成前置工序之前完成某个工序（根据序列 ID），系统将抛出验证错误。

### 相关主题

- [工单](/erpnext/work-order)
- [物料清单](/erpnext/bill-of-materials)

---
original_url: https://docs.frappe.io/erpnext/routing
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---