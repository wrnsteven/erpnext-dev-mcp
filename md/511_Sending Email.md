在 ERPNext 中，打开任何单据后，点击菜单 > 邮件，即可将该单据作为邮件（附带 PDF 附件）进行发送。

![图片](../../images/511_send-email.gif)

**注意：** 为此您必须已设置好发件 [Email Account](/erpnext/email-account)。

点击发送后，邮件会被添加到邮件队列中。在发送完成之前，它将处于"发送中"状态。邮件状态会在队列中显示，如果发送失败，可以点击"立即发送"重新发送。

![图片](../../images/511_email-queue.png)

发送邮件时可以使用以下选项：

- **收件人：** 邮件的接收者。

- **发件人：** 如果用户有多个发件 Email Account，可以选择使用哪个发件 Email Account。可以在用户文档的"用户邮件"表中添加多个发件 Email Account。

- **抄送：** 邮件的抄送副本。当您希望让某人了解对话内容但不想直接将邮件发送给他们时，此功能非常有用。

- **密送：** 密送与抄送类似，但邮件线程中的其他收件人看不到该邮件也已发送给密送收件人。当您需要向很多不一定相互认识的人发送邮件时，可用于隐藏某些人的邮件地址。

- **邮件模板：** 您可以创建预设模板来发送标准回复。系统中已有调度通知、休假状态通知和休假审批通知的邮件模板。您可以通过[自定义表单](/erpnext/customize-form)设置默认邮件模板。

- **发送副本给我：** 邮件的副本将发送到您的邮件地址。这有助于确保邮件已正常发送。

- **发送已读回执：** 勾选此复选框后，当收件人阅读邮件时，您将收到通知。如果有多个收件人，只要其中一人已阅读邮件，您就会收到通知。

- **附加文档打印件：** 将您发送的文档的 PDF 附加到邮件中。

- **选择附件：** 可以在这里添加任何其他附件。

以下两个字段是打印界面上显示的字段：

![图片](../../images/511_email-print-options.png)

- **选择打印格式：** 文档的打印格式。了解更多关于打印格式的信息，请参阅[此处](/erpnext/print-format)。

- **选择语言：** 生成 PDF 所使用的语言。

### 相关主题

- [Email Domain](/erpnext/email-domain)

- [Email Account](/erpnext/email-account)

- [Email Inbox](/erpnext/email-inbox)

---
original_url: https://docs.frappe.io/erpnext/sending-email
translated_by: AI (Claude Code)
translation_date: 2026-04-18