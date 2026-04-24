Rebuild Tree 功能是 ERPNext 中的一个工具，用于纠正和刷新层级数据的结构完整性，特别是会计科目表（CoA）。它确保账户的父子关系和显示顺序在整个系统中准确反映。

**问题描述**：

有时用户在总账报告中选择账户时，报告中的数据却显示为不同的账户，如下面的截图所示。
![图片](../../images/460_Rebuild%20Issue.png)
在这种情况下，可以使用 **Rebuild Tree** 功能来轻松解决此问题。

**重建 CoA 树的逐步指南**

重建树是一个快速的过程。

**步骤 1**：访问会计科目表
导航到会计科目表树形视图：
Accounting > 会计科目表

**步骤 2**：打开操作菜单
在会计科目表树形界面中，找到并点击窗口右上角的菜单按钮（通常用三个点或线条表示）。
**步骤 3**：选择"Rebuild Tree"
从出现的下拉菜单中，选择 Rebuild Tree 选项。
![图片](../../images/460_Screenshot%202025-10-16%20at%201.27.11%E2%80%AFPM.png)

重建树过程完成后，您可以检查总账报告是否在报告中显示了正确的数据。

![图片](../../images/460_Screenshot%202025-10-16%20at%201.11.56%E2%80%AFPM.png)

---
original_url: https://docs.frappe.io/erpnext/rebuild-tree
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---