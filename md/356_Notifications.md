**您可以在系统中配置各种通知，以提醒您重要的活动。**

- 任务的完成日期。

- 销售订单的预计交货日期。

- 预计付款日期。

- 跟进提醒。

- 收到或发出超过特定金额的订单时。

- 合同的到期通知。

- 任务的完成/状态变更。

要访问通知设置，请前往：

> 首页 > 设置 > 通知

- 设置提醒

要设置通知：

在"发送提醒条件"下定义您要监视的事件。事件包括：

- 新建：当创建所选类型的新文档时。

- 保存/提交/取消：当所选类型的文档被保存、提交或取消时。

- 天数前/天数后：在**参考日期**前几天或几天后触发此提醒。要设置天数，请设置**天数前或后**。这对于提醒您即将到来的到期日期或提醒您跟进某些潜在客户报价非常有用。

- 值变更：当所选类型中的某个特定值发生变化时。

- 方法：当特定方法被触发时发送通知。例如：before_insert。

- 自定义：向选定的[Email Account](/erpnext/email-account)发送通知。

选择要监视变更的文档类型。从版本 16 开始，如果发送提醒条件设置为*天数前*或*天数后*，还可以选择子文档类型。

根据需要设置其他条件。

设置此提醒的收件人。收件人可以是文档的字段或固定电子邮件地址列表。

撰写消息。

保存。

### 1.1 设置主题

