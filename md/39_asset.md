---
original_url: "https://docs.frappe.io/erpnext/asset"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 资产

资产是公司拥有的任何有价值物品，用于运营且使用寿命超过一年。

例子包括家具、电脑、手机、打印机、汽车和制造设备。资产可以是有形的（位于公司场所或员工手中的实物）或无形的。

资产的使用寿命跨越多年，因此从会计角度来看，其经济价值在相应年份内摊销。如果您购买一台价格为300美元的打印机，预计使用三年，从会计角度来看，三年中每年记录100美元作为费用，而不是在第一年记录全部300美元。大多数国家对此类计算都有规定。

在 ERPNext 中，<strong>Asset 记录</strong>是资产模块的核心。所有与资产相关的交易——购买、折旧、维护、移动、报废和销售——都记录在此记录下。

要访问资产列表，请转到：

> Home > Assets > Assets > Asset

## 1. 先决条件

在创建和使用资产之前，建议先创建以下内容：

- 启用了'Is Fixed Asset'的<a href="https://docs.frappe.io/erpnext/user/manual/en/item">Item</a>
- <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-location">Location</a>
- <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-category">Asset Category</a>
- <a href="https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt">Purchase Receipt</a> / <a href="https://docs.frappe.io/erpnext/user/manual/en/purchase-invoice">Purchase Invoice</a>

## 2. 如何创建资产

### 2.1 准备 Item

- 创建一个<strong>Item</strong>来表示资产。
- <strong>'Maintain Stock'</strong>应取消选中。
- <strong>'Is Fixed Asset'</strong>必须选中。

### 2.2 自动创建资产（可选）

- 如果您希望在提交<strong>Purchase Receipt</strong>时自动创建资产，请在 Item 中启用<strong>'Auto Create Assets on Purchase'</strong>。
- 在 Purchase Receipt 商品表中提供<strong>Asset Location</strong>。
- 提交时，ERPNext 显示一条消息确认资产已创建。

### 2.3 手动创建资产

如果未启用自动资产创建：

1. 转到资产列表并点击新建。
2. 输入资产的名称。
3. 选择 Item Code。
4. 关联 Purchase Receipt/Purchase Invoice（Purchase Date 和 Gross Purchase Amount 自动填充）。
5. 选择一个位置（例如 Mumbai）。
6. 设置可供使用日期——折旧将从该日期开始。
7. 点击保存并提交。

> <strong>注意：</strong>每个单独资产需要一个资产记录。例如，如果您在一次 Purchase Receipt 中购买了5台电脑，请创建5个单独的资产记录。

### 2.4 创建组合资产

- <strong>Composite Asset</strong>可以从多个物料组成（例如，由显示器、键盘等组成的计算机）。
- 在 Asset 表单中选择资产类型为<strong>'Composite Asset'</strong>。
- 在 Purchase Receipts/Invoices 中将此资产标记在<strong>WIP Composite Asset</strong>字段中。
- 收到所有物料后，使用<strong>Asset Capitalization</strong>来资本化组合资产。

<img src="/images/39_Screenshot 2026-02-20 at 1.32.41AM.png" alt="" />

<img src="/images/39_Screenshot 2026-01-11 at 11.22.10PM.png" alt="" />

### 2.5 导入现有资产

从旧系统迁移时：

1. 选择资产类型为<strong>'Existing Asset'</strong>。
2. 提供：

- Gross Purchase Amount
- Purchase Date
- Available-for-Use Date
- Opening Accumulated Depreciation
- Number of Depreciations Booked
- Is Fully Depreciated（如适用）

ERPNext 将自动计算剩余折旧计划。

## 3. 附加选项

- <strong>Custodian：</strong>负责资产的员工
- <strong>Department：</strong>保管人的部门
- <strong>Calculate Depreciation：</strong>启用以自动计算折旧

## 4. 功能

### 4.1 折旧

- <strong>折旧频率（月）：</strong>折旧条目之间的时间
- <strong>折旧总数：</strong>使用年限内的总条目数（现有资产的待摊折旧）
- <strong>折旧方法：</strong>直线法、余额递减法、双倍余额递减法、手动
- <strong>折旧过账日期：</strong>折旧开始日期
- <strong>使用年限后的预期价值：</strong>残值或残余价值
- <strong>残值百分比：</strong>根据采购总额自动计算
- <strong>折旧率：</strong>根据预期价值计算
- <strong>Finance Book：</strong>折旧条目记录的账本
- <strong>每日按比例/基于班次的折旧：</strong>根据实际使用情况调整折旧的选项

### 4.2 折旧计划

- 在<strong>折旧选项卡</strong>中查看计划
- 列：计划日期、折旧金额、已折旧金额、会计凭证

<img src="/images/39_Screenshot 2026-01-12 at 12.26.14AM.png" alt="" />

### 4.3 保险详情

- 保单号
- 保险公司
- 保险金额
- 保险开始/结束日期
- 综合保险（如适用）

### 4.4 会计条目

- 提交时：CWIP 账户贷方，资产账户借方
- 提交需要可供使用日期
- 如果是未来日期，会计条目将通过调度程序自动过账

### 4.5 维护

- 启用维护要求以记录资产维护条目
- 详细信息请参阅<strong><a href="https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance">资产维护</a></strong>页面

## 5. 提交后

创建并提交资产后，您可以：

- 转让资产
- 报废资产
- 出售资产
- 使用操作按钮调整价值或记录折旧条目

<img src="/images/39_Screenshot 2026-01-11 at 11.41.58PM.png" alt="" />

## 6. 相关主题

1. <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-maintenance">Asset Maintenance</a>
2. <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-movement">Asset Movement</a>
3. <a href="https://docs.frappe.io/erpnext/user/manual/en/purchase-receipt">Purchase Receipt</a>
4. <a href="https://docs.frappe.io/erpnext/user/manual/en/purchase-invoice">Purchase Invoice</a>