---
original_url: "https://docs.frappe.io/erpnext/allocating-credit-note-and-payment"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 分配贷项通知单和付款

<strong>问题：</strong>我们有客户在发票付款后退回商品。因此，我们通常会创建贷项通知单。但有时没有其他未结发票可以分配贷项通知单。在这种情况下，我们需要向客户退款。我如何处理这种交易，以避免在发票列表中出现负面信贷？

<strong>答案</strong>

您应该能够按照下面分享的步骤来处理这个特定场景。

1. 首先，针对发票创建贷项通知单
2. 然后为退货金额创建付款条目
3. 使用付款对账将付款与原始 Sales Invoice（而不是贷项通知单本身）进行勾销。

<strong>注意：</strong>在采购循环中（您在系统中为类似场景创建借项通知单），步骤如下：

1. 首先，针对采购发票在系统中创建借项通知单
2. 然后为退货金额创建付款条目
3. 使用付款对账将付款与原始 Purchase Invoice（而不是借项通知单本身）进行勾销。
