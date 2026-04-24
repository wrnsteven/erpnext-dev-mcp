# 从 *x* 应用程序迁移到 ERPNext 时，如何记录预付款应付账款并与未来发票对账？

## 记录预付款应付账款

创建一个类型为 **Opening Entry** 的 **Journal Entry**，借方选择 *Creditor Account* 并选择相应的 *Supplier*，贷方选择 *Temporary Opening Account*。

展开债权人的行，为 *Is Advance* 选择 **Yes**。

*请参阅下面的 GIF 演示：*

![图片](../../images/461_CsMRH40.gif)

提交 Journal Entry 后，**Accounts Payable Summary** 将显示负余额：

![图片](../../images/461_cJ2xpY7.png)

## 与采购发票对账

创建 Purchase Invoice 后，查看 **Accounts Payable** 报告：

![图片](../../images/461_cxZArKd.png)

目前，它们尚未对账，显示为**两个独立条目**，请使用 **Payment Reconciliation** 工具对账这两个条目，*请参阅 GIF 了解步骤：*

![图片](../../images/461_jbj6LRc.gif)

对账后查看 Accounts Payable 报告，**Journal Entry** 将不再显示，只会反映（*发票金额 - 预付款金额*）：

![图片](../../images/461_vaXYQNc.png)

---

original_url: https://docs.frappe.io/erpnext/reconcile-advance-payment-made-to-the-supplier
translated_by: AI (Claude Code)
translation_date: 2026-04-18