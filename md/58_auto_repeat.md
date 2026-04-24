---
original_url: https://docs.frappe.io/erpnext/auto-repeat
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 自动重复

自动重复功能帮助你自动创建给定时间段内的某些文档。

从版本 12 开始，你可以自定义任何表单，使文档**可重复**。

例如：假设你对某些项目使用递延费用系统。这要求你每月创建相同的日记账分录，以贷记递延费用账户和借记费用账户。你可以手动为其创建第一个日记账分录，然后为其创建自动重复交易。

要访问自动重复，请转到：

> Home > Settings > Automation > Auto Repeat

## 1. 如何设置自动重复

### 1.1 自定义表单

1. 进入：**Home > Customization > Form Customization > Customize Form**。
2. 选择你要允许创建可重复文档的表单。
3. 勾选"允许自动重复"以允许为该表单创建可重复文档。这对于文档类型显示在 Auto Repeat doctype 下的参考文档字段中是必要的。

![Allow Auto Repeat](images/58_allow-auto-repeat.png)

### 1.2 设置自动重复

1. 进入 **Home > Settings > Automation > Auto Repeat > New**。
2. 选择参考文档类型，如日记账分录或销售发票等。
3. 选择参考文档。这是你要重复的单个文档。
4. 设置开始日期和结束日期（可选）。
   如果未指定结束日期，将创建重复文档，除非自动重复被禁用。
5. 设置创建可重复文档的频率
   （每日、每周、每月、每季度、每半年、每年）。
6. 保存。

### 1.3 直接从文档设置自动重复

你也可以通过点击工具栏中**菜单**的**重复**选项来设置文档自动重复。

**注意**：如果文档已经在自动重复上，则"重复"选项不可用。

![Repeat in Transactions](images/58_repeat-option.png)

点击重复后，将显示自动重复提示。填写详情并点击保存。

![Auto Repeat Prompt](images/58_auto-repeat-prompt.png)

## 2. 功能

### 2.1 创建时提交

如果你启用"创建时提交"，则重复创建的文档将自动提交。
