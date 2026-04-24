**Item Tax Template 用于按项目设置税务。**

如果某些物料的税率与"税费及费用"表中指定的标准税率不同，您可以创建 Item Tax Template 并将其分配给[物料](/erpnext/item)或[物料组](/erpnext/item-group)。Item Tax Template 中指定的税率将优先于"税费及费用"表中指定的标准税率。

例如，如果在销售订单的"税费及费用"表中添加了 18% 的 GST，则该销售订单中的所有项目都将适用该税率。但是，如果您需要对某些项目应用不同的税率，请按照以下步骤操作。

要访问 Item Tax Template 列表，请转到：

> 首页 > 会计 > 税费 > Item Tax Template

让我们假设您正在创建一份销售订单。我们已创建了 GST 9% 的[销售税费及费用模板](/erpnext/sales-taxes-and-charges-template)。在所有销售项目中，其中一个项目仅适用 5% 的 GST，而另一个项目则免税（非应税项目）。您需要选择税费的核算科目并设置覆盖税率。

## 1. 先决条件

在创建和使用 Item Tax Template 之前，建议先创建以下内容：

- [物料](/erpnext/item)

- 在[账户设置](/erpnext/accounts-settings)中启用"自动从 Item Tax Template 添加税费及费用"

## 2. 如何创建 Item Tax Template

- 进入 Item Tax Template 列表，点击"新建"。

- 输入 Item Tax Template 的名称。

- 选择一个核算科目并设置覆盖税率。如有需要，可添加更多行。

- 保存。

现在 Item Tax Template 已准备就绪，可以分配给物料。要进行此操作，请进入物料的"Item Tax"部分，选择一个 Item Tax Template：

![图片](../../images/296_item-tax-in-item.png)

> 注意：建议不要在此处选择的[税费规则](/erpnext/tax-rule)中使用销售/采购模板，这可能会造成干扰。如果您希望为税费规则和 Item Tax Template 使用相同的税率，请使用不同的名称来命名销售/采购税费模板。

### 2.1 在物料主数据中指定适用税率

税费模板预设了税率值。对于税率与其他项目不同的项目，您需要在物料主数据中进行更改。进入物料的税费表，添加一行，选择税费类型并更改税率。现在，在创建订单/发票时，新税率将覆盖模板。例如，在下面的截图中，您可以看到税率设置为 5，这就是将在交易中应用的税率。

![图片](../../images/296_item-wise-tax.png)

对于完全免税的物料，请在物料主数据中将税率指定为 0%。

![图片](../../images/296_tax-exempted-item.png)

> 注意：要使 Item Tax Template 生效，您需要确保在 Item Tax Template 中设置的税费类型（账户）（已更改的税率）存在于销售税费及费用模板中。

> 如果您想包含具有不同税率的多个物料，需要将它们记录在不同的税费科目下。例如，VAT 14%、VAT 5% 等。

### 2.2 交易中的税费计算

在报价单、销售订单和销售发票等销售交易中，项目的税费按所选的销售税费及费用模板计算。但是，如果某些项目关联了 Item Tax Template，则这些项目的税费将按照 Item Tax Template 中指定的税率计算，而不是按照销售税费及费用模板中指定的税率计算。

例如，在下面的截图中，您可以看到税费按 3% 计算，即使销售税费及费用模板中的税率是 6.25%。

![图片](../../images/296_tax-calculation.png)

### 2.3 每个项目的 Item Tax Template

您也可以在交易中为每个项目手动选择不同的 Item Tax Template：

![图片](../../images/296_select-item-tax-template.png)

### 2.4 物料组级别的按项目计税

您可以通过在物料组文档内的 Item Tax 部分修改 Item Tax 表，为物料组分配 Item Tax Template。

![图片](../../images/296_item-tax-template-in-item-group.png)

应用于物料组的 Item Tax Template 将适用于该组中的所有物料，除非该物料组中的单个物料已分配了自己的 Item Tax Template。

### 2.5 物料税的有效期

![图片](../../images/296_item-tax-in-item.png)

您也可以为税费模板指定有效期，如上图所示。

- 根据交易的过账日期，系统将自动获取有效的税费模板。

- 如果有多个有效的税费模板，则将获取 Item Tax 表中第一个有效的税费模板。

- 如果没有有效的税费模板，则将获取 Item Tax 表中没有"生效日期"的第一个税费模板。

> 注意：在采购发票中添加项目时，将优先使用"供应商发票日期"而不是"过账日期"来获取有效的 Item Tax Template。

### 2.6 注意事项

如果将税费类别设置为空，则默认的 Item Tax Template 将应用于交易中的物料。

您可以为不同的税费类别应用不同的 Item Tax Template。

要使 Item Tax Template 覆盖税费，"税费及费用"表中必须有一行具有相同税费核算科目和标准税率。

如果您希望仅对具有 Item Tax Template 的物料应用税费，则可以将标准税率设置为 0。

### 3. 相关主题

- [税费规则](/erpnext/tax-rule)

- [销售发票](/erpnext/sales-invoice)

- [采购发票](/erpnext/purchase-invoice)

---
original_url: https://docs.frappe.io/erpnext/item-tax-template
translated_by: AI (Claude Code)
translation_date: 2026-04-18