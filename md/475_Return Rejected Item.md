---
original_url: https://docs.frappe.io/erpnext/return-rejected-item
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

在采购收料单中，您可以将在途仓库中的物料接收至已验收仓库或已拒绝仓库。

如果您需要为已拒绝仓库中收到的物料创建采购退货，请按照以下步骤创建退货单据。

- 在采购收料单明细表中，对于需要退货的物料，在"已收货数量"字段中输入负数的退货数量。

- 将"已验收仓库"字段的值设置为零。

- 在"已拒绝仓库"字段中，输入负数的退货数量。

有关为拒绝物料创建采购退货单据的详细步骤，请参阅下面的示例。

![图片](../../images/475_purchase-return.gif)