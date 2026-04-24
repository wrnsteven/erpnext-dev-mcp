```
---
original_url: https://docs.frappe.io/erpnext/paypal-integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---
```

支付网关是一种电子商务应用服务提供商服务，用于授权信用卡支付，适用于电子商务企业、在线零售商、线上线下融合零售商或传统实体店。

支付网关促进支付门户（如网站、手机或交互式语音应答服务）与前端处理器或收单银行之间的信息传输。

要设置 PayPal，请访问
`Explore > Integrations > PayPal Settings`

#### 设置 PayPal

要启用 PayPal 支付服务，您需要配置 API 用户名、API 密码和签名等参数。

![图片](../../images/377_paypal_settings.png)

您还可以通过设置 **Use Sandbox** 来配置测试支付环境。

启用服务后，系统将创建 Payment Gateway 记录和在科目表中创建账户头，该账户类型为银行。

![图片](../../images/377_paypal_coa.png)

同时还会创建 Payment Gateway Account 条目。Payment Gateway Account 是配置中心，您可以从中设置现有科目表中的账户头、默认 Payment Request 邮件模板。

![图片](../../images/377_payment_gateway_account_paypal.png)

启用服务并配置 Payment Gateway Account 后，您的系统即可接受在线支付。

#### 支持的交易货币

AUD, BRL, CAD, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, TRY, USD

## 获取 PayPal 凭据

#### PayPal Sandbox API 签名

登录到 PayPal 开发者账户，[PayPal Developer Account](https://developer.paypal.com/)

在 **Accounts** 选项卡中，创建一个新的企业账户。

![图片](../../images/377_setup-sanbox-1.png)

从该账户的个人资料中获取您的沙盒 API 凭据

![图片](../../images/377_sanbox-credentials.png)

#### PayPal 账户 API 签名

登录 PayPal 账户并进入个人资料

![图片](../../images/377_api-step-1.png)

在 **My Selling Tools** 中进入 **API Access**

![图片](../../images/377_api-step-2.png)

在 API Access 页面，选择选项 2 来生成 API 凭据

![图片](../../images/377_api-step-3.png)