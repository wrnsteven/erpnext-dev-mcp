---
original_url: "https://docs.frappe.io/erpnext/address-template"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 地址模板

<strong>地址模板可以存储基于不同地区的地址格式。</strong>

每个地区都有其特定的地址定义方式。要管理文档（如报价单、采购发票等）的多种地址格式，您可以创建针对不同国家的<strong>地址模板</strong>。

要访问地址模板，请前往：

> CRM > Address Template

在设置系统时会创建一个默认地址模板。您可以编辑它或创建新模板。此默认模板将适用于所有没有特定模板的国家。

考虑一位来自美国的客户，其地址中包含"County"。如果您在美国地址模板中设置了县，那么它将显示在地址字段中，从而显示在打印预览中。像 PIN code 这样的字段可以更改为 ZIP code 显示，像县这样的字段可以通过地址模板添加。

地址模板会根据地址主数据中的"Country"字段，将不同的地址模板应用到交易中。

1. 如何创建地址模板

<hr />

1. 转到地址模板列表，点击"Add Address Template"。
2. 选择一个国家。
3. 根据需要修改 CSS 和 Jinja。
4. 如果它将成为系统中的默认地址模板，请标记为默认。
5. 保存。

<img src="/images/26_Screenshot%202024-05-23%20at%204.29.42%20PM.png" alt="Screenshot 2024-05-23 at 4.29.42 PM" />

注意：模板引擎基于 HTML 和 <a href="https://jinja.palletsprojects.com/">Jinja</a> 系统。所有字段（包括自定义字段）都可用于创建模板。

### 2. 相关主题

1. <a href="/erpnext/terms-and-conditions">Terms and Conditions Template</a>
2. <a href="/erpnext/cheque-print-template">Cheque Print Template</a>
