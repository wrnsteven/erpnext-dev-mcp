---
original_url: "https://docs.frappe.io/erpnext/amending-purchase-order-after-submit"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 提交后修改采购订单

现在可以使用 <code>Update Items</code> 按钮在提交后修改采购订单中的单价和数量。

<img src="/images/34_po-update-items.png" alt="Update Items" />

要更新已提交采购订单中的单价和数量，请点击 <code>Update Items</code> 按钮。将会弹出一个对话框让您进行更改。

<img src="/images/34_po-update-items-rate-and-qty.gif" alt="Update Items" />

请注意以下验证和用例：

- 更新功能会检查采购订单是否有采购收货单和采购发票。
- 可以更新未收货和部分收货的采购订单的数量。对于已完成采购收货的采购订单，无法更新数量。
- 可以更新未开票和部分开票的采购订单的单价。对于已提交采购发票的采购订单，无法更新单价。
