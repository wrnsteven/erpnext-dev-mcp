---
original_url: https://docs.frappe.io/erpnext/make-a-colorful-gantt-chart
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

ERPNext 允许用户为特定文档添加颜色，以获得更好的视觉提示和呈现效果。一个很好的例子是 [Event Calendar](/erpnext/how-to-sync-doc-types-with-calendar)，您可以为每个事件添加颜色。

我们将在 Projects 模块中通过自定义 [Tasks](/erpnext/tasks) 来实现此功能。

## 为甘特图添加颜色的步骤

- 进入系统中的 [Customize Form](/erpnext/customize-form)，在 *Enter Form Type* 选项中选择 *Task*。或者，您也可以通过 Task 列表或表单中的 **菜单 > 自定义** 到达此页面。

![图片](../../images/321_project-gantt-customize-form-1.gif)

- 在 doctype 中添加一个 fieldtype 为 color 的新字段。

- 勾选 *In List View* 选项。

![图片](../../images/321_project-gantt-in-list.png)

- 保存表单，返回 Task 列表并刷新页面。

- 打开现有或新建的 Task 时，您应该会看到一个 color 字段。为 Task 选择一种颜色。

![图片](../../images/321_project-gantt-pick-color.png)

- 返回 Task 列表并切换到 Gantt 视图。

![图片](../../images/321_project-gantt-colors.png)