---
original_url: "https://docs.frappe.io/erpnext/accounts/articles/managing-transactions-in-multiple-currencies"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 管理多币种交易

在 ERPNext 中，交易可以以本位币以及交易方（客户或供应商）的货币创建。如果以交易方货币创建交易，则其货币符号也会在打印格式中更新。

如果您以不同货币向客户报价，您需要更新汇率以使 ERPNext 能够以您的标准货币保存信息。这将帮助您以您的货币分析报价的价值。

让我们以 Sales Invoice 为例，其中您的本位币是 USD，交易方货币是 EUR。

1. 创建新的 Sales Invoice: **Home > Accounting > Billing > Sales Invoice > New**。

2. 从客户主数据中选择客户。如果在客户主数据中更新了默认货币，将在此处获取。

3. 本位币和客户货币之间的汇率会自动获取。

4. 更新其他详细信息，如项目、税费、条款。在税费和其他费用表中，类型为"实际"的费用应以客户货币更新。

5. 保存 Sales Invoice，然后检查打印格式。所有货币字段（汇率、金额、总计）都将显示客户货币符号。

## 货币兑换主数据

如果您已与交易方达成协议，可以遵循标准汇率，您可以通过创建货币兑换主数据来获取它。要创建，请前往：

> Home > Accounting > Settings > Currency Exchange

在 ERPNext 中，会获取实时汇率。

**注意**：如果您创建了具有特定汇率的货币兑换主数据，将优先于实时汇率。例如，如果您在货币兑换中设置 $1 = ₹65，即使实时汇率为 ₹69，也将在交易中使用 ₹65。
