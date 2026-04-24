**在 ERPNext 中采购资产涉及创建资产记录、可选地从采购中自动创建资产，以及遵循采购和会计流程。**

资产可以手动采购，也可以在收到采购收据或采购发票中的物料时自动创建。这确保了准确的资产跟踪和正确的会计分录。

## 1. 先决条件

在采购新资产之前，请确保已完成以下配置：

- 已创建 **[资产类别](https://docs.frappe.io/erpnext/user/manual/en/asset-category)**

- 已创建启用了 **"是否为固定资产"** 的[物料](https://docs.frappe.io/erpnext/user/manual/en/item)

- 可选：如果希望物料入库时自动创建资产，请在物料主数据中启用 **"采购时自动创建资产"**

![图片](../../images/442_Screenshot_2026-01-11_at_11.49.39_PM.png)
*物料主数据*

## 2. 如何采购资产

- 按照标准的资产采购流程操作：

- 创建采购订单（如需要）

- 通过采购收据接收物料

- 提交采购发票

- 在采购收据或采购发票的物料明细表中输入资产位置。

- 提交采购收据时：

- 如果启用了自动创建资产，ERPNext 将自动创建资产记录。

- 然后您可以在资产表单中手动更新其他详细信息。

![图片](../../images/442_Screenshot_2025-05-21_at_12.04.07_AM.png)

### 2.1 会计分录

- 启用资本化在建工程（CWIP）时

- 提交采购收据时，在建工程科目被借记，而非资产科目。

- 这表示资产已购买但尚不可用。

- 当资产可以投入使用时，在建工程被贷记，相应的资产科目被借记。

- 禁用 CWIP 时

- 收货分录直接过账到资产类别中定义的资产科目。

- 临时负债科目

- 提交采购收据时，ERPNext 使用 **"已收资产但未开票"**（负债科目）。

- 提交采购发票时，该科目被借记/冲销。

![图片](../../images/442_Screenshot_2026-01-11_at_11.55.53_PM.png)

## 3. 相关主题

- [采购收据](https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt)

- [采购发票](https://docs.frappe.io/erpnext/user/manual/en/purchase-invoice)

---
original_url: https://docs.frappe.io/erpnext/purchasing-an-asset
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---