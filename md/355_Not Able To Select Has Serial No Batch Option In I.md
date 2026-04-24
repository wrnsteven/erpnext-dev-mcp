有时你可能不想从一开始就将库存作为批次和/或序列号进行追踪，而是希望在后续阶段才启用此功能。
系统在设计上不允许在已有库存交易后激活这些选项。![图片](../../images/355_a0VHlSB.png)
你可以阅读更多关于此选项为何被禁用的信息[点击此处](https://erpnext.com/docs/user/manual/en/stock/articles/maintain-stock-field-frozen-in-item-master.html)。

要重新启用这些选项，你可以删除该物料的所有库存交易，或者如果无法删除，可以复制相同物料并以勾选这些选项的方式入库。

**步骤：**

1. 首先，你必须使用库存调整工具（Stock Reconciliation Tool）将当前物料的库存清空（使当前库存为零）。你也可以通过创建类型为 **物料发料（Material issue）** 的库存调拨来清空库存。
2. 然后使用物料收料（Material Receipt）入库序列号库存。关于此操作的帮助，请参阅以下链接：[序列号和批次物料的期初库存余额录入](/erpnext/opening-stock-balance-entry-for-serialized-and-batch-item)
3. 禁用旧物料，使其无法再次在交易中被选中。

**注意：** 如果你想保持相同的物料代码，你需要先重命名现有物料，然后再按实际物料代码创建新物料。否则，你将使用新代码来管理该物料。

---
original_url: https://docs.frappe.io/erpnext/not-able-to-select-has-serial-no-batch-option-in-item-list
translated_by: AI (Claude Code)
translation_date: 2026-04-18