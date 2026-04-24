---
original_url: "https://docs.frappe.io/erpnext/asset-category"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 资产类别

<strong>资产类别用于分类公司的不同资产，并为其设置默认的会计和折旧规则。</strong>

Asset Category DocType 帮助将类似的资产组织在单一分类下，并简化资产管理。例如，所有台式机和笔记本电脑可以属于一个名为<strong>"电子设备"</strong>的资产类别。每个类别可以有其默认的折旧方法、会计设置和成本中心，这些设置会自动应用到该类别下的所有资产。

要访问资产类别列表，请前往：

> Home > Asset > Assets > Asset Category

## 1. 先决条件

在创建资产类别之前，建议先创建：

- 一个<strong><a href="https://docs.frappe.io/erpnext/user/manual/en/company-setup">公司</a></strong>

## 2. 如何创建资产类别

- 前往资产类别列表并点击新建。
- 输入类别的名称。
- 根据需要配置可选的折旧和会计详情。
- 点击保存。

<img src="/images/41_Screenshot 2026-01-11 at 11.31.43PM.png" alt="" />
*资产类别*

### 2.1 创建资产类别时的其他选项

1. <strong>启用资本在建工程会计</strong>：启用此选项后，不在使用中的属于此类别的资产的会计条目将过账到资本在建工程账户。当您拥有资产但尚未使用时（即"可供使用日期"设置为较晚的日期），就会发生这种情况。如果您立即使用所有资产，请禁用此功能。禁用此功能后，将跳过 CWIP 会计。
2. <strong>不折旧类别</strong>：启用此选项后，将跳过此类别下资产的折旧。折旧相关的账户字段将不是必需的，并且不会生成折旧计划。将其用于土地或其他不可折旧的资产等。如果应 적용折旧，请禁用。

## 3. 功能

### 3.1 财务账本详情

如果您以不同方式报告折旧，可以链接一个财务账本。您可以输入以下字段：

- <strong>折旧方法</strong>：选择一种折旧方法，您将使用该方法记录此类别中资产的折旧。要了解更多信息，请访问此页面。
- <strong>折旧频率（月）</strong>：折旧将被记录在其中的月数。资产在此期间后可能会被报废。
- <strong>折旧总数</strong>：在选定时间段内要记录的折旧次数。
- <strong>折旧率</strong>：在选定期间应用的折旧率。这将根据所选的折旧方法计算。

<img src="/images/41_Screenshot 2026-01-11 at 11.31.43PM5c5a1a.png" alt="" />

### 3.2 会计详情

可以设置以下账户详情以在账本中记录资产价值：

- 公司
- 固定资产账户
- 累计折旧账户
- 折旧费用账户
- 资本在建工程账户

## 4. 创建资产类别之后

创建后，您可以：

- 在此类别下创建新的<strong>资产</strong>。
- 使用资产模块跟踪折旧、维护、转移或处置。

## 5. 相关主题

1. <a href="https://docs.frappe.io/erpnext/user/manual/en/finance-book">Finance Book</a></li>
2. <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-depreciation">折旧</a></li>