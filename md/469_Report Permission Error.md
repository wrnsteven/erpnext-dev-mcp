**问题：** 用户被分配了 Account User 和 Account Manager 角色，但在访问 Account Receivable 报告时，仍然收到没有 Territory 主表权限的错误信息。

![图片](../../images/469_Screenshot%202024-06-21%20at%202.31.40%20PM.png)

**回答：**

根据 ERPNext 的权限系统，用户若要访问某个表单或报告，应至少拥有该表单/报告中所有链接字段的读取权限。由于 Territory 是 Account Receivable 报告中的一个链接字段，请添加权限规则，使 Account User/Manager 至少拥有 Territory 主表的读取权限。请按照以下步骤解决此问题。

- 分配给用户的角色是 Account User 和 Account Manager。

- 正如错误信息所示，该用户在 Territory 主表上没有权限。根据默认权限设置，分配给该用户的上述角色都没有 Territory 主表的任何权限。

- 为解决此问题，我已为 Account User 分配了 Territory 主表的读取权限。

![图片](../../images/469_Screenshot%202024-06-21%20at%202.26.27%20PM.png)

根据此权限更新，用户应该能够正常访问 Account Receivable 报告。

---
original_url: https://docs.frappe.io/erpnext/report-permission-error
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---