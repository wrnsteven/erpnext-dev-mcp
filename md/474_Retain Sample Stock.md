---
original_url: https://docs.frappe.io/erpnext/retain-sample-stock
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

**样品库存是指为应对未来可能出现的分析需求而储存的任何物料批次。**

用于储存样品库存的物料可以是原材料、包装材料或成品。

## 1. 前置条件

在使用样品保留功能之前，建议您先创建以下内容：

- [物料](/erpnext/item)

- [批次](/erpnext/batch)

- [仓库](/erpnext/warehouse)

## 1. 如何在库存设置中设置样品保留仓库

建议单独创建一个仓库用于保留样品，不要在生产中使用该仓库。

![图片](../../images/474_sample-warehouse.png)

### 1.2 在物料主数据中启用保留样品

保留样品基于批次，因此必须先启用"有批次号"。勾选"保留样品"并设置每个批次允许的最大样品数量。

![图片](../../images/474_retain-sample.png)

### 1.3 创建库存事务

- 每当创建目的为"物料入库"的[库存事务](/erpnext/stock-entry)时，对于已启用"保留样品"的物料，可以在库存事务中设置样品数量。您需要为物料选择批次号。样品数量不能超过物料主数据中设置的最大样品数量。

![图片](../../images/474_material-receipt-sample.png)

- 提交此库存事务后，将出现"创建保留库存事务"按钮，用于将样品物料从相关批次转移到库存设置中设置的保留仓库。

![图片](../../images/474_sample-retention-button.png)

- 点击此按钮将跳转至新的"物料转移"类型的库存事务。此事务将您的样品从目标仓库（Stores）转移至样品保留仓库。其中将包含所有信息，请核实后点击提交。

![图片](../../images/474_material-transfer-sample.png)

## 2. 相关主题

- [仓库](/erpnext/warehouse)