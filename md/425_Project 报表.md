# Project 报表

这些报表有助于跟踪项目进度、项目状态以及关键指标（如时间线、成本和资源分配）。

## Project Summary

**Project Summary** 提供项目关键信息的概览，包括当前项目状态、开始和结束日期，以及相关记录的汇总视图。它显示关联的 **Tasks** 和 **Timesheets** 数量，让用户能够一目了然地快速评估项目进度和活动情况。

下图展示了我们之前在 Rack Storage 制造入门示例中讨论的摘要。

![图片](../../images/425_project_summary.png)
*Project Summary*

## Daily Timesheet Summary

**Daily Timesheet Summary** 提供选定时间段内 Timesheet 中记录的所有任务的汇总视图。它显示 Timesheet 活动以及已记录工时和对应的关联任务与项目，让用户能够一目了然地审查每日时间分配情况。

![图片](../../images/425_daily_timesheet_summary.png)
*Daily Timesheet Summary*

## Timesheet Billing Summary

此报表提供选定时间段内基于 Timesheet 的计费摘要。它显示总工时以及对应的可计费工时、计费费率和计算的计费金额，让用户能够一目了然地审查和分析工时材料计费情况。

![图片](../../images/425_timesheet_billing_summary.png)
*Timesheet Billing Summary*

## Project Wise Stock Tracking

此报表提供与项目相关的库存移动明细，包括采购物料和发出物料。它还显示关键项目信息，如项目状态、项目总价值和项目开始及完成日期，便于有效跟踪物料使用情况和整体项目进度。

![图片](../../images/425_project_wise_stock_tracking.png)
*Project wise stock tracking*

## Delayed Task Summary

Delayed Tasks Summary 报表帮助识别已超过预期结束日期的任务。它提供正常进度和延迟任务的明细，以及当前进度和预期开始及结束日期，便于用户识别进度偏差并采取纠正措施。

查看此报表的路径：

> Home > Projects > Reports > Delayed Tasks Summary

该报表基于 Task Doctype 生成。

### 延迟计算方式

Task 有一个日期字段称为 **Completed On**，当 Task 状态更改为 Completed 时该字段才会显示。

##### 场景 1

如果任务被标记为已完成且设置了 Completed On 字段，则延迟时间计算为 Completed On 与预期结束日期之间的差值。

```
Delay = Completed On - Expected End Date
```

##### 场景 2

如果未设置 Completed On 字段，则延迟时间计算为当前日期与预期结束日期之间的差值。

```
Delay = Current Date - Expected End Date
```

### 图表

图表显示根据应用筛选条件生成的报表中处于 On Track 或 Delayed 状态的任务数量。

![图片](../../images/425_delayed-tasks-summary.png)
*Delayed Tasks Summary*

---
original_url: https://docs.frappe.io/erpnext/project-reports
translated_by: AI (Claude Code)
translation_date: 2026-04-18