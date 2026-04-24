**物料替代是原始物料的类似物料，可用于替代原始物料进行生产。**

如果在生产过程中 BOM 中定义的原材料不可用，则可以使用各自可用的替代物料来完成生产过程。

首先需要在物料中启用"允许替代物料"。

![图片](../images/290_allow-alternative-item.png)

要访问物料替代列表，请转到：

> 首页 > 库存 > 物料与定价 > 物料替代

也可以通过在物料主控台中点击"物料替代"旁边的加号来完成此操作。

如果两个物料可以互相作为替代品使用，您可以在这两个物料之间启用双向替换。

![图片](../images/290_item-alternative.png)

## 1. 前置条件

在创建和使用物料替代之前，建议先创建以下内容：

- [物料](/erpnext/item)

## 2. 工单物料替代

要允许在制造过程中使用替代物料，用户可以在 BOM/工单中配置"允许替代物料"

### 2.1 在 BOM 中允许替代物料的设置

您可以在 BOM 中启用"允许替代物料"，然后在库存调拨中选择替代物料。这也可以通过工单来完成。

![图片](../images/290_allow-alternative-item-bom.png)

### 2.2 在工单中允许替代物料的设置

用户也可以为单个工单启用/禁用允许替代物料。

![图片](../images/290_allow-alternative-item-wo.png)

勾选"允许替代物料"复选框将显示一个名为"替代物料"的按钮。您可以点击此按钮在工单中设置物料替代。以下是在工单中使用物料替代的方法：

![图片](../images/290_work_order_item_alternative.gif)

以下是在库存调拨中使用物料替代的方法：

![图片](../images/290_se_item_alternative.gif)

如果物料表中的"允许替代物料"复选框被禁用，则无法为此物料设置替代物料。

### 2.3 委外加工的物料替代

在委外加工中，用户需要将原材料转移给委外供应商以获取成品。如果库存中没有原材料，使用此功能，用户可以将委外原材料的替代物料转移给供应商。这在库存调拨中完成。

![图片](../images/290_purchase_order_item_alternative.gif)

之后，当您从工单创建采购收货时，将显示替代物料。

### 3. 相关主题

- [物料清单](/erpnext/bill-of-materials)

- [工单](/erpnext/work-order)

---
original_url: https://docs.frappe.io/erpnext/item-alternative
translated_by: AI (Claude Code)
translation_date: 2026-04-18