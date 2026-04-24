---
original_url: https://docs.frappe.io/erpnext/purchase-invoice-account-type-error
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

**问题：** 保存 Purchase Invoice 时，我收到一条验证消息，提示 Credit To Account 必须是资产负债表账户。

![图片](../../images/436_credit-to-ledger-in-purchase-invoice.png)

**答案：** 提交 Purchase Invoice 时，应付款会更新至 Supplier。根据会计准则，Payable Account 归属于流动负债（资产负债表的贷方）。

错误消息表明，在 Credit To 字段中选择的账户不属于 Liability 组。请确保在 Purchase Invoice 中选择的 Payable Account 位于 Liability 组下。