**Paytm 集成允许通过支付网关提供商 Paytm 处理交易。**

Paytm 集成方便了 Paytm 支付门户与 ERPNext 之间的支付处理。您的客户可以选择使用任何信用卡/借记卡、UPI、网上银行或 Paytm 钱包进行支付。

要设置 Paytm，请访问：

> 集成与支付 > 支付 > Paytm 设置

## 1.如何获取 Paytm API 凭证？

- 要激活您的 API 凭证，您需要登录您的 Paytm 账户。

- 然后，在侧边栏中打开"开发者设置"选项。

- 选择"API 密钥"选项，它应该显示两种类型的 API 详细信息（测试/生产）。

- 生产 API 详细信息中提到的凭证是您应该在 Paytm 设置中使用的凭证。

![图片](../../images/378_paytm_credentials.png)

## 2.设置 Paytm

要启用 Paytm 支付服务，您需要配置从 Paytm 获取的所有必填参数。如果您想使用集成的预上线环境，可以选择预上线选项并使用 Paytm 提供的测试 API 开发者凭证。

![图片](../../images/378_paytm_settings.png)

在 ERPNext 中启用 Paytm 集成后，系统将创建一个支付网关记录和一个会计科目表中的账户科目，账户类型为银行，如下图所示。

![图片](../../images/378_paytm_coa.png)

此外，它还会创建一个支付网关账户条目。支付网关账户是配置中心，您可以在此处设置账户科目和默认的付款请求邮件模板，用于向客户请求付款。

![图片](../../images/378_payment_gateway_account_paytm.png)

配置支付网关账户后，您将能够通过 Paytm 接收在线付款。

## 3.支持的交易货币

Paytm 仅适用于以 INR（印度卢比）作为公司货币的公司。

---
original_url: https://docs.frappe.io/erpnext/paytm-integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18