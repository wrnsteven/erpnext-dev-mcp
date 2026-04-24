---
original_url: https://docs.frappe.io/erpnext/exchange-rate-revaluation
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

# 汇率重估

在 ERPNext 中，您可以用多种货币进行会计录入。例如，如果您有外币银行账户，您可以以该货币进行交易，系统将以该特定货币显示银行余额。

汇率重估主记录的目的是根据货币汇率的任何变化调整总账账户中的余额。当您结清账户账簿并希望从其他货币账户引入资金来更新公司总账账户时，这非常有用。

注意：从 ERPNext v14 开始，汇率重估可以处理在基本货币或账户货币中余额为"0"的外币账户。系统将为它们创建一张状态为草稿的"汇率收益/损失"类型的独立日记账。

访问汇率重估列表，请前往：

首页 > 会计 > 多币种 > 汇率重估

## 如何在账户中设置货币

- 要开始多币种会计，您需要在账户记录中分配会计货币。

- 您可以在创建账户时从会计科目表定义货币。

![分类账中的货币](images/217_currency-in-ledger.png)

3. 您还可以通过打开特定账户记录来为现有账户分配/修改货币。
4. 点击该账户，然后点击"编辑"。

![设置账户货币](images/217_update-currency-in-ledger.png)

## 如何启用汇率重估

汇率重估功能用于处理在一个公司的会计科目表中存在不同货币账户的情况。

- 进入：**设置 > 公司 > *选择公司***。

- 在公司 DocType 中设置"未实现汇率收益/损失账户"字段。此账户用于平衡总贷方和总借方的差额。

![公司中的未实现汇率收益/损失分类账](images/217_unrealized-exchange-gain-loss-ledger-in-company.png)

3. 进入会计 > 设置 > 汇率重估 > 新建。
4. 选择公司。
5. 点击"获取条目"按钮。它将获取货币不同于在公司中设置的"默认货币"的账户。
6. 如果该货币在货币汇率 DocType 中未设置，这将自动获取新汇率，否则将获取[货币汇率](/erpnext/currency-exchange) DocType 中设置的"汇率"。![汇率重估](images/217_exchange-rate-revaluation.png)
7. 提交后，将出现"创建日记账凭证"按钮。![提交后的日记账凭证选项](images/217_exchange-rate-revaluation-submit.png)
8. 点击此按钮将为汇率重估创建日记账凭证。![汇率重估日记账凭证](images/217_exchange-rate-revaluation-journal-entry.png)
9. 提交日记账凭证后，总账将受到如下影响：![汇率重估总账](images/217_exchange-rate-revaluation-gl.png)

### 3. 自动创建汇率重估

在公司主记录中的"汇率重估设置"下提供了自动创建汇率重估的选项。

![Screenshot 2023-07-10 at 11.52.17 AM](images/217_Screenshot%202023-07-10%20at%2011.52.17%20AM.png)

### 4. 相关主题

- [公司间日记账凭证](/erpnext/inter-company-journal-entry)

- [公司间发票](/erpnext/inter-company-invoices)