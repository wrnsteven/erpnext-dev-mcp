很多时候，当生成涉及大量数据的报告时，例如整个年度的分类账报告，你可能会遇到以下错误信息：**请求超时**。这是因为报告中需要处理和展示大量数据，但服务器资源不足，从而导致超时。

为了更好地处理此类报告，ERPNext 提供了预生成报告功能（自 v11 起）。当报告被设置为预生成报告时，它会通过[后台任务](/framework/user/en/guides/app-development/running-background-jobs)生成，生成完成后用户即可查看。

## 设置预生成报告的步骤

- 进入[页面和报告的角色权限](/erpnext/role-permission-for-page-and-report)。

- 在"设置角色对象"字段中选择**报告**。

- 在"报告"字段中选择你要启用/禁用预生成报告的报告。

- 使用**禁用预生成报告**复选框来启用/禁用预生成报告。如果勾选此选项，所选报告的预生成报告功能将被禁用。

- 点击**更新**。

![图片](../../images/398_set-prep-report.gif)

## 如何使用预生成报告

- 打开相应报告（例如总账），并应用所需的所有筛选条件。

如果该报告已启用预生成报告选项，你将看到一个**生成报告**按钮。点击该按钮。
![图片](../../images/398_prepared-report-generate.png)
你将在屏幕右下角看到一条通知："报告已启动。你可以*在此*查看其状态"
![图片](../../images/398_prepared-report-bg.png)
你可以留在当前页面等待，也可以点击上述消息中的*此处*打开报告页面。这将为你打开一个新的报告页面：
![图片](../../images/398_prepared-report-queued.png)
如你所见，报告页面的状态显示为"排队中"。一旦报告生成完成，你将看到一个**显示报告**按钮，点击即可查看报告：
![图片](../../images/398_prepared-report-page.png)
- 由于预生成报告本身也是一个 doctype，要查看预生成报告列表，你可以使用[角色权限管理器](/erpnext/role-based-permissions)来授予相应的访问权限。

---
original_url: https://docs.frappe.io/erpnext/prepared-report
translated_by: AI (Claude Code)
translation_date: 2026-04-18