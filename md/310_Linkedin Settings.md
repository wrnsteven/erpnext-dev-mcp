> 注意：此集成已弃用，将在 v15 中移除。

可以在此处配置 LinkedIn 相关设置（如 OAuth）。ERPNext 需要访问 API 来分享帖子，通过 OAuth 2.0 认证协议实现。

- 如何设置 LinkedIn 开发者应用

您必须为您的公司创建 LinkedIn 开发者应用。ERPNext 与此应用交互以分享帖子。

### 1.1 创建 LinkedIn 开发者应用

通过链接 `https://www.linkedin.com/developers` 创建应用，填写所有详细信息并验证。该应用应包含以下产品。

- Share on LinkedIn

- Sign In with LinkedIn

- Marketing Developer Platform ![图片](../../images/310_linkedin-dev-products.png)

### 1.2 配置重定向 URL：

进入 LinkedIn 开发者应用，然后点击 **Auth** 选项卡。

在 **OAuth 2.0 settings** 部分添加 **Redirect URLs**：`https://{yoursite}/api/method/erpnext.crm.doctype.linkedin_settings.linkedin_settings.callback`

点击 **Update** 以保存更改。 ![图片](../../images/310_linkedin-redirect-urls.png)

如何设置 LinkedIn Settings

要访问 LinkedIn Settings，请前往：

> Home > CRM > Settings > LinkedIn Settings

![图片](../../images/310_linkedin-settings.png)

### Company ID

您可以从 LinkedIn 公司 URL 获取 Company ID。 ![图片](../../images/310_linkedin-company-id.png)

### Consumer Key and Consumer Secret

您可以从 LinkedIn 开发者账户获取 **Consumer Key** 和 **Consumer Secret**，请访问：

> `https://www.linkedin.com/developers/` > My Apps > `{Your App}` > Auth

![图片](../../images/310_linkedin-client.png)

填写 **Company ID**、**Consumer Key** 和 **Consumer Secret** 并保存文档后，系统将重定向到 LinkedIn 登录页面。提供有效的 LinkedIn 凭据并点击 Allow（允许）后，成员即批准您的应用程序访问其成员数据并代表其与 LinkedIn 交互。 ![图片](../../images/310_authorize-linkedin.jpg)

---
original_url: https://docs.frappe.io/erpnext/linkedin-settings
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---