## 启用双因素认证（2FA）

通过运行以下命令来激活双因素认证：

`bench --site [sitename] set-config enable_two_factor_auth true`

在系统设置中进行以下配置：

- OTP 验证方式（OTP App = 使用软件或硬件令牌的 TOTP，Email/SMS = 使用邮件或短信的 HOTP）

- 如果指定了 OTP App，需要设置服务器端二维码的有效期

- OTP 签发方名称

![图片](../../images/530_twofactor-1.png)

从设置中启用 2FA 后，"所有用户"角色也会同步启用。这样一来，包括管理员在内的所有用户都需要进行第二级身份验证。通过取消勾选"所有用户"角色中的"双因素认证"选项，并在其他角色中启用它，可以将需要令牌登录的要求限制在特定角色。2FA 不适用于网页用户登录和 API 登录。

![图片](../../images/530_twofactor-2.png)

如果使用短信认证，请确保您的短信设置已更新。

![图片](../../images/530_twofactor-3.png)

如果使用邮件认证，请确保您的发件邮箱设置已更新。

![图片](../../images/530_twofactor-4.png)

当新用户在已启用双因素认证且认证方式为 OTP App 的系统中首次登录时，系统会发送一封包含二维码链接的邮件。

![图片](../../images/530_twofactor-5.png)

![图片](../../images/530_twofactor-6.png)

使用 Google Authenticator 等身份验证应用扫描二维码后，系统会为用户注册访问权限，并自动开始生成可用于登录的令牌。

![图片](../../images/530_twofactor_app.jpeg)

如果使用邮件或短信作为认证方式，您还会收到相应的通知。

![图片](../../images/530_twofactor-8.png)

### 常见问题（FAQ）

问：按照整个流程操作后仍然无法登录。

答：Frappe 使用基于 TOTP 的 OTP 算法，该算法依赖您设备的系统时间。请确保您使用的设备与 ERPNext 服务器设置了相同的时间。

---
original_url: https://docs.frappe.io/erpnext/setup-two-factor-authentication
translated_by: AI (Claude Code)
translation_date: 2026-04-18