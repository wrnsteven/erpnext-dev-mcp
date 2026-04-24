---
original_url: https://docs.frappe.io/erpnext/purchase-taxes-and-charges-template
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

**购买税费及附加费可应用于您购买的任何商品。**

Purchase Taxes and Charges Template 与 Sales Taxes and Charges Template 类似。通过此表单创建的模板可用于 Purchase Orders 和 Purchase Invoices 的内部记录。

对于您想在税费模板中使用的税务科目，必须将该科目的 Account Type 字段设置为"Tax"。

访问 Purchase Taxes and Charges Template 的路径：

> Home > Buying > Settings > Purchase Taxes and Charges Template

## 1. 如何通过模板添加 Purchase Taxes/Charges

在创建新模板之前，请注意许多常用税费已预先创建了模板。

- 点击"新建"。

- 输入税费的标题名称。

- 在类型下，设置税费的计算方式及税率。类型下有五个选项用于确定税费的计算方式。

- **Actual**：基于每个商品的实际金额。

- **On Net Total**：基于所有商品的合计金额。

- **On Previous Row Amount**：用于复合计费。例如，在上一行已计税的金额基础上征收附加费。

- **On Previous Row Total**：与上述相同，但基于总账单计算，而非单个商品的金额。

- 选择已预设税率的账户科目或创建您自己的科目。

- 选择"default"后，该模板将自动应用于新的 Purchase 交易。

保存。
![图片](../../images/440_purchase-taxes.png)

**Is Inter State**：适用于印度。在 Sales Invoice 或 Delivery Note 中选择客户时，如果供应地点的 GST 代码与客户收货地址不匹配，则将自动设置勾选了"Is Inter State"的模板作为税费模板。如果供应地点和收货地址相同，则应用默认税费模板。这也适用于 Purchase Invoice，在选择 Supplier 时，模板的设置取决于地址。例如 IGST。

## 2. 功能

### 2.1 Purchase Taxes and Charges 表格

**Consider Tax or Charge for**：Total - 对所有商品合计计算。Valuation - 对每个商品分别计算。Valuation and total - 同时应用税费/附加费。[查看这篇文章](https://docs.erpnext.com/docs/v13/user/manual/en/accounts/articles/difference-in-total-and-valuation-in-tax-and-charges)了解 Total 和 Valuation 之间的区别。

**Add or Deduct**：是否要从商品中添加或扣除税费。

**Reference Row #**：如果税费基于"Previous Row Total"，您可以选择行号作为此计算的基准（默认为上一行）。
![图片](../../images/440_purchase-taxes-table.png)

**Is this Tax included in Basic Rate?**：如果勾选，税费金额将被视为已包含在 Print Rate / Print Amount 中。

**Account Head**：该税费将记账的账户分类账。如果您选择 VAT 或任何其他预设科目，税率将自动填充。

**Cost Center**：如果税费/附加费是收入（如运费）或支出，需要针对某个 Cost Center 记账。

**Description**：税费的描述（将打印在发票/报价单上）。

**Rate**：税率，例如：14 = 14% 税费。

**Amount**：要应用的税费金额，例如：100.00 = ₹100 税费。

### 3. 相关主题

- [Purchase Order](/erpnext/purchase-order)

- [Buying Settings](/erpnext/buying-settings)