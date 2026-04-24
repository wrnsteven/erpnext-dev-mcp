# ERPNext 项目模块入门

ERPNext 中的项目模块用于跟踪涉及多个步骤、人员和交易的工作。项目将任务、时间、材料、交货和计费统一在一个参考编号下。

下面的示例展示了如何将简单的制造工作作为项目进行管理，以及它如何与其他 ERPNext 模块建立连接。

## 场景

一家制造公司收到订单，为仓库客户制作一个**定制金属储物架**。

### 前提条件

- 创建一个[物料](https://docs.frappe.io/erpnext/user/manual/en/item) - 储物架

### 步骤 1：为储物架创建销售订单

- 要创建销售订单，请前往：

> 首页 > 销售 > 销售订单

![图片](../../images/432_sales_order.png)
*包含储物架的销售订单*

### 步骤 2：从销售订单创建项目

- 提交销售订单后，我们可以从销售订单创建项目

![图片](../../images/432_project from sales order.png)
*从销售订单创建项目*

- 项目创建后，仪表盘也将被创建，这将允许创建任务和时间表

![图片](../../images/432_project dashboard.png)
*项目仪表盘*

### 步骤 3：为项目创建基础任务

- 我们为项目创建单独的任务，如切割和焊接、喷漆以及最终组装。

![图片](../../images/432_taskf4bc2a.png)
*切割和焊接任务*

### 步骤 4：同时为原材料创建采购订单及相应的库存记录

- 制造储物架所需的原材料将进行采购，因此将为相同物料创建采购订单

![图片](../../images/432_purchase order.png)
*原材料采购订单*

### 步骤 5：创建时间表以记录钢构件和油漆的执行情况

- 为了记录钢构件的执行和储物架的喷漆过程，我们创建时间表

- 此项目中进行的更改将反映成本和计费详情

![图片](../../images/432_timesheet.png)
*时间表中的执行详情*

### 步骤 6：随着流程推进，我们更新任务的进度

![图片](../../images/432_task status.png)
*任务状态*

- 所有任务完成后，项目也将进入完全完成状态

![图片](../../images/432_completed project.png)
*最终项目状态*

---
original_url: https://docs.frappe.io/erpnext/projects/introduction/getting-started
translated_by: AI (Claude Code)
translation_date: 2026-04-18