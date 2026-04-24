UoM 是计量单位（Unit of Measurement）的缩写。UoM 的常见例子包括：个数（Nos）、千克、升、米、盒、箱等。

有些 UoM 不能有小数值。例如，如果有一台电视机，其 UoM 为个数，那么就不能有 1.5 台电视机，或 3.7 台电脑。此类物品的数量值必须是整数。

您可以配置某个 UoM 是否允许小数值。默认情况下，所有 UoM 都允许小数值。若要限制某个 UoM 的小数位或分数值，请按以下步骤操作。

### UoM 列表

进入 UoM 列表的操作路径：

`Stock > Setup > UoM`

从 UoM 列表中，选择需要限制小数的 UoM。假设 UoM 为"个数"。

### 配置

在 UoM 主数据中，有一个名为"Must be whole number"的字段。勾选此字段后，使用该 UoM 的物料在数量字段中将不允许输入小数值。

![图片](../../images/326_uom-fraction-1.png)

### 验证

在创建业务单据时，如果为勾选了"Must be whole number"的 UoM 的物料输入了小数，系统会提示错误信息：

`Quantity cannot be a fraction at row #`

![图片](../../images/326_uom-fraction-2.png)

---
original_url: https://docs.frappe.io/erpnext/managing-fractions-in-uom
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---