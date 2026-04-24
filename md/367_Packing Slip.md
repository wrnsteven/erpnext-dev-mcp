**装箱单是一份列出运输物品的文件。**

它通常随货物一起交付。

从一张 Delivery Note（交货单）可以创建多张 Packing Slip（装箱单）。当货物分装在不同的箱子中时，这非常有用。每个箱子可以有不同的重量和物品数量。例如，如果你要运输 20 把椅子，装在 4 个箱子中，每个箱子可以装 5 把椅子，每个箱子对应不同的 Packing Slip。

要访问 Packing Slip 列表，请前往：

> Home > Stock > Tools > Packing Slip

> 注意：要从 Delivery Note 创建 Packing Slip，该 Delivery Note 需要处于 Draft（草稿）阶段。

## 1. 前置条件

在创建和使用 Packing Slip 之前，建议先创建以下内容：

- [Delivery Note](/erpnext/delivery-note)

## 2. 如何创建新的 Packing Slip

通常，当 Delivery Note 处于 Draft 阶段时，你应该从 Delivery Note 创建 Packing Slip。但是，如果你想手动创建 Packing Slip，请按以下步骤操作。

- 进入 Packing Slip 列表，点击"新建"。

- 选择 Delivery Note。

- 输入该 Packing Slip 的"从包裹编号"。

- 点击"获取物品"按钮，将物品和数量获取到物品表中。

- 保存。

如果你从 Delivery Note 创建 Packing Slip，大部分详情会自动获取。

![图片](../../images/367_packing-slip.png)

### 1.1 创建 Packing Slip 时的附加选项

**至包裹编号**：如果有多个相同类型的包裹需要一起发货，请设置"从"和"至"包裹编号。例如，一个 Packing Slip 中使用 1 到 5 号包裹，下一个 Packing Slip 中使用 6 到 10 号包裹，以此类推。打印 Packing Slip 时会显示这些编号。请注意，这只在你的 Shipment 中有足够数量的 Items 时才有效。

## 2. 功能

### 2.1 物品表

- 如果这是一个批次的 Item，你必须选择 Batch Number（批次号）。

- Quantity（数量）、UoM（单位）、Net Weight（净重）和 Weight UoM（重量单位）将从 Delivery Note 获取。

- Page Break（分页）会在打印时在此物品之前创建一个分页。

### 2.2 包裹重量详情

这些详情将在打印 Packing Slip 时显示。

**净重**：这是表格中所有 Items 重量的总和。
**毛重**：这是最终总重量，包括所使用的包装材料的重量。
**毛重单位**：可以为产品的最终重量设置一个 UoM。

### 2.3 Letterhead

你可以在公司的 letterhead 上打印 Packing Slip。了解更多信息 [此处](/erpnext/letter-head)。

### 2. 相关主题

- [Quality Inspection](/erpnext/quality-inspection)

- [Delivery Note](/erpnext/delivery-note)

---
original_url: https://docs.frappe.io/erpnext/packing-slip
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---