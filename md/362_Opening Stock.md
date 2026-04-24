**期初库存是指在会计期初，企业可用于销售或使用的物料数量和价值。**

上一会计期间的期末库存将成为本期初的期初库存。

## 1. 前置条件

- 创建[仓库](/erpnext/warehouse)。

- 将仓库链接到相应的会计科目。

## 2. 非序列号管理物品的期初库存

要过账期初库存，请访问[库存调整](/erpnext/stock-reconciliation)页面。

## 3. 序列号管理和批次管理物品的期初库存

请提前创建[批次](/erpnext/batch)和[序列号](/erpnext/serial-no)记录。要过账序列号管理和批次管理物品的期初库存：

- 进入 **库存 > 库存交易 > 库存录入 > 新建**。

- 在"库存录入类型"中选择"物料入库"。

- 将`Is Opening`设置为`Yes`。

- 在"默认目标仓库"中选择仓库。

- 在物料明细表中，选择物料代码、数量和基本 Rate。

- 对于批次管理物品，选择批次号。

- 对于序列号管理物品，选择序列号。

- 保存并提交。

### 5. 相关主题

- [库存会计](/erpnext/accounting-of-inventory-stock)

- [库存录入](/erpnext/stock-entry)

- [库存调整](/erpnext/stock-reconciliation)

---
original_url: https://docs.frappe.io/erpnext/opening-stock
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---