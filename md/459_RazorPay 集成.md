# RazorPay 集成

支付网关是一种电子商务应用服务，为电商企业、在线零售商、线上线下融合商户或传统实体店提供信用卡支付授权服务。

支付网关促进支付门户（如网站、手机或交互式语音应答服务）与前端处理器或收单银行之间的信息传输。

## 设置 RazorPay

> **Explore &gt; Integrations &gt; RazorPay Settings**

![图片](../../images/459_razorpay-api.gif)

#### 配置 RazorPay

要启用 RazorPay 支付服务，需要配置 API Key、API Secret 等参数。

![图片](../../images/459_razorpay_settings.png)

启用服务后，系统将创建支付网关记录，并在科目表中创建账户头（账户类型为银行）。

![图片](../../images/459_razorpay_coa.png)

同时，系统还会创建 Payment Gateway Account 条目。Payment Gateway Account 是配置中心，您可以从中设置现有科目表中的账户头、默认 Payment Request 邮件模板等。

![图片](../../images/459_payment_gateway_account_razorpay.png)

启用服务并配置 Payment Gateway Account 后，您的系统即可接受在线支付。

#### 支持的交易货币

RazorPay 仅适用于以 `INR (Indian Rupee)` 为货币的公司。

---

original_url: https://docs.frappe.io/erpnext/razorpay-integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18