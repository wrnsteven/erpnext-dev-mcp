**退还的采购物料称为采购退货。**

通过采购退货功能，您可以将产品退还给供应商。这可能是由于多种原因，例如货物缺陷、质量不符、采购方不再需要该库存等。

## 1. 前提条件

在创建和使用采购退货之前，建议您先创建以下内容：

- [物料](/erpnext/item)
- [采购发票](/erpnext/purchase-invoice)

或

[采购收货](/erpnext/purchase-receipt)

## 2. 如何创建采购退货

- 首先打开原始的采购收货单，供应商就是通过该单据交付物料的。

![图片](../../images/439_purchase-return-original-purchase-receipt.png)

- 点击"创建 > 退货"，这将打开一个新的采购收货单，并勾选"为退货"。物料、单价和税费将显示为负数。

![图片](../../images/439_purchase-return-against-purchase-receipt.png)

- 提交采购退货后，系统将从指定仓库减少物料数量。为保持正确的库存估值，库存余额将根据退货物料的原始采购价格相应增加。

![图片](../../images/439_purchase-return-stock-ledger.png)

- 在会计账本中，手头库存账户将贷记，库存已收但未开票账户将借记。

![图片](../../images/439_purchase-return-general-ledger.png)

如果启用了持续库存，系统还将过账与仓库账户对应的会计分录，以使仓库账户余额与库存账本的库存余额保持同步。

## 3. 通过采购收货退货对库存的影响

在创建针对采购收货的采购退货时：

原始采购收货单以及关联的采购订单中的**退货数量**将更新。

如果100%退货，原始采购收货单的状态将变更为**已退货**：
![图片](../../images/439_purchase-return-issue.png)

### 4. 相关主题

- [销售退货](/erpnext/sales-return)
- [持续库存](/erpnext/perpetual-inventory)

---
original_url: https://docs.frappe.io/erpnext/purchase-return
translated_by: AI (Claude Code)
translation_date: 2026-04-18