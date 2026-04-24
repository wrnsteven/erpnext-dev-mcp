---
description: 描述
translated_by: AI (Claude Code)
translation_date: 2026-04-18
original_url: https://docs.frappe.io/erpnext/issue
---

**Issue 是来自 Customer 的来询，通常通过电子邮件或您网站的 *Contact* 部分接收。**

> 提示：设置一个专用的支持邮箱是追踪客户来询的好方法。例如，您可以将支持请求发送至 ERPNext 的 support@erpnext.com，系统将自动在其中创建一个 Issue。

要访问 Issue 列表，请前往：

> Home > Support > Issues > Issue

![图片](../../images/286_issue.png)

## 1. 前置条件

在创建和使用 Issue 之前，建议先创建以下内容：

- [Customer](/erpnext/customer)
- [Email Account](/erpnext/email-account)

## 2. 如何创建 Issue

如果您在 [Email Account](/erpnext/email-account#32-incoming-email-accounts) 中使用 **追加至功能**，Issue 将自动创建。

您也可以手动创建 Issue，具体步骤如下：

- 进入 Issue 列表，点击"新建"。
- 输入 Subject、Raised By 以及 Issue 的描述。

### 2.1 创建 Issue 时的附加选项

**Status**：新建 Issue 时状态为"Open"，回复后状态变为"Replied"。

- Open：Issue 已创建，尚未回复。
- Replied：已向该 Issue 发送回复。
- Hold：Issue 因某种原因处于搁置状态。
- Resolved：当用户确信已为客户提供了问题解决方案，但尚未收到客户关于解决结果的确认时。
- Closed：客户表示对解决方案满意并通过确认表示认可，Issue 已关闭。

如果发送者回复了该对话，状态将再次变为"Open"。用户可以通过点击右上角的 **Close** 按钮手动"关闭"Issue。

> 注意：如果已设置 SLA，则 SLA 的履行状态将在 **Closed** 和 **Resolved** 两种状态下均会更新。

- **Customer**：如果邮件来自存储在 ERPNext 账户中的 [Customer](/erpnext/customer)，则该字段将显示客户链接。

- **Priority**：可根据需要设置优先级。默认有三个优先级——Low、Medium 和 High。您可以根据需要删除或添加更多。

- **Issue Type**：可使用 Issue Type 对 Issue 进行分类。Issue Type 的示例包括：'Functional'、'Technical'、'Hardware' 等。

- **Raised By (Email)**：显示发送 Issue 的电子邮件地址。

## 3. 功能

### 3.1 Details

- **Description**：此文本字段可以查看 Issue 的详细信息。也可以包含图片或表格。

### 3.2 Service Level Agreement

它是服务提供商与终端用户之间的合同，定义了期望从服务提供商获得的服务级别。

用户可以从列表中选择 [Service Level Agreement](/erpnext/service-level-agreement)（SLA）。

- 每个 Issue 都将有一个响应时间和解决时间，Support 团队需在此时间内回复和解决 Issue。
- 可以更改 Priority 来升级 Issue。优先级需要在 Service Level Agreement 中指定。
- 如有需要，可以通过点击 Issue 中的 **Reset Service Level Agreement** 按钮来重置 SLA：

![图片](../../images/286_new-issue.gif)

### 3.3 Response

**Mins to First Response**：从 Issue 创建到首次回复发送的时间（以分钟为单位）。

**First Responded on**：当 Support 团队成员首次回复 Issue 时，将更新首次响应日期和时间。

**Average Response Time**：回复客户的平均时间。这是通过计算所有"收到"与"发送"通信之间时间跨度的平均值得出的。每当向客户发送回复时，此字段都将更新。

![图片](../../images/286_response.png)

### 3.4 Reference

用户可以根据链接到 Issue 的以下字段筛选问题：

- Lead
- Contact
- Email Account
- Project
- Company

### 3.5 Resolution

- **Opening Date**：创建或记录 Issue 时的日期。
- **Opening Time**：创建或记录 Issue 时的具体时间将自动记录。
- **Resolution Date**：当用户解决 Issue 时，日期和时间将在此字段中更新。
- **Resolution Details**：用户可以在 Issue 解决后输入问题的详细信息。这是一个文本字段。用户也可以上传图片、输入或创建表格。
- **Resolution Time**：关闭工单的总时间（从 Issue 创建到关闭）。
- **User Resolution Time**：很多时候，用户需要等待客户的回复才能解决某些 Issue。在衡量用户工作效率时，不应将这段等待时间计算在内。因此，用户解决时间是指用户关闭工单所花费的总时间，计算公式为：

*解决时间 - 用户等待客户回复的总时间*

Resolution Time 和 User Resolution Time 这两个指标在"Close"时设置。当 Issue 重新打开或拆分时，这些指标将自动重置。

![图片](../../images/286_resolution.png)

#### 通过 Customer Portal

如果提出 Issue 的客户是 Website User（无法访问模块），则将勾选此复选框以作标识。

## 4. 保存后

### 4.1 添加评论

Issue 登记后，Support 团队用户可以为该 Issue 添加评论。此字段可编辑。Issue 中的评论仅供内部讨论，不会向客户显示。

### 4.2 新建邮件

用户可以向提出 Issue 的人员发送邮件。所有邮件（收到的和发送的）都可以在 Issue 的对话中查看。

### 4.3 对话线程

Issue 中的邮件讨论线程会保留系统中针对该 Issue 发送和接收的所有邮件，以便您追踪发送者与回复者之间的沟通内容。

- 当您从邮箱发送新邮件时，系统会自动向发送者发送一封包含您的消息和支持工单号的自动回复。
- 发送者可以向该邮件发送补充信息。
- 所有主题中包含此 Issue 编号的后续邮件都将添加到该 Issue 对话线程中。
- 发送者也可以在邮件中添加附件。

### 4.4 分配 Issue 给用户

> Issue 可以使用 [Assignment Rule](/erpnext/assignment-rule) 在用户之间自动分配。

您可以通过点击左侧栏中的"Assign"功能将 Issue 分配给特定用户。这将为该用户添加一个新的 To Do，并向其发送一条消息，告知该 Issue 已被分配。

![图片](../../images/286_issue-assign.png)

### 4.5 关闭

- 您可以通过点击工具栏中的"Close"手动关闭 Issue。
- 如果发送者在 7 天内没有回复，Issue 将自动关闭。

## 5. 相关主题

- [Issue Type and Priority](/erpnext/issue-type-and-priority)