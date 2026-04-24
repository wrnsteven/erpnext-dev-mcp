SMTP，即简单邮件传输协议，是一种快速简便的服务器间邮件发送方式。SendGrid 提供 SMTP 服务，允许您通过其服务器而非您的客户端或服务器来发送邮件。ERPNext 内置了已配置的邮件客户端，您可以在 ERPNext 中发送和接收邮件，并在需要时将其附加到文档中。

**集成 SendGrid 的 Web API**

SendGrid 的 SMTP API 允许开发者在邮件中插入 X-SMTPAPI 头，以指定自定义的邮件处理指令。

**步骤 1：** 您需要创建一个 API 密钥来验证您的应用程序（本例中为 ERPNext）。详细了解 SendGrid 与 SMTP API 的集成方式请参阅[此处](https://sendgrid.com/docs/API_Reference/SMTP_API/integrating_with_the_smtp_api.html)

点击 SMTP Relay![图片](../../images/527_Screenshot%202024-06-01%20at%2012.44.17%20PM.png)

生成一个 API 密钥![图片](../../images/527_Screenshot%202024-06-01%20at%2012.44.33%20PM.png)

**步骤 2：** API 密钥创建完成后，您需要在您的 ERPNext 账户中进行配置。创建一个**新的****邮件账户**。

**邮件地址：** *您的邮箱地址*

**服务：** 选择 "*SendGrid*"

勾选 "使用不同的邮箱 ID"

**替代邮箱 ID：** apikey

**密码：** *<步骤 1 中生成的 API 密钥>*

外发服务器：<步骤 1 中生成的服务器名称>

端口：<上述生成的端口号>

![图片](../../images/527_Screenshot%202024-06-01%20at%2012.44.45%20PM.png)

对于 SSL 连接，请取消勾选 "使用 TLS" 选项！![图片](../../images/527_Screenshot%202024-06-01%20at%2012.45.14%20PM.png)

现在**保存**这些信息，您就成功在 ERPNext 中配置好了 SendGrid SMTP 邮件。

为您的能力赋能！

---

original_url: https://docs.frappe.io/erpnext/setting-up-sendgrid-smtp-email-in-erpnext
translated_by: AI (Claude Code)
translation_date: 2026-04-18