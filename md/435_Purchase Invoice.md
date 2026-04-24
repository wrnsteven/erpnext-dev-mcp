**Purchase Invoice 是您从供应商处收到的账单，您需要根据该账单进行付款。**

Purchase Invoice 与 Sales Invoice 完全相反。在此处，您将费用应计给供应商。创建 Purchase Invoice 与创建 Purchase Order 非常相似。

要访问 Purchase Invoice 列表，请前往：

> 首页 > 会计 > 应付账款 > Purchase Invoice

![图片](../../images/435_pi-flow.png)

### 前提条件

在创建和使用 Purchase Invoice 之前，建议首先创建以下内容：

- [Item](/erpnext/item)
- [Supplier](/erpnext/supplier)
- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)（可选）

### 如何创建 Purchase Invoice

Purchase Invoice 通常从 Purchase Order 或 Purchase Receipt 创建。供应商的物料详情将被获取到 Purchase Invoice 中。但是，您也可以直接创建 Purchase Invoice。

要自动获取 Purchase Invoice 中的详情，请点击 **Get Items from**。可以从 Purchase Order 或 Purchase Receipt 获取详情。

手动创建请按以下步骤操作：

- 进入 Purchase Invoice 列表，点击新建。
- 选择供应商。
- 过账日期和时间将设置为当前时间，您可以勾选"过账时间"下的复选框后进行编辑。
- 设置付款到期日。
- 在物料表中添加物料和数量。
- 税率和金额将被自动获取。
- 保存并提交。

![图片](../../images/435_截图_2026-01-19_下午_12.37.15.png)

### 2.1 创建 Purchase Invoice 时的其他选项

- **Is Paid（已付款）**：如果已通过[预付款单据](/erpnext/advance-payment-entry)支付了款项，您可以勾选"已付款"。如果有全部或部分付款，应勾选此项。

- **Is Return (Debit Note)（退货（借项通知单））**：如果客户已退货，请勾选此项。了解更多详情，请访问[借项通知单](/erpnext/debit-note)页面。

- **Apply Tax Withholding Amount（适用预扣税金额）**：如果所选供应商设置了预扣税类别，此复选框将启用。更多信息，请访问[预扣税类别](/erpnext/tax-withholding-category)页面。

### 2.2 状态

- **Draft（草稿）**：已保存但尚未提交到系统。
- **Return（退货）**：物料已退还给供应商。
- **Debit Note Issued（已开具借项通知单）**：物料已退回，并已针对该发票开具了[借项通知单](/erpnext/debit-note)。
- **Submitted（已提交）**：Purchase Invoice 已提交到系统，分类账已更新。
- **Paid（已付款）**：供应商已全额收到发票款项，相应的[付款单据](/erpnext/payment-entry)已提交。
- **Partly Paid（部分付款）**：供应商已收到部分发票款项，相应的[付款单据](/erpnext/payment-entry)已提交。
- **Unpaid（未付款）**：Purchase Invoice 尚未付款。
- **Overdue（逾期）**：付款到期日已过。
- **Canceled（已取消）**：发票因某种原因被取消。

### 功能

### 3.1 会计维度

会计维度让您能够根据特定区域、分支、客户等标记交易。这有助于根据所选标准分别查看会计报表。了解更多，请访问[会计维度](/erpnext/accounting-dimensions)页面。

> 注意：项目和成本中心默认被视为维度。

### 3.2 挂起发票

有时您可能需要将发票挂起以防止提交。

**Hold Invoice（挂起发票）**：启用此复选框可将 Purchase Invoice 置于挂起状态。这只能在提交发票之前完成。一旦启用了"挂起发票"并且 Purchase Invoice 被提交，状态将变为"临时挂起"。

![图片](../../images/435_截图_2026-01-19_下午_12.38.23.png)

一旦采购发票被提交，如果您想更改"释放日期"，可以使用右上角提供的"挂起发票"按钮。

如果您想挂起已提交的采购发票，可以使用"阻止发票"选项；如果想再次解除阻止，请使用"解除阻止发票"选项。

![图片](../../images/435_截图_2026-01-19_下午_12.39.12.png)

