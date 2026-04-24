---
original_url: "https://docs.frappe.io/erpnext/allow-over-delivery-billing-against-sales-order-upto-certain-limit"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 允许超出订单一定限额的交货/开票

创建 Delivery Note 时，系统会验证商品的数量的与 Sales Order 是否一致。如果商品数量增加，您将收到关于超出交货或收款的验证消息。

考虑到销售情况，如果您希望能够交付比 Sales Order 中规定的更多商品，您应该在 Item master 中更新"允许超出此百分比限额的交货或收款"。

<img src="/images/32_limit-1.png" alt="Itemised Limit Percentage" />

创建发票时，商品单价也会根据前置交易（如 Sales Order）进行验证。这同样适用于从 Purchase Order 创建 Purchase Receipt 或 Purchase Invoice。更新"允许超出此百分比限额的交货或收款"将影响所有销售和采购交易。

例如，如果您订购了 100 件商品，并且商品的超出收货百分比为 50，则您最多可以创建 150 件商品的 Purchase Receipt。

从 Stock Settings 更新"允许超出此百分比限额的交货或收款"的全局值。在此更新的值将适用于所有商品。

1. 转到 <code>Stock > Setup > Stock Settings</code>
2. 设置 <code>Limit Percentage</code>。
3. 保存 Stock Settings。

<img src="/images/32_TGPrUJY.png" alt="" />
