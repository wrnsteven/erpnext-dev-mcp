---
original_url: "https://docs.frappe.io/erpnext/address"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 地址

您可以记录与潜在客户、客户、供应商、股东、销售合作伙伴或仓库关联的地址。

您也可以将地址作为独立记录添加，而不链接到上述任何实体。

要访问地址列表，请前往:

> Home > CRM > Address

## 如何创建地址

1. 转到地址列表，点击"新建"。
2. 选择地址类型。
3. 在地址行1、地址行2、城市/城镇、县、省/州、国家中输入详细信息。
4. 输入电子邮件地址、电话和传真。
5. 输入链接 DocType 和链接名称，将此地址链接到客户、供应商等。
6. 保存。联系人

您也可以通过单击 Customer 或 Supplier 记录中的"新建地址"按钮来添加地址，如下所示。

<img src="/images/25_imagea26d72.png" alt="" />

要从电子表格导入多个地址，请使用数据导入工具。

## 功能

### 将地址链接到多个实体

一个地址可以链接到多个客户或多个供应商。

地址也可以同时链接到客户和供应商。

<img src="/images/25_image48b1ed.png" alt="" />

### 地址标题

如果地址未链接到任何实体，您需要手动添加标题。

如果地址链接到客户或供应商等实体，标题会自动以"实体名称-地址类型"格式生成。

<img src="/images/25_Address%20Billing.png" alt="" />

### 首选收货地址和发货地址

如果您勾选"首选发货地址"，该地址将自动添加到 Sales Order、Sales Invoice 和 Delivery Note 交易的发货地址中。

同样，如果您勾选"首选账单地址"，该地址将自动添加到 Sales Order、Sales Invoice 和 Delivery Note 交易的账单地址中。

### 印度 GST 本地化

如果客户或供应商已注册 GST，您可以在地址中输入 GSTIN 和 GST 州。请确保输入的 GSTIN 格式有效。

<img src="/images/25_gst-details-in-address.png" alt="GST Details in Address" />

在销售交易中，连同地址一起获取 GSTIN。

<img src="/images/25_imageefea37.png" alt="" />

您也可以添加自己公司设施的地址。勾选"是我公司地址"，在链接 DocType 中选择公司，在链接名称中选择此类地址的公司名称，您可以在 GST Sales Invoice 中选择它们来打印您自己的地址。

<img src="/images/25_imagedfad7a.png" alt="" />

> GSTIN 应添加到地址中，而不是客户/供应商中，因为一个客户/供应商可能有多个 GSTIN（每个开展业务的州一个）。

### 相关主题

1. Customer
2. Supplier
3. Sales Partner