您可以使用 `doc.[field_name]` 检索特定字段的数据。要在主题/消息中使用它，必须用 `{% raw %}{{ }}{% endraw %}` 将其包围。这些被称为 [Jinja](http://jinja.pocoo.org/) 标签。例如，要获取文档的名称，您可以使用 `{% raw %}{{ doc.name }}{% endraw %}`。以下示例在保存任务时发送一封电子邮件，主题为"TASK#### has been created"

![图片](../../images/356_email-alert-subject.png)

### 1.2 设置条件

通知允许您根据文档中的字段数据设置条件。例如，如果您希望在潜在客户的状态保存为"感兴趣"时收到一封电子邮件，请在条件文本框中输入 `doc.status == "Interested"`。您还可以通过使用 **and** 或 **or** 运算符组合它们来设置更复杂的条件。

![图片](../../images/356_notification_screenshotb9a4a2.jpg)

上面的示例将在任务保存时发送通知，前提是任务状态为"打开"且任务的"预计结束日期"在保存当天或之前。

### 1.3 设置消息

您可以在消息文本框中使用 Jinja 标签（`{% raw %}{{ doc.[field_name] }}{% endraw %}`）和 HTML 标签。

```
{% raw %}<h3>订单逾期</h3>

交易 {{ doc.name }} 已超过到期日期。请采取必要措施。

{% if comments %} 最后评论：{{ comments[-1].comment }}，由 {{ comments[-1].by }} {% endif %}

<h4>详情</h4>

- 客户：{{ doc.customer }}
- 金额：{{ doc.total_amount }}

{% endraw %}
```

### 1.4 提醒设置后设置属性

有时为了确保通知不会多次发送，您可以（通过自定义表单）定义一个自定义属性（如"通知已发送"），然后通过设置**提醒后设置属性**字段在提醒发送后设置此属性。

然后您可以在**条件**规则中使用它来确保邮件不会多次发送

![图片](../../images/356_email-alert-subject.png)

### 1.5 示例

- 定义标准 ![图片](../../images/356_email-alert-1.png)

- 设置收件人和消息 ![图片](../../images/356_email-alert-2.png)

- Slack 通知

如果您希望将通知发送到专用的 Slack 频道，您还可以在频道选项中选择"Slack"选项，并选择相应的 Slack Webhook URL。

### 2.1 Slack Webhook URL

Slack webhook URL 是指向特定 Slack 频道的 URL。

要生成 webhook URL，您需要创建一个新的 Slack App：

- 访问 https://api.slack.com/slack-apps。

- 点击"创建 Slack App"。 ![图片](../../images/356_slack_notification_1.png)

- 为您的 App 命名并选择正确的工作区。创建应用后，进入"传入 Webhook"部分并添加一个新的 Webhook 到工作区。 ![图片](../../images/356_slack_notification_2.png)

- 复制创建的链接，返回 ERPNext 并用它来在集成 > Slack Webhook URL 中创建新的 Slack Webhook URL。 ![图片](../../images/356_slack_notification_3.png)

- 在通知的频道和 Slack 频道字段中选择 Slack 和您的 Slack 频道

### 2.2 消息格式

与电子邮件不同，Slack 不允许 HTML 格式。

相反，您可以使用 markdown 格式：[Slack 文档](https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages)

示例：{% raw %} *订单逾期*

```
交易 {{ doc.name }} 已超过到期日期。请采取必要措施。

{% if comments %}
最后评论：{{ comments[-1].comment }}，由 {{ comments[-1].by }}
{% endif %}

*详情*

• 客户：{{ doc.customer }}
• 金额：{{ doc.grand_total }}
{% endraw %}

![图片](../../images/356_slack_notification_4.png)

- 系统通知

在**版本 12**中，我们引入了**分配**、**提及**、**文档共享**和**能量点**的系统通知。这些通知显示在导航栏右上角的通知下拉菜单中。

在**版本 13**中，我们引入了一个额外的渠道来发送提醒——**系统通知**：

![图片](../../images/356_system-notifications-channel.png)

选择此渠道将在触发通知时发送系统通知，而不是电子邮件或 Slack 通知。

![图片](../../images/356_system-notification.png)

点击通知会跳转到**通知日志**文档，其中包含配置的主题、消息以及附件（如果设置了附加打印）：

![图片](../../images/356_notification-log.png)

如果同时需要 Email/Slack 提醒和系统通知，可以将主渠道设置为 Email 或 Slack，并勾选此选项：

![图片](../../images/356_send-system-notification.png)

- WhatsApp

在**版本 13**中，我们引入了一个额外的渠道来发送提醒——**WhatsApp**： ![图片](../../images/356_twilio-channel.png)

如果您希望将通知发送到 WhatsApp 号码，您还可以在频道选项中选择"WhatsApp"选项，并选择相应的 Twilio 号码。Twilio 号码可以添加到 Frappe 的 Twilio 设置中。WhatsApp 消息只能发送到包含国家代码的号码。

![图片](../../images/356_twilio-settings.png)

### 4.1 Twilio 设置

要配置 Twilio 设置，您需要首先从 Twilio 账户的账户设置中获取 Twilio 凭证。您只能添加在 Twilio 账户中已激活 WhatsApp 访问权限的电话号码。 ![图片](../../images/356_twilio-credentials.png)

### 4.2 消息格式

WhatsApp 只允许用户向客户发送预先批准的消息模板。否则可能会导致您的 Twilio 账户受到限制。 ![图片](../../images/356_twilio-pre-approved-message.png)

- SMS

在**版本 13**中，我们引入了一个额外的渠道来发送提醒——**短信**： ![图片](../../images/356_sms-notification-channel.png)

要使用此渠道，您需要完成 [短信设置](/erpnext/sms-setting) 的配置。

### 6. 相关主题

- [短信设置](/erpnext/sms-setting)

- [文档关注](/erpnext/document-follow)

### 7. 一次性提醒

> 注意：此功能目前仅在每日构建版本中可用。

由于设置通知是一个相当复杂的过程，Frappe Framework 还提供了一种在文档上设置一次性提醒的方法。此类通知的示例是"4 小时后提醒我跟进这个潜在客户"

要在文档上设置一次性提醒：

- 打开要设置提醒的文档

- 点击菜单（三个点）> "提醒我"

- 选择时间并添加描述，然后点击"创建"

- 系统将在您配置的时间左右向您发送一条系统通知，主题为提醒描述。

---
original_url: https://docs.frappe.io/erpnext/notifications
translated_by: AI (Claude Code)
translation_date: 2026-04-18