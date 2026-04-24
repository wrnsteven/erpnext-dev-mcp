在 [Permission Manager](/erpnext/role-based-permissions) 中自定义规则时，可能会收到以下错误信息：

> 对于 Customer（或任何其他文档）第 8 行中的 System Manager *（或任何其他角色）*，在级别 2 *（或其他级别）*：必须先设置 0 级别的权限，才能设置更高级别的权限。

错误信息表明问题出在该文档现有的权限设置上。

对于任何角色，在分配 Perm Level 1 或 2（依此类推）的权限之前，必须先分配 Perm Level 0 的权限。错误信息显示 System Manager 已被分配了 Perm Level 1 和 2 的权限，但未被分配级别 0 的权限。您应首先通过以下方式更正 System Manager 角色的权限：

- 在级别 0 为 System Manager 分配权限。

或

- 移除级别 1 和 2 的权限。

执行上述步骤之一后，您应该能够在 Role Permission Manager 中成功添加新的权限规则。

---
original_url: https://docs.frappe.io/erpnext/perm-level-error-in-permission-manager
translated_by: AI (Claude Code)
translation_date: 2026-04-18