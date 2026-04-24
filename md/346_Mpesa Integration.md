**M-Pesa 集成允许通过支付网关提供商 M-Pesa 处理交易。**

M-Pesa 集成促进了 M-Pesa 应用程序与 ERPNext 之间的支付处理。M-Pesa 集成仅与 POS 配合使用，以促进支付。该功能不适用于购物车。

要设置 M-Pesa，请访问：

> 集成 &gt; 支付 &gt; M-Pesa 设置

## 1.如何获取 M-Pesa 凭证？

- 要激活您的 API 凭证，您需要登录您的 M-Pesa 账户。

- 然后，打开应用程序的"Go Live"部分，并按照步骤获取应用程序的审批。

- 当所有测试用例都满足且预期结果与最终结果匹配时，您需要提交文档并按照步骤获取应用程序的最终凭证。

- "Production URL and Credentials"部分中提到的详细信息是您应在 M-Pesa 设置中使用的凭证。

![图片](../images/346_mpesa_credentials.png)

## 2.设置 M-Pesa

要启用 M-Pesa Express，您需要配置从 M-Pesa 收到的所有必需参数。如果您想使用集成的预发布环境，可以选择预发布选项并使用 M-Pesa 提供的预发布凭证（通过为该环境创建一个单独的应用程序）。

![图片](../images/346_mpesa_settings.png)
在 ERPNext 中启用 M-Pesa 集成后，系统将创建一个支付网关记录和一个会计科目，账户类型为银行，如下图所示。

![图片](../images/346_mpesa_coa.png)
![图片](../images/346_mpesa_pos_settings.png)
它还将创建一个同名且账户与支付网关相同的支付方式，以及 POS 设置中的某些自定义字段，用于处理 POS 支付。

![图片](../images/346_payment_gateway_account_mpesa.png)

配置支付网关账户后，您将能够通过 M-Pesa 接受在线支付。

## 3. M-Pesa POS 支付

在使用 M-Pesa 支付方式设置 POS 配置文件后，POS 结账页面将显示一个附加信息部分。该部分包含两个字段，这些字段在添加 M-Pesa 设置时自动设置。

![图片](../images/346_additional-information.png)

一旦 POS 用户填写了客户的手机号码，他们就可以向客户发起支付请求。请求将发送到与指定手机号码关联的客户的 M-Pesa 移动应用程序。用户在处理支付后，系统将提示确认对话框以提交支付。

## 4. M-Pesa 账户余额

可以通过"获取账户余额"按钮获取与个人 M-Pesa 关联的账户余额。这将在仪表板中加载 M-Pesa 账户余额详情。

![图片](../images/346_mpesa_account_balance.png)

## 5.支持的交易货币

M-Pesa 仅适用于以肯尼亚先令（KSH）作为公司货币的公司。

---
original_url: https://docs.frappe.io/erpnext/mpesa-integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---