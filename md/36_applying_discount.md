---
original_url: "https://docs.frappe.io/erpnext/applying-discount"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 应用折扣

在销售交易中，有多种方式可以对商品应用折扣。这可以在所有销售和采购交易中完成。

## 1. 按商品价目表价格的折扣

您可以在交易的商品表中找到折扣字段，点击行右侧的向下箭头。折扣可以作为百分比或与商品价目表价格相关的固定金额来应用。

<img src="/images/36_discount-on-price-list-rate.png" alt="Discount on Price List Rate" />

折扣（%）功能在所有销售和采购交易中都可用。

如果您想定期对 certain quantities 应用折扣（作为百分比），最好使用"定价规则"。阅读 <a href="/erpnext/pricing-rule">Pricing Rule</a> 文档了解更多。

## 2. 按净额或grand总额折扣

在"附加折扣"部分（"Sales Order"或"Sales Invoice"相同），您可以按总销售额的固定金额或百分比应用折扣。

<img src="/images/36_additional-discount.png" alt="Additional Discount" />

### 2.1 按"净额"折扣

如果按**净额**应用折扣，则商品的净额率和净额金额将根据折扣金额计算。只有在使用此功能应用折扣时，净额率和金额字段才会显示。

<img src="/images/36_discount-on-net-total.png" alt="Discount on Net Total" />

### 2.2 按"总额"折扣

如果基于**总额**应用折扣，则商品的净额率、净额金额以及税费都将根据折扣金额重新计算。

<img src="/images/36_discount-on-grand-total.png" alt="Discount on Grand Total" />