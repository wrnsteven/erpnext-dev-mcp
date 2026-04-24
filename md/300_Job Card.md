```markdown
---
original_url: https://docs.frappe.io/erpnext/job-card
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

## Job Card

**Job Card 用于存储特定工序在特定工作站上执行的实际生产信息。**

Job Card 由 Work Order 创建，并分配给生产车间中的各个工作站，以便根据 Work Order 中定义的各工序，开始生产指定数量的物料。

Job Card 允许各工序工作站针对生产所需的原材料发起"Material Request"和"Stock Transfer to Manufacture"。

Job Card 的完成将改变 Work Order 中的生产状态，我们可以跟踪 Work Order 中各工序的生产进度。

![图片](../../images/300_manufacturing-flow-jc.png)

要访问 Job Card 列表，请前往：

> 首页 > 生产制造 > 生产 > Job Card

## 1. 前置条件

在创建和使用 Job Card 之前，建议先创建以下内容：

- [Bill Of Materials](/erpnext/bill-of-materials)
- [Operation](/erpnext/operation)
- [Workstation](/erpnext/workstation)
- [Work Order](/erpnext/work-order)

## 2. 如何创建 Job Card

当 Work Order 提交时，系统会自动为各工序创建 Job Card。

以下是 Job Card 的示例：

![图片](../../images/300_job-card.png)

使用 Job Card 的步骤如下：

- 点击"开始作业"按钮，完成后点击"完成作业"。

- 或者，您也可以在时间记录表中填写开始时间和结束时间。

- 选择分配到该 Job Card 的员工。

- 输入完成数量。这是指在所选时间间隔内完成该工序的物料数量。

- 在时间记录表中添加更多行，并使用开始/完成按钮记录时间。

- 点击提交。

在 Work Order 中，工序和工作站从物料的 BOM 中获取。为便于使用，您应确保在 BOM 中配置了 [Routing](/erpnext/routing)。

每个创建的 Job Card 都将分配有工作站和工序。所需原材料数量将根据各源仓库的生产需求量计算。

提交 Work Order 后，将根据工序表中的值自动创建 Job Card。

![图片](../../images/300_work-order-job-card-creation.gif)

### 2.1 选择待生产的 Work Order 和物料

您可以在 Bill of Materials 中将"转移物料方式"选择为"Job Card"，以便针对 Job Card 转移生产用原材料。

在 Work Order 中，您可以选择以下选项：

![图片](../../images/300_work-order-transfer-against-job-card.png)

### 2.3 使用 Job Card

员工分配和时间详情也将在 Job Card 中定义。工作所需时间可以记录。如果多个员工在同一个工序上工作，请通过点击"创建 Job Card"按钮添加新的 Job Card。

![图片](../../images/300_job-card-form.png)

### 2.4 基于 Job Card 的 Material Request

系统将从 Job Card 生成 Material Request，作为准备生产过程所需原材料的基准/订单。所生成的 Material Request 将引用原始 Job Card 编号。

![图片](../../images/300_material-request-against-job-card.png)

通过各工序完成情况跟踪 Work Order 中的生产进度。

Job Card 的完成允许您通过查看与 Work Order 相关的各工序完成情况，来跟踪 Work Order 内的生产进度。

![图片](../../images/300_work-order-job-card-completion.png)

### 2.5 废料物品

在完成工序的过程中，可能会产生一些废料。这些废料需要入库。为此，用户需要在 Job Card 中填写废料物品的详细信息。用户也可以在废料物品表中设置缺陷材料/损坏材料。

![图片](../../images/300_job_card_scrap_item.png)

## 3. 功能

### 3.1 质量检验跟踪

> 版本 13 中引入

对于生产订单，在制品（半成品）的质量也需要跟踪。质量由在制品上执行的工序定义，而工序又定义在 Job Card 中。在制品检验与来料检验和出货检验不同。在生产过程中监控质量有助于确保所生产的成品符合所需质量。您可以为生产物料创建针对 Job Card 的 Quality Inspection。

![图片](../../images/300_qi-against-job-card.png)
![图片](../../images/300_qi-link-in-job-card.png)
更多详情，请参阅 [Quality Inspection](/erpnext/quality-inspection) 页面。
```