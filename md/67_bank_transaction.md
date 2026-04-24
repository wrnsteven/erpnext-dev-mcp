---
original_url: https://docs.frappe.io/erpnext/bank_transaction
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 银行交易

**Bank Transaction** 表单显示导入到 ERPNext 的银行交易，通常来自银行对账单或集成。

## 1. 前置条件

在使用 **Bank Transaction** 之前，建议首先创建以下内容：

1. **[Bank](erpnext/user/manual/en/bank)**
2. **[Bank Account](erpnext/user/manual/en/bank-account)**

## 2. 如何使用银行交易

**Bank Transaction** 通常不是手动创建的。它可以通过以下方式导入或创建：

1. **[Bank Statement Import](erpnext/user/manual/en/bank-reconciliation#321-bank-statement-import)** — 从 CSV 或 XLSX 文件导入
2. **[Data Import](erpnext/user/manual/en/data-import)** — 标准数据导入工具
3. 银行集成应用（例如，Plaid 或其他第三方集成）

导入后，可以使用 [Bank Reconciliation Tool](erpnext/user/manual/en/bank-reconciliation) 将 **Bank Transactions** 与凭证进行对账。

## 3. 字段

### 3.1 基本信息

- *日期*：银行交易的日期。
- *状态*：交易的当前状态：
    - 待处理
    - 已结算
    - 未对账
    - 已对账
    - 已取消
- *银行账户*：进行交易的 **Bank Account**。
- *公司*：与银行账户关联的 **Company**（从 *Bank Account* 自动获取）。

### 3.2 交易金额

- *存款*：存入的金额（贷记到你的账户）。
- *取款*：取出的金额（从你的账户借记）。
- *货币*：交易使用的货币。

### 3.3 描述和参考

- *描述*：来自银行对账单的描述。
- *参考编号*：支票号码或其他参考。
- *交易 ID*：来自银行的唯一标识符（只读）。
- *交易类型*：银行报告的交易类型。

### 3.4 付款分录

*Payment Entries* 表将银行交易链接到 ERPNext 中的凭证以进行对账：

- *付款凭证*：交易要对账的凭证类型，例如 **Sales Invoice**、**Purchase Invoice**、**Payment Entry**、**Journal Entry** 或 **Expense Claim**。
- *付款分录*：链接到此交易的特定凭证。
- *分配金额*：从此银行交易分配到付款分录的金额。
- *清算日期*：付款清算的日期（提交后显示）。

### 3.5 分配摘要

- *已分配金额*：已分配到付款分录的总金额（只读）。
- *未分配金额*：尚未分配的剩余金额（只读）。

### 3.6 付款从/到（交易方信息）

- *交易方类型*：交易方类型（例如，客户、供应商、员工）。
- *交易方*：链接到此交易的特定交易方。

以下字段包含银行对账单提供的交易方信息：

- *交易方名称/账户持有人（银行对账单）*：银行对账单中的交易方名称。
- *交易方账号（银行对账单）*：银行对账单中的交易方账号。
- *交易方 IBAN（银行对账单）*：银行对账单中的交易方 IBAN。

> 银行对账单中的交易方信息可用于在 **Accounts Settings** 中启用时进行自动交易方匹配。

### 3.7 扩展银行对账单（费用处理）

这些字段处理可能包含在交易金额中或从中排除的银行费用：

- *包含费用*：已包含在 *取款* 金额中的费用。例如，如果取款 100 包含 5 的费用，则净付款为 95。
- *排除费用*：单独从交易中收取的费用。保存时，通过调整交易金额自动将其转换为 *包含费用*。

> **注意**：排除费用会调整交易金额：减少 *存款* 或增加 *取款*。
