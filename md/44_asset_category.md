---
original_url: "https://docs.frappe.io/erpnext/asset-category"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 资产类别

资产类别对公司不同资产进行分类，并为其设定默认的会计和折旧规则。

资产类别 DocType 帮助将类似资产归为一个分类并简化资产管理。例如，所有台式机和笔记本电脑可以属于名为<strong>"电子设备"</strong>的资产类别。每个类别可以有不同的默认折旧方法、会计设置和成本中心，这些会自动应用于该类别中的所有资产。

要访问资产类别列表，请转到：

> Home > Asset > Assets > Asset Category

## 1. 先决条件

在创建资产类别之前，建议：

- 创建一个<strong><a href="https://docs.frappe.io/erpnext/user/manual/en/company-setup">公司</a></strong>

## 2. 如何创建资产类别

- 转到资产类别列表并点击新建。
- 输入类别的名称。
- 根据需要配置可选的折旧和会计详细信息。
- 点击保存。

<img src="/images/44_Screenshot 2026-01-11 at 11.31.43PM.png" alt="" />
*资产类别*

### 2.1 创建资产类别时的附加选项

1. **启用资本化工作进度会计**：启用此选项后，不在使用中的资产（即可供使用日期设置为较晚日期）的会计条目将过账到资本化工作进度账户。如果您立即使用所有资产，请禁用此功能。禁用此功能后，将跳过 CWIP 会计。

2. **非折旧类别**：启用此选项后，将跳过此类别资产的折旧。折旧相关账户字段不是必需的，不会生成折旧计划。将此用于土地或其他不可折旧的资产等。如果应该应用折旧，请禁用。

## 3. 功能

### 3.1 Finance Book 详情

如果您以不同方式报告折旧，您可以链接一个 Finance Book。您可以输入以下字段：

- **折旧方法**：选择折旧方法，用于记录此类别资产的折旧。了解更多，请访问此页面。
- **折旧频率（月）**：折旧入账的月数。资产在此期间后可能会报废。
- **折旧总数**：在所选时间段内入账的折旧次数。
- **折旧率**：在所选期间应用的折旧率。这将根据所选的折旧方法计算。

<img src="/images/44_Screenshot 2026-01-11 at 11.31.43PM5c5a1a.png" alt="" />

### 3.2 会计详情

可以设置以下账户详情来在分类账中记录资产价值：

- Company
- Fixed Asset Account
- Accumulated Depreciation Account
- Depreciation Expense Account
- Capital Work In Progress Account

## 4. 创建资产类别后

创建后，您可以：

- 在此类别下创建新的<strong>Assets</strong>。
- 使用资产模块追踪折旧、维护、转让或处置。

## 5. 相关主题

1. <a href="https://docs.frappe.io/erpnext/user/manual/en/finance-book">Finance Book</a>
2. <a href="https://docs.frappe.io/erpnext/user/manual/en/asset-depreciation">Depreciation</a>