## 概述

ERPNext 中的 **Repost Item Valuation** 功能用于在因历史过账条目或库存账本相关问题导致不一致时，重新计算物料估值、库存余额及相关会计数据。

此流程可确保库存估值和总账（GL）条目保持准确和一致。

## 何时使用 Repost Item Valuation

在以下场景中使用此功能：

- 创建或修改了历史过账的库存交易
- Stock Ledger Entries（SLE）余额不正确
- 因重新过账问题出现负库存
- 修复库存或估值相关的 bug 或应用补丁后
- 数据迁移或批量导入库存交易

## Repost Item Valuation 的功能

重新过账物料估值执行以下操作：

- 从特定时间点重新计算 **Stock Ledger Entries (SLEs)**
- 重新计算 **Running Available Stock** 和 **Stock Balance**
- 根据估值方法重新评估物料估值
- 更新 **Stock Value** 和 **Valuation Rate**
- 重新过账相关的 **General Ledger 条目**（如需要）

## 重新过账的类型

### 1. 自动重新过账

ERPNext 在以下情况下自动创建重新过账条目：

- 保存历史过账的库存交易时
- 系统检测到需要重新过账时

这些条目由计划任务在后台处理。

### 2. 手动 Repost Item Valuation

用户可以使用 **Repost Item Valuation** 工具手动触发重新过账。

#### 步骤：

1. 搜索 **Repost Item Valuation**。
2. 点击 **New**。
3. 填写所需详情：
   - **Company** – 需要重新过账的公司
   - **Item Code**（可选）– 重新过账特定物料的估值
   - **Warehouse**（可选）– 将重新过账限制在某个仓库
   - **Posting Date** 和 **Posting Time** – 重新过账的起始点
4. 保存文档。
5. 点击 **Start Reposting**。

系统将根据提供的筛选条件将重新过账任务加入队列。

## 将 Stock Ledger Variance 报告与重新过账结合使用

在触发重新过账之前，建议使用 **Stock Ledger Variance** 报告来：

- 识别不正确的 Stock Ledger Entries
- 筛选数量或余额有差异的行
- 直接选择受影响的条目创建重新过账条目

这有助于缩小重新过账范围并提高性能。

## 性能注意事项

对于大型数据集，重新过账可能消耗大量资源。

建议：

- 按物料、仓库或日期限制重新过账范围
- 在非高峰期运行重新过账

除非必要，否则避免触发完整重新过账。

## 常见问题与故障排除

### 重新过账耗时过长

- 检查受影响的条目数量
- 缩小筛选条件（物料、仓库、日期）
- 确保后台 worker 正在运行

### 重新过账后出现负库存错误

- 验证外向交易之前是否存在内向条目
- 检查过账日期和时间
- 如需要，使用 Stock Reconciliation

### GL 条目未更新

- 确保相关交易启用了 **Update Stock**
- 确认允许会计重新过账

## 最佳实践

- 重新过账前务必使用报告审查库存数据
- 避免频繁进行历史过账交易
- 保持 ERPNext 更新至最新补丁版本
- 使用增量重新过账工具，而非完整重新处理

## 注意事项

- Repost Item Valuation 会影响历史数据；请谨慎使用
- 重新过账会改变相应财年的期末余额，请谨慎操作
- 避免对已关账的财年使用重新过账，因为这将改变已关账财年的期末余额
- 用户应具备执行重新过账的适当权限
- 主要适用于影响库存的交易

**Repost Item Valuation** 功能是一项关键的维护工具，有助于确保 ERPNext 中的库存准确性和会计完整性。

---
original_url: https://docs.frappe.io/erpnext/repost-item-valuation
translated_by: AI (Claude Code)
translation_date: 2026-04-18