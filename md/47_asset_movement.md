---
original_url: "https://docs.frappe.io/erpnext/asset-movement"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 资产移动

<strong>资产移动是一个用于在位置和/或员工（保管人）之间转移资产的交易。</strong>

此功能帮助您跟踪组织内资产的 physical 移动和保管。您可以将资产从一个仓库移动到另一个仓库，分配给员工，或记录其归还。

例如，笔记本电脑可以从总部位置发放给销售部门的员工，之后在归还时转移回仓库。

要访问资产移动列表，请前往：

> Home > Assets > Assets > Asset Movement

## 1. 如何创建资产移动

1. 前往<strong>资产移动</strong>列表。
2. 点击<strong>新建</strong>。
3. 选择<strong>目的</strong>。
4. 输入所需的详细信息。
5. 点击<strong>保存</strong>和<strong>提交</strong>。

> 资产移动是一笔交易，必须<strong>提交</strong>才能更新资产的位置或保管人。

<img src="/images/47_Screenshot 2026-02-20 at 12.39.33AM.png" alt="" />

## 2. 功能

### 2.1 资产移动的目的

<strong>目的</strong>字段决定正在执行的移动类型。基于所选目的，必填字段将发生变化。

1. 转移：将资产从一个位置移动到另一个位置。
   - 示例：将成型机从"工厂A"转移到"工厂B"。
2. 发放：将资产从一个员工移动到另一个员工
   - 示例：从仓库向 John Carter（销售主管）发放公司笔记本电脑。
3. 接收：将资产从员工处移回位置。
   - 示例：从辞职员工处接收笔记本电脑并将其移回仓库。
4. 转移和发放：在单个条目中同时将资产从一个位置到另一个位置，以及从一个员工到另一个员工。

当资产同时更改物理位置和保管人时，这很有用。

## 3. 一次移动多个资产

如果您想一起移动多个资产：

1. 前往<strong>资产列表</strong>。
2. 使用复选框选择多个资产。
3. 点击<strong>操作</strong>（右上角）。
4. 选择<strong>创建资产移动</strong>。

这将创建带有预填充所选资产的新资产移动。

<img src="/images/47_Screenshot 2026-02-20 at 12.35.22AM.png" alt="" />

## 4. 从资产表单发起资产移动

在资产表单右上角的<strong>操作</strong>下拉菜单中也有<strong>转移资产</strong>选项可发起资产移动。它从资产表单自动填充可用字段。

<img src="/images/47_Screenshot 2026-02-20 at 12.37.04AM.png" alt="" />