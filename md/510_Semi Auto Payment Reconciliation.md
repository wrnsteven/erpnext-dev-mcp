如果存在大量需要快速对账而不进行手动分配的发票，可以使用 `Process Payment Reconciliation` doctype。

## 步骤：

- 首先需要在账户设置中启用此功能。在账户设置中启用 `Auto Reconcile Payments`。

![图片](../images/510_Screenshot%202024-08-20%20at%203.51.12%20PM.png)

- 导航至 `Process Payment Reconciliation` doctype

- 选择需要进行对账的公司、交易对象及应收/应付账户。保存并提交

- 文档状态将为 `已排队`。

![图片](../images/510_Screenshot%202024-08-20%20at%203.55.43%20PM.png)

- 每 15 分钟运行一次的后台作业会拾取 `已排队` 的文档并开始对账。如有需要，可以使用 `开始/继续` 按钮立即触发作业。

- 这将创建一条 `Process Payment Reconciliation Log` 记录，其中包含将处理的分配总数以及成功对账的条目详情。

![图片](../images/510_Screenshot%202024-08-20%20at%204.00.49%20PM.png)

## 相关主题

- [Payment Reconciliation](/erpnext/payment-reconciliation)

---
original_url: https://docs.frappe.io/erpnext/semi-auto-payment-reconciliation
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---