---
original_url: https://docs.frappe.io/erpnext/erpnext_shipping
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

# ERPNext Shipping

版本 13 中引入

ERPNext Shipping 应用帮助您比较多家服务提供商提供的运费、生成标签并跟踪货运状态。

可与以下服务提供商集成：

- [LetMeShip](https://www.letmeship.com/en/)

- [SendCloud](https://www.sendcloud.com)

要使用这些功能，必须在您的站点上安装 ERPNext Shipping 应用。您可以从 [GitHub](https://github.com/frappe/erpnext-shipping/tree/master)、[Frappe Cloud Marketplace](https://cloud.frappe.io/marketplace/apps/erpnext_shipping) 获取该应用，或联系您的主机平台。

## 设置

为了让应用顺利工作，您需要从上面列出的至少一个平台生成 API 密钥。以下是设置指南：

### 1.1 SendCloud

- 在 [SendCloud](https://panel.sendcloud.sc/accounts/signup/) 注册。

- 按照[这些步骤](https://support.sendcloud.com/hc/en-us/articles/360024967612-Service-points-for-API-Integrations#step-1-) 生成 Public Key 和 Secret Key。

- 在 awesomebar 中搜索 SendCloud。

- 将 Public Key 添加到 SendCloud DocType 的"API Key"字段，将 Secret Key 添加到"API Secret"字段。

- 勾选"启用"字段。

- 保存。

![Sendcloud API](images/215_sendcloud_api.png)

### 1.2 LetMeShip

- 在 [LetMeShip](https://www.letmeship.com/en/) 注册。

- 按照[这些步骤](https://www.letmeship.com/en-de/shipping-api/) 生成 API ID 和 API Password。

- 在 awesomebar 中搜索 LetMeShip。

- 将 API ID 和 API Password 添加到 LetMeShip DocType。勾选"启用"字段。

- 保存。

![LetMeShip API](images/215_letmeship_api.png)

## 功能

### 2.1 运费比较

提交[货运单](/erpnext/shipment)后，如果已安装应用，将出现"获取运费"按钮。点击后，您将看到服务列表及其服务提供商和费率。

![获取费率](images/215_fetch_rates.png)

您还可以使用包裹服务类型将常用服务添加到您的首选服务中：

- 假设高亮显示的服务是我们的常用服务，让我们将其添加到首选服务中

![高亮服务](images/215_service_highlight.png)

2. 进入包裹服务类型 > 新建。创建新的包裹服务。在我们的例子中，它是"TNT"。
3. 添加包裹服务类型。在我们的例子中，它将是"经济"。
4. 将"经济"也添加到包裹服务类型别名表中。
5. 添加描述（可选）。
6. 启用"显示在首选服务列表中"字段。保存。

现在当您点击"获取运费"按钮时，您将始终在首选服务下看到之前高亮显示的服务。

![首选服务](images/215_preferred_service.png)

### 2.2 创建货运单

比较费率后，您可以通过点击相应服务行中的"选择"来选择任何服务继续。点击后，货运单将在您的服务提供商平台上自动创建。

您会注意到货运信息部分会根据创建的货运自动更新。

![创建货运单](images/215_create_shipment.gif)

您还可以使用货运 ID 字段在服务提供商平台上搜索您的交易。

### 2.3 打印标签

要使用"打印货运标签"按钮，必须在当前记录中生成货运 ID。

![打印标签按钮](images/215_print_label_button.png)

然后您可以点击它生成货运标签。

![虚拟货运标签](images/215_dummy_shipping_label.png)

您还可以通过点击"查看" > "跟踪状态"来跟踪货运状态。

注意：当前集成的平台可能无法为您的地区服务。请访问附加的链接了解更多。