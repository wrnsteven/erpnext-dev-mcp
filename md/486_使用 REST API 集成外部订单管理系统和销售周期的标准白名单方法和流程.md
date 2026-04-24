# 使用 REST API 集成外部订单管理系统和销售周期的标准白名单方法和流程

## 1. 销售订单

Frappe Framework 为所有 DocType 开箱即用地生成 REST API。此方法可用于创建销售周期的第一个文档。如果您从销售订单开始，可以使用标准 REST API POST 请求来生成订单。如下所示的示例，您可以在请求体中相应地包含自定义字段和其他 doctype 详细信息。

POST /api/resource/Sales Order

# Body

```json
{
 "doctype": "Sales Order",
 "customer": "Test Customer",
 "company_address": "Test - Billing",
 "customer_address": "Test-Billing-3",
 "items": [{
  "item_code": "Mobile Display",
  "qty": 10,
  "rate": 2000,
  "delivery_date": "2022-11-06",
  "delivery_warehouse": "Stores - GTPL"
 }]
}
```

## 2. 交货单

如果您从交货单开始，请使用与上述销售订单相同的方法，只需将 doctype 键值替换为 **Delivery Note** 而不是 **Sales Order**。如果您想从销售订单创建交货单，请使用以下端点。这里的 `source_name` 参数是销售订单 ID。

POST /api/method/erpnext.selling.doctype.sales_order.sales_order.make_delivery_note

# Body

```json
{"source_name": "SO-2022-00001"}
```

该端点返回一个包含订单中所有待交货项目的交货单 JSON 对象。

## 3. 销售发票

同样，如果您只是创建销售发票，最佳方法是使用标准 REST API。为此，请参阅销售订单部分中提到的示例。

要从销售订单创建销售发票，请使用以下端点。这里的 `source_name` 参数是销售订单 ID。

POST /api/method/erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice

# Body

```json
{"source_name": "SO-2022-00001"}
```

要从交货单创建销售发票，请使用以下端点。这里的 `source_name` 参数是交货单 ID。

POST /api/method/erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice

# Body

```json
{"source_name": "SO-2022-00001"}
```

两个端点都返回一个包含所有待开票项目的销售发票 JSON 对象。

## 4. 订单或发票付款

要生成针对销售订单或发票的付款条目，请使用以下端点

POST /api/method/erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry

# Body

```json
{
 "dt": "Sales Invoice",
 "dn": "SI-2022-0001",
 "party_amount": 2000, # 如果文档没有 `outstanding_amount` 字段则传递（可选参数）
 "bank_account": "Bank Name - CAB", # 如需使用非默认账户则传递（可选参数）
 "bank_amount": 2000, # 根据付款条目类型为已付或已收金额（可选参数）
 "party_type": "Customer", # 如果付款条目针对 Customer 或 Supplier 以外的当事方类型（可选参数）
 "payment_type": "Pay", # 付款或收款（可选参数）
}
```

---

original_url: https://docs.frappe.io/erpnext/sales-integration

translated_by: AI (Claude Code)

translation_date: 2026-04-18