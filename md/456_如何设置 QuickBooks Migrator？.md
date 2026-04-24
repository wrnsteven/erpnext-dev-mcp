# 如何设置 QuickBooks Migrator？

## 创建 QuickBooks Online 应用

- 在 Awesome-bar 中，进入 "QuickBooks Migrator" DocType。

- 访问 [Intuit Developer Portal](https://developer.intuit.com)

- 使用现有账户登录或注册。

- 进入 "My Apps" 页面。

- 点击 "Select APIs"。

- 在 "QuickBooks API" 下勾选 "Accounting"。

- 点击 "Create App"。

- 你将进入应用的控制面板。

- 进入 "Keys" 选项卡。

- 进入 "Production Keys" 部分。

- 完成相关要求。

- 在 "QuickBooks Migrator" DocType 中会为你生成一个 "Redirect URL"，请将其添加到 Intuit 应用的 "Redirect URIs" 列表中（在 "Production Keys" 部分下）。点击保存。

- 确保 Redirect URL 以 `https` 开头。

- 从 "Production Keys" 部分复制 "Client ID" 和 "Client Secret" 到 "QuickBooks Migrator" DocType。

- 保存 "QuickBooks Migrator"。

## 连接 QuickBooks Online API

- 点击 "Connect to QuickBooks"。

- 浏览器中会打开一个新标签页，系统会要求你登录。

- 如果你有多个公司，请选择要迁移的公司。

- 点击 "Connect"。

- 授权成功后，该标签页将关闭。

- 状态指示器将变为 "Connected to QuickBooks"。

- 在 "QuickBooks Migrator" 中选择你要迁移数据的目标 "Company"。

- 保存 "QuickBooks Migrator"。

## 迁移数据

- 点击 "Fetch Data" 按钮。

- 状态指示器将从 "Connected to QuickBooks" 变为 "In Progress"。

- 进度条将显示迁移状态。

- 根据数据量大小，此过程可能需要几分钟。

- 迁移完成后，状态指示器将变为 "Complete" 或 "Failed"。

## 点击获取数据会发生什么？

## 账户

### 现有科目表

创建公司时，ERPNext 会为该公司的创建一个科目表，这些账户将被保留。

### 账户命名

为避免与现有账户名称冲突，来自 QuickBooks 的所有账户都将被添加 "- QB" 后缀。

例如：`Job Expense` 将变为 `Job Expense - QB`。

**注意**：ERPNext 还会使用公司缩写对账户名称进行编码。考虑到这一点，`Job Expense` 将变为 `Job Expense - QB - AZ`（假设 `AZ` 是公司缩写）。

### 根账户

将创建五个根账户，即 `Asset`、`Equity`、`Expense`、`Liability`、`Income`，所有账户（根据账户类型）将成为这些根账户的子账户。

### 分组账户

QuickBooks 允许在分组账户上进行交易，但 ERPNext 不允许这样做。为处理这种情况，每个分组账户都将有一个带连字符的子账户。

例如：

```
Job Expenses
Job Materials

```

将变为：

```
Job Expenses
Job Expenses - 1
Job Materials

```

### 名称冲突

QuickBooks 允许多个账户使用相同名称，但 ERPNext 不允许这样做。为处理这种情况，每个重复的账户都将有一个带连字符的名称。

例如：

```
Insurance
Job Materials
Job Expenses
Job Materials

```

将变为：

```
Insurance
Job Materials
Job Expenses
Job Materials - 1

```

## 物料

### 命名

所有物料都将使用公司编码的名称。

例如：`Pen` 将变为 `Pen - AZ`（假设 `AZ` 是公司缩写）。

### 单位

所有物料都将被分配 `Unit` 作为默认单位。

### 分数量单位

`Unit` 将允许小数值。

### 库存

无论物料在 QuickBooks 中是库存物料还是非库存物料，都不会保留任何库存相关信息。

## 客户和供应商

### 命名

所有客户和供应商都将使用公司编码的名称。

例如：`Pen` 将变为 `Pen - AZ`（假设 `AZ` 是公司缩写）。

## 发票

### 变体

QuickBooks 有四种交易类型的发票变体，所有这些都将保存为销售发票。

- **Invoice** 等同于销售发票。

- **Sales Receipt** 等同于 POS 销售发票。

- **Credit Memo** 等同于退货销售发票（贷项通知单）。

- **Refund Receipt** 等同于退货 POS 销售发票。

### 折扣和加价

QuickBooks 为加价和折扣使用特殊账户，ERPNext 不以这种方式处理折扣费用和加价，而是所有物料将在其收入账户中看到变化。

### 运输

对于有运输费用的发票，将在物料表中添加名为 Shipping 的物料。

### 四舍五入

ERPNext 使用与 QuickBooks 不同的四舍五入方法，因此对于有税且币种不同于公司币种的发票，销售发票的总计将与 QuickBooks 发票不同。

### 特殊情况

如果 QuickBooks 发票链接到 `Delayed Charge` 或 `Statement Charge`，则将为该发票创建等效的日记账分录。

## 账单

### 变体

QuickBooks 有两种交易类型的账单变体，所有这些都将保存为采购发票。

- **Bill** 等同于采购发票。

- **Supplier Credit** 等同于退货采购发票。

## 其他

以下交易将保存为日记账分录

- 预付款

- 账单付款

- 支票

- 信用卡退款

- 费用

- 库存数量调整

- 日记账分录

- 付款

- 税款支付

## 税

对于每个 QuickBooks 税率，将创建一个 ERPNext 账户。

## 自定义字段

QuickBooks Migrator 将添加以下自定义字段

公司字段

- Customer

- Item

- Supplier

QuickBooks ID 字段

- Customer

- Item

- Journal Entry

- Purchase Invoice

- Sales Invoice

- Supplier

---

original_url: https://docs.frappe.io/erpnext/quickbooks-migrator
translated_by: AI (Claude Code)
translation_date: 2026-04-18