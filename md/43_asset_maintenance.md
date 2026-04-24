---
original_url: "https://docs.frappe.io/erpnext/asset-maintenance"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 资产维护

资产维护是指对资产进行任何活动以保持其性能或状态。

ERPNext 提供功能来追踪资产 individual 维护/校准任务的详情，包括日期、负责维护的人员以及未来的维护到期日期。

要访问资产维护列表，请转到：

> Home > Assets > Maintenance > Asset Maintenance

## 1. 先决条件

- 创建一个<a href="/erpnext/asset">资产</a>
- 创建一个<a href="/erpnext/asset-maintenance-team">资产维护团队</a>。

<img src="/images/43_Screenshot 2026-01-09 at 5.41.00PM.png" alt="" />

## 2. 如何创建资产维护记录

1. 转到<strong>Asset Maintenance</strong>。
2. 点击<strong>New</strong>。
3. 填写所需的详细信息：

- 基本详情
  - <strong>Asset</strong>：选择需要维护的资产。
  - <strong>Maintenance Team</strong>：选择负责的团队。
  - <strong>Maintenance Type</strong>：
    - <strong>Preventive</strong> – 计划的例行维护。
    - <strong>Calibration</strong> – 恢复测量精度的调整。
- 计划详情
  - <strong>Start Date</strong>：计划开始维护的日期。
  - <strong>End Date</strong>：预期完成日期。
  - <strong>Last Completion Date</strong>：如果维护晚于计划完成，请输入实际完成日期。

4. 保存并提交文档。

> Asset Maintenance 是一个交易，必须提交以确认计划。

## 3. 功能

### 3.1 资产维护日志

提交后：

- 创建了一个<strong>Asset Maintenance Log</strong>。
- 日志追踪维护任务的执行。
- 未来的维护到期日期基于计划自动计算。

### 3.2 ToDo 中的维护

当维护任务分配给用户时：

- 它会自动出现在分配用户的<strong>ToDo 列表</strong>中。
- 这确保了负责人员得到通知和提醒。

<img src="/images/43_Screenshot 2026-01-09 at 5.47.59PM.png" alt="" />