---
translation_date: 2026-04-18
original_url: https://docs.frappe.io/erpnext/lower-deduction-certificate
---

根据税务预扣类别，付款责任人需要按规定的税率源泉扣税。政府不是等到以后再从您那里收取所得税，而是希望付款方事先扣除税款并向政府缴纳。然而，这种源泉扣税制度可能会给一些在该财政年度可能没有应税收入的纳税人带来问题。

因此，对于此类纳税人，政府提供了一个选项，让他们可以获得证书，证明其适用的TDS税率低于税务预扣类别规定的税率或为零税率。

## 1. 前置条件

在创建和使用低额扣税证书之前，建议先创建并了解以下内容：

- [供应商](/erpnext/supplier)
- [税务预扣类别](/erpnext/tax-withholding-category)

## 2. 如何创建低额扣税证书

- 进入低额扣税证书列表，点击**新增**。
- 输入证书编号。
- 选择章节代码。
- 输入[财政年度](/erpnext/fiscal-year)。
- 选择拥有有效PAN号码的供应商。选择供应商后，PAN号码将自动获取。
- 输入生效日期和有效截止日期。
- 根据证书输入TDS税率和证书限额。
- 点击**保存**。

![图片](../images/313_lower-deduction-certificate.png)

## 3. 使用低额扣税证书

### 3.1 在采购发票中的使用

在以下示例中，我们选择了TDS类别为"TDS - 194D - Individual"，该类别的税率为5%。

![图片](../images/313_tax-withholding-category.png)

- 在供应商主数据中为供应商设置税务预扣类别。然后在选择该供应商时，采购发票中会显示一个复选框，用于选择是否应用税款，TDS类别将自动获取。

![图片](../images/313_supplier-with-tax-withholding-category.png)

- 创建一张金额为20,000的发票。保存发票时会自动计算税款并将其添加到采购税费表中。虽然分配给供应商的税类税率为5%，但当前税率为1%，该税率在低额扣税证书中已有说明。

![图片](../images/313_lower-tax-withholding-in-purchase-invoice.png)

### 4. 相关主题

- [税务预扣类别](/erpnext/tax-withholding-category)