这是发票级别的挂起，供应商也可以被挂起。[在此了解更多](/erpnext/supplier#23-credit-limit)。

### 3.3 供应商发票详情

- **Supplier Invoice No（供应商发票号）**：供应商可能使用自己的编号来标识此订单。仅供参照。

- **Supplier Invoice Date（供应商发票日期）**：供应商在其端下单/确认您订单的日期。

### 3.4 地址和联系人

- **Supplier Address（供应商地址）**：这是供应商的账单地址。

- **Contact Person（联系人）**：如果供应商是一家公司，则会从此字段获取联系人（如果在[供应商](/erpnext/supplier)表单中设置了）。

- **Shipping Address（收货地址）**：物料将被发运到的地址。

对于印度，可以记录以下 GST 相关信息：

- Supplier GSTIN
- Place of Supply
- Company GSTIN

### 3.5 货币和价格列表

您可以设置 Purchase Invoice 订单的货币。这是从 Purchase Order 获取的。如果您设置了价格列表，则物料价格将从该列表获取。勾选"忽略价格规则"将忽略"会计 > 价格规则"中设置的[价格规则](/erpnext/pricing-rule)。

![图片](../../images/435_截图_2026-01-19_下午_12.39.55.png)

阅读[价格列表](/erpnext/price-lists)和[多币种交易](/erpnext/accounts/articles/managing-transactions-in-multiple-currencies)了解更多。

### 3.6 分包或"供应原材料"

设置"供应原材料"选项对于分包非常有用，您可以在制造物料时提供原材料。了解更多，请访问[分包页面](/erpnext/subcontracting)。

### 3.7 物料表

- **scan barcode（扫描条码）**：如果您有条码扫描器，可以通过扫描条码在物料表中添加物料。阅读[使用条码跟踪物料](/erpnext/track-items-using-barcode)的文档了解更多。

- 物料代码、名称、描述、图片和制造商将从[物料主数据](/erpnext/item)获取。

- **Manufacturer（制造商）**：如果物料由特定制造商生产，可以在此处添加。如果在物料主数据中设置，将被获取。

- **Quantity and Rate（数量和税率）**：当您选择物料代码时，其名称、描述和 UOM 将被获取。"UOM 转换系数"默认设置为1，您可以根据从卖方处收到的 UOM 进行更改，更多内容见下一节。

如果设置了标准采购价，将获取"价格列表税率"。"上次采购价"显示您上次 Purchase Order 中物料的税率。如果在物料主数据中设置了税率，则会被获取。您可以附加物料税模板以对该物料应用特定税率。

- 如果在物料主数据中设置了，将获取**物料重量**，否则手动输入。

- **Discount on Price List Rate（价格列表税率折扣）**：您可以对单个物料按百分比或在物料总金额上应用折扣。阅读[应用折扣](/erpnext/applying-discount)了解更多详情。

- **Item Weight（物料重量）**：如果已在物料主数据中设置，将获取每单位的物料重量详情和重量 UOM，否则手动输入。

- **Accounting Details（会计详情）**：如有需要，可以在此处更改费用科目。

- **Deferred Expense（递延费用）**：如果该物料的费用将在未来几个月内分期入账，请勾选"启用递延费用"。了解更多，请访问[递延费用页面](/erpnext/deferred-expense)。

- **Allow Zero Valuation Rate（允许零估值税率）**：勾选"允许零估值税率"将允许在物料估值税率为0时提交 Purchase Receipt。这可能是样品物料或与供应商协商一致的结果。

- **BOM**：如果为该物料创建了[物料清单](/erpnext/bill-of-materials)，将在此处获取。这在[分包](/erpnext/subcontracting)时作为参考非常有用。

- **Item Tax Template（物料税模板）**：您可以设置物料税模板以对该特定物料应用特定税额。了解更多，请访问[此页面](/erpnext/item-tax-template)。

- **Page Break（分页）**将在打印时在该物料之前创建分页。

#### Update Stock（更新库存）

> 注意：从版本13开始，我们引入了不可变账本，这改变了取消库存单据和在 ERPNext 中过账历史库存交易的规则。[在此了解更多](/erpnext/immutable-ledger-in-erpnext)。

如果希望 ERPNext 自动更新您的库存，应勾选**更新库存**复选框。因此，将不需要 Purchase Receipt。

### 3.8 税和费用

税和费用将从 [Purchase Order](/erpnext/purchase-order) 或 [Purchase Receipt](/erpnext/purchase-receipt) 获取。

![图片](../../images/435_截图_2026-01-19_下午_12.40.47.png)

访问 [Purchase Taxes and Charges Template](/erpnext/purchase-taxes-and-charges-template) 页面了解更多关于税的信息。

总税和费用将显示在表格下方。

要通过税类别自动添加税，请访问[此页面](/erpnext/tax-category)。

确保在税和费用表中正确标记所有税，以获得准确的估值。

#### Shipping Rule（运输规则）

运输规则有助于设置运输物料的成本。成本通常随运输距离增加而增加。了解更多，请访问[运输规则](/erpnext/shipping-rule)页面。

### 3.9 额外折扣

可以在此部分设置对整个发票的任何额外折扣。该折扣可以基于含税/费用的小计（即总合计）或不含税/费用的净合计。额外折扣可以按百分比或金额应用。

![图片](../../images/435_截图_2026-01-19_下午_12.42.03.png)

访问[应用折扣](/erpnext/applying-discount)页面了解更多详情。

### 3.10 预付款

对于高价值物料，卖方可能在处理订单之前要求预付款。**Get Advances Received** 按钮会打开一个弹出窗口，您可以从中获取已预付款的订单。了解更多，请访问[预付款单据](/erpnext/advance-payment-entry)页面。

### 3.11 付款条款

发票付款可能根据您与供应商的约定分期进行。这是从 Purchase Order 获取的（如已设置）。

![图片](../../images/435_截图_2026-01-19_下午_12.43.59.png)

了解更多，请访问[付款条款](/erpnext/payment-terms)页面。

### 3.12 坏账冲销

当客户支付的金额少于发票金额时，会发生坏账冲销。这可能是很小的差额，如0.50。在多笔订单中，这可能会累积成一个大数目。为了会计准确性，这个差额金额被"冲销"。了解更多，请访问[付款条款](/erpnext/payment-entry#25-deductions-or-loss)页面。

### 3.13 条款和条件

在销售/采购交易中，可能存在某些条款和条件，供应商根据这些条款向客户提供货物或服务。您可以将条款和条件应用到交易中，它们将在打印文档时显示。了解条款和条件，[请点击此处](/erpnext/terms-and-conditions)

### 3.14 打印设置

#### Letterhead（信头）

您可以在公司的信头上打印 Purchase Invoice。在[此处](/erpnext/letter-head)了解更多。

"Group same items（分组相同物料）"将对物料表中多次添加的相同物料进行分组。当您打印时可以查看。

#### Print Headings（打印标题）

Purchase Invoice 标题也可以在打印文档时更改。您可以通过选择**打印标题**来执行此操作。要创建新的打印标题，请前往：首页 > 设置 > 打印 > 打印标题。在[此处](/erpnext/print-headings)了解更多。

### 3.15 GST 详情（适用于印度）

可以为 GST 设置以下详情：

- GST Category（GST 类别）
- Invoice Copy（发票副本）
- Reverse Charge（反向征收）
- E-commerce GSTIN（电商 GSTIN）
- Eligibility For ITC（ITC 资格）
- Availed ITC Integrated Tax（已抵扣 ITC 综合税）
- Availed ITC Central Tax（已抵扣 ITC 中央税）
- Availed ITC State/UT Tax（已抵扣 ITC 邦/联邦直辖区税）
- Availed ITC Cess（已抵扣 ITC 附加税）

### 3.16 更多详情

- **Is Opening Entry（是期初余额）**：如果这是影响您账户的期初余额条目，请选择"是"。即如果您在年中从另一个 ERP 迁移到 ERPNext，您可能需要使用期初余额来更新 ERPNext 中的账户余额。

- **Remarks（备注）**：可以在此处添加有关 Purchase Invoice 的任何其他备注。

### 3.17 提交后

提交 Purchase Invoice 后，可以根据它创建以下单据：

- [日记账分录](/erpnext/journal-entry)
- [付款单据](/erpnext/payment-entry)
- [付款请求](/erpnext/payment-request)
- [到岸成本凭证](/erpnext/landed-cost-voucher)
- [资产](/erpnext/asset)

![图片](../../images/435_截图_2026-01-19_下午_12.45.03.png)

### 更多

### 4.1 会计影响

与 Sales Invoice 类似，在 Purchase Invoice 中，您需要为物料表中的每一行输入一个费用或资产科目。这有助于表明物料是资产还是费用。您也可以更改成本中心。这些也可以在物料主数据中设置。成本中心可以在公司级别设置。

Purchase Invoice 将按如下方式影响您的账户：

- 典型复式记账"采购"的会计分录（分类账分录）：

借记：
- 费用或资产（净额，不含税）
- 税额（如为增值税类型则计入资产或费用）

贷记：
- 供应商

![图片](../../images/435_截图_2026-01-19_下午_12.45.54.png)

### 4.2 勾选"已付款"时的会计处理

如果勾选了**已付款**，ERPNext 还将生成以下会计分录：

借记：
- 供应商

贷记：
- 银行/现金账户

在"提交" Purchase Invoice 后，要查看分录，请点击"查看分类账"。

### 4.3 采购是"费用"还是"资产"？

如果物料在购买时立即消耗，或者是服务，则采购成为"费用"。例如，电话费或差旅费是"费用"——它们已经被消耗了。

对于有价值的库存物料，这些采购还不是"费用"，因为它们在库存中时仍有价值。它们是"资产"。如果它们是原材料（用于某个流程），它们在消耗的那一刻将成为"费用"。如果它们是要卖给客户的，它们在发运给客户时成为"费用"。

### 4.4 源头扣税

在许多国家，法律可能要求您在向供应商付款时扣税。这些税可能基于标准税率。在这种方案下，通常如果供应商超过某个付款门槛，并且产品类型应纳税，您可能需要扣除一些税（您代表供应商向政府支付）。

为此，您需要在"税务负债"或类似科目下创建一个新的税科目，并在每笔交易中按您必须扣除的百分比贷记该科目。

### 4.5 挂起 Purchase Invoice 的付款

有两种方式可以挂起采购发票：

- 日期范围挂起
- 明确挂起

#### 明确挂起

明确挂起将无限期地挂起采购发票。要执行此操作，在采购发票表单的"挂起发票"部分，只需勾选"挂起发票"复选框。在"挂起原因"文本字段中，输入解释为什么发票要被挂起的评论。

如果您需要挂起已提交的发票，请点击"创建"按钮，然后点击"阻止发票"。此外，在弹出的对话框中添加解释为什么发票要被挂起的评论，然后点击"保存"。

#### 日期范围挂起

日期范围挂起将采购发票挂起至指定日期。要执行此操作，在采购发票表单的"挂起发票"部分，勾选"挂起发票"复选框。接下来，在弹出的对话框中输入释放日期，然后点击"保存"。释放日期是文档上的挂起到期的日期。

发票保存后，您可以通过点击"挂起发票"下拉按钮然后点击"更改释放日期"来更改释放日期。此操作将弹出一个对话框。

![图片](../../images/435_截图_2026-01-19_下午_12.47.43.png)

选择新的释放日期并点击"保存"。您还应在"挂起原因"字段中输入评论。

请注意以下几点：

- 所有被挂起的采购都不会包含在付款单据的参考表中
- 释放日期不能是过去的日期
- 只有在发票未付款时才能阻止或解除阻止采购发票
- 只有在发票未付款时才能更改释放日期

### 4.6 费用的临时会计处理（仅适用于非库存物料）

在许多情况下，服务已收到并发生了费用，但该服务的 Purchase Invoice 在下个月才完成，因此这笔费用不会流入您每月的财务报表（如损益表），因为发票尚未完成。临时会计帮助您解决此问题。以下是设置临时会计的步骤。

- 在公司主数据中启用临时会计并设置默认临时科目

![图片](../../images/435_enable-provisional-accounting.png)

- 为非库存物料创建 Purchase Receipt

![图片](../../images/435_pa-purchase-receipt.png)

针对 Purchase Receipt 的会计分录如下

![图片](../../images/435_pa-accounting-entry-pr.png)

- 针对 Purchase Receipt 创建 Purchase Invoice Purchase Invoice 的会计分录将照常过账

![图片](../../images/435_pa-account-entries-pi.png)

在过账采购发票时，针对采购收据的会计分录将被冲销

![图片](../../images/435_pa-accounting-entries-pr-reversed.png)

### 5. 相关主题

- [Sales Invoice](/erpnext/sales-invoice)
- [Item Wise Taxation](/erpnext/item-tax-template)
- [Payment Entry](/erpnext/payment-entry)
- [Payment Request](/erpnext/payment-request)
- [Request For Quotation](/erpnext/request-for-quotation)
- [Purchase Order](/erpnext/purchase-order)
- [Purchase Receipt](/erpnext/purchase-receipt)

---
original_url: https://docs.frappe.io/erpnext/purchase-invoice
translated_by: AI (Claude Code)
translation_date: 2026-04-18