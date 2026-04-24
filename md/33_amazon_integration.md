---
original_url: "https://docs.frappe.io/erpnext/amazon-integration"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# Amazon SP-API 集成

Amazon Connector 从 Amazon  marketplace 拉取产品和销售订单。

## 如何设置 Amazon SP-API Connector？

Amazon Connector 已从 ERPNext 中移除，可通过 <a href="https://frappecloud.com/marketplace/apps/ecommerce_integrations">Frappe Cloud Marketplace</a> 上的 Frappe App 获取。

### App 安装

- 如果您在 Frappe Cloud 上托管您的 ERPNext 站点，您可以通过转到站点仪表板快速安装该 app。该 app 可在 <a href="https://frappecloud.com/marketplace/apps/ecommerce_integrations">Frappe Cloud Marketplace</a> 获取
- 如果您的站点由 Frappe 托管，请提交支持工单以在您的站点上安装 app。
- 如果您是自托管 ERPNext，您可以使用 Frappe bench 安装 app。有关安装 Frappe Apps 的信息，请参阅 <a href="https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation">bench 文档</a>。<code>bench get-app ecommerce_integrations --branch main</code>

该 app 的仓库托管在 GitHub 上：http://github.com/frappe/ecommerce_integrations/

### 在 ERPNext 中设置凭据

一旦您成为其网站的注册卖家，您可以从 Amazon Seller Central 请求开发者凭据。有关详细信息，请点击<a href="https://developer.amazonservices.com/">此处</a>。

#### 1. 设置 SP-API 凭据

输入 IAM ARN、Refresh Token、Client ID、Client Secret、AWS Access Key、AWS Secret Key 和 Country。 <img src="/images/33_Credentials.png" alt="Credentials" title="Credentials.png" />

#### 2. 设置订单详情

设置 Company、Warehouse、Parent Item Group、Price List、Customer Group、Territory、Customer Type 和 Account Group。Account Group 用于存放 Amazon 收取的佣金、税费等。 <img src="/images/33_Screenshot%20from%202023-07-31%2013-51-36.png" alt="setup" title="setup.png" />

#### 3. 设置同步配置

使用 After Date，您可以同步在特定日期之后创建的订单。如果您要导入大量历史数据，建议以 After Date 的倒序开始，并小批量导入数据。 <img src="/images/33_Screenshot%20from%202023-07-31%2013-45-15.png" alt="Syncing" title="Syncing.png" />设置完所有配置后，点击 Is Active 并保存设置。您现在可以开始使用该集成了。

#### 4. Amazon - ERPNext 物料映射

ASIN 和 SellerSKU 都可用于将 Amazon 物料与相应的 ERPNext 物料进行映射。例如，如果您的系统中存在通过其他集成预先创建的物料，您可以使用自定义表单功能在 Item Master 中创建自定义字段，并将 ASIN/SellerSKU 设置为值。

在从 Amazon 同步订单的过程中，系统将尝试使用配置为在 Amazon - ERPNext 物料映射表中查找物料代码的字段来查找物料代码。如果在映射表中找不到物料，您可以通过勾选 <strong>Create Item If Not Exists</strong> 框来创建新物料。

<img src="/images/33_Screenshot%20from%202023-07-31%2013-52-50.png" alt="Screenshot from 2023-07-31 13-52-50" title="Screenshot from 2023-07-31 13-52-50.png" />

#### 5. 同步订单

点击此按钮同步销售订单。成功后，您应该可以在 ERPNext 中将 Amazon 订单作为销售订单看到。您还可以设置调度程序来自动同步订单。

> 如果您的开发者账户无法访问个人身份信息，客户名称将存储为 BuyerName + <Order ID> 或 Marketplace email ID 的组合。

<img src="/images/33_Sales%20Order.png" alt="Sales Order" title="Sales Order.png" />

### 注意

连接器不会处理订单取消。如果您在 Amazon 中取消任何订单，那么您必须在 ERPNext 中手动取消相应的 Sales Order 和其他文档。
