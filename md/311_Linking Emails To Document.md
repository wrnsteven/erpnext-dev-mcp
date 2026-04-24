> v12 新增功能

**一封邮件可以链接到 ERPNext 中的多个文档。**

可以通过以下两种方式实现：

- 在 Contact、Customer、Supplier 中的邮件聚合。

- 自动邮件链接。

- 客户和供应商的邮件聚合

邮件聚合发生在 Contact、Customer 和 Supplier 中。从某个 Contact 发送或接收的所有邮件都可以在该 Contact 的时间线中查看，也可以链接到关联的 Customer 或 Supplier 的时间线中。要启用邮件聚合功能，请执行以下操作：

- 在 Contact 中，分别为 Customer 或 Supplier 添加链接。

![图片](../../images/311_contact-link.png)

2. 当向与 Customer 或 Supplier 关联的 Contact 发送邮件或接收来自该 Contact 的邮件时，该邮件将链接到 Contact 链接部分中提到的 Customer 或 Supplier。
![图片](../../images/311_email_aggregation.gif)

- 自动邮件链接到文档

自动邮件链接功能会将邮件链接到系统为文档生成的唯一电子邮件地址。如果使用该唯一电子邮件地址发送或接收邮件，系统会将该邮件链接到对应的文档。

- 在 Email Account 中启用自动邮件链接功能。此功能一次只能用于一个 Email Account。

![图片](../../images/311_enable_email_link.png)

2. 启用此功能后，您将看到一个使用 Email Account 中填写的电子邮件地址生成的唯一 Email ID。
3. 现在您可以点击复制该 Email ID，并使用这个唯一的 Email ID 发送或接收邮件。如果一封邮件在收件人（TO）或抄送（CC）部分包含此唯一 Email ID，系统将把该邮件链接到指定的文档。
![图片](../../images/311_email_link.gif)

> 注意：不支持使用 BCC 进行邮件链接。您必须将唯一邮箱添加到收件人（TO）或抄送（CC）。

### 3. 相关主题

- [自动邮件报告](/erpnext/auto-email-reports)

- [从任意文档发送邮件](/erpnext/sending-email)

- [文档关注](/erpnext/document-follow)

---
original_url: https://docs.frappe.io/erpnext/linking-emails-to-document
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---