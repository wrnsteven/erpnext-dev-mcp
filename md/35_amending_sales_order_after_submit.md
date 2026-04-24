---
original_url: "https://docs.frappe.io/erpnext/amending-sales-order-after-submit"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 提交后修改销售订单

现在可以使用 <code>Update Items</code> 按钮在提交后修改销售订单中的单价和数量。

<img src="/images/35_so-update-items.png" alt="Update Items" />

要更新已提交销售订单中的单价和数量，请点击 <code>Update Items</code> 按钮。将会弹出一个对话框让您进行更改。

<img src="/images/35_so-update-items-rate-and-qty.gif" alt="Update Items" />

请注意以下验证和用例：

- 更新功能会检查销售订单是否有 Delivery Note 和 Sales Invoice。
- 可以更新未交货的销售订单和部分交货的发货单的数量。对于已完成交货的发货单，无法更新数量。
- 可以更新未开票和部分开票的销售订单的单价。对于已提交 Sales Invoice 的销售订单，无法更新单价。
