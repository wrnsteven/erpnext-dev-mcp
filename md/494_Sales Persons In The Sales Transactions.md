在ERPNext中，Sales Person主数据以[树形结构](/erpnext/managing-tree-structure-masters.html)维护。Sales Person可在所有销售交易中进行选择。

Sales Persons也可以在Customer主数据中进行更新。在交易中选择Customer时，Customer中更新的Sales Persons会自动带入到销售交易中。

![图片](../../images/494_sales-person-in-customer.png)

####Sales Person贡献

如果多个Sales Persons共同参与一个订单，则需要为每个Sales Person设置贡献百分比。

![图片](../../images/494_sales-person-in-sales-order.png)

保存交易时，系统会根据净总额和贡献百分比，为每个Sales Person计算"Contribution to Net Total"。

所有Sales Person的贡献百分比总和必须为100%。如果仅选择一个Sales Person，则贡献百分比将为100。

####Sales Person交易报告

查看Sales Person的交易报告：

`Selling > Standard Reports > Sales Person-wise Transaction Summary`

此报告可基于Sales Order、Delivery Note和Sales Invoice生成。它会显示员工的总销售额。

![图片](../../images/494_sales-person-wise-transaction-summary-report.png)

####Sales Person佣金

ERPNext仅提供Sales Person的销售总额。如果您需要向Sales Person支付佣金，应在ERPNext中将Sales Person添加为Sales Partners。对于Sales Partners，您可以定义佣金百分比。在销售交易中选择Sales Partner后，系统会根据净总额自动计算佣金金额。您可以查看Sales Partner的佣金报告：

`Accounts > Standard Reports > Sales Partners Commission`

---
original_url: https://docs.frappe.io/erpnext/sales-persons-in-the-sales-transactions
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---