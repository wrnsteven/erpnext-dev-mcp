**询价单是一份组织向一个或多个供应商发送的文件，用于请求物品报价。**

![图片](../../images/471_buying_flow_rfq.png)

要访问**询价单**，请打开 "Buying" workspace，在 "Reports & Masters" > "Buying" 下，点击 "Request for Quotation"。

- 前置条件

在创建和使用**询价单**之前，建议您先创建以下内容：

- [Supplier](/erpnext/supplier)

- [Item](/erpnext/item)

- 如何创建询价单

转到**询价单**列表，点击"+ Add Request for Quotation"。

输入*Required Date*（需求日期），即您需要所请求物料的日期。

在"Suppliers"列表中填写可能的供应商。
如果您设置了*Contact*（联系人）和*Email Id*（电子邮件地址），之后可用于通过电子邮件发送**询价单**，并授予供应商门户访问权限。

在下一个表格中，输入所需的物料及其 UOM 和数量，以及目标仓库。

如果该物料未启用*Maintain Stock*（维护库存），则可以留空 *Warehouse*（仓库）。

如果您想通过电子邮件将**询价单**发送给供应商，可以创建**Email Template**（电子邮件模板）并在此处选择。在模板中，您可以使用特殊的供应商特定数据变量：

- `{{ update_password_link }}`：供应商可以设置新密码以登录您门户的链接。

- `{{ portal_link }}`：供应商门户中此 RFQ 的链接。

- `{{ supplier_name }}`：您供应商的公司名称。

- `{{ contact.salutation }} {{ contact.last_name }}`：您的供应商联系人。

- `{{ user_fullname }}`：您的全名。

除此之外，您可以访问此 RFQ 中的所有值，如 `{{ message_for_supplier }}` 或 `{{ terms }}`。

您可以使用"Preview Email"（邮件预览）按钮来查看特定供应商的邮件外观。

![图片](../../images/471_email-preview.png)
8. 如果您想向供应商发送更多附件，可以启用*Send Attached Files*（发送附件文件）复选框。这会将附加到**询价单**的每个文件作为附件添加到每个供应商邮件中。
9. 完成操作后，将**询价单**保存为草稿。
10. 准备就绪后，您可以提交**询价单**。这将向每个启用了*Send Email*（发送邮件）的供应商触发一封电子邮件。
![图片](../../images/471_rfq-create.png)

询价单 (RFQ) 也可以从已提交的物料请求创建。创建 RFQ 后，您可以打印并向供应商发送 PDF，其中包含您输入的所有与 RFQ 相关的详细信息。您也可以在 ERPNext 中获取他们的回复（供应商报价），请参阅章节 [4.1 用户创建的供应商报价](#41-supplier-quotation-by-user)。但是，对于大量物料，您的供应商可能更习惯使用 Excel 表格等。

- 功能

### 3.1 从...获取物料

物料表中的物料可以从其他文档中获取。选项包括：物料请求、机会和可能的供应商。

- **Material Request（物料请求）**：物料将从您选择的已提交物料请求中获取。可以通过一些匹配词搜索物料请求，也可以选择日期范围来筛选物料请求。

- **Opportunity（机会）**：物料将从已保存的机会中获取。此处也可以选择日期范围。

- **Possible Supplier（可能的供应商）**：选择一个可能的供应商。然后，如果您有任何针对该供应商的已提交物料请求，可以从其中获取物料。

![图片](../../images/471_rfq-get-items.png)

### 3.2 获取供应商

除了手动在表格中输入供应商外，您还可以使用"Get Suppliers"按钮获取它们。点击**Tools > Get Suppliers**后，您将看到"Get Suppliers By"字段。有两种获取供应商的方式：按标签或按组。

- **By tag（按标签）**：通过搜索栏搜索进入"Tag Category"。您必须先在此处创建标签，然后将其分配给采购模块中的供应商。然后您可以选择"By Tag"。点击"Add All Suppliers"后，将获取具有匹配标签的供应商。

- **By Group（按组）**：选择"Supplier Group"并选择需要添加供应商的供应商组。例如，如果您选择 Hardware，所有硬件供应商将被添加，这样您就可以从所有供应商处获取报价。

![图片](../../images/471_rfq-get-suppliers.png)

在供应商表中，展开带有倒三角形的行后，您将看到"Download PDF"选项，这将打开 RFQ 的 PDF。

### 3.3 链接到物料请求

点击**Tools > Link to Material Requests**后，它会将询价单链接到可用的物料请求。询价单和物料请求中的物料应该相同。

![图片](../../images/471_link-to-material-request.png)

现在，当询价单被保存后，您可以在仪表板中看到它已链接到物料请求。如果有多个具有相同物料的物料请求，则会与最新的物料请求创建链接。

### 3.5 条款和条件

在销售/采购交易中，可能存在某些条款和条件，供应商根据这些条款和条件向客户提供商品或服务。您可以将条款和条件应用到交易中，它们会在打印文档时显示。了解条款和条件，请[点击此处](/erpnext/terms-and-conditions)

### 3.6 打印设置

#### Letterhead（信头）

您可以在公司的信头上打印您的询价单/采购订单。了解更多[此处](/erpnext/letter-head)。

"Group same items"（合并相同物料）将对物料表中多次添加的相同物料进行分组。打印时可以看到效果。

#### Print Headings（打印标题）

您可以更改文档的标题。了解更多[此处](/erpnext/print-headings)。

#### 特殊属性

通过"Tools > Download PDF"按钮打印 RFQ 时，系统会要求您选择要针对的特定供应商。在 RFQ 的**Print Format**中，可以通过特殊属性访问此信息：

- `{{ doc.vendor }}` 保存所选供应商的 ID。

- `{{ doc.items[i].supplier_part_no }}` 保存所请求行项目的*Supplier Part Number*（供应商零件号）。

渲染标准打印预览时将使用第一个供应商的数据。如果要为不同供应商打印，请使用"Tools > Download PDF"按钮。

- 在 RFQ 之后创建供应商报价

创建询价单后，有两种方式可以从询价单生成供应商报价。

### 4.1 用户创建的供应商报价

- 打开询价单并点击**Supplier Quotation > Create**。

![图片](../../images/471_make-supplier-quotation-from-rfq.png)
2. 选择供应商，再次点击该供应商。在此页面，点击"Supplier Quotation"旁边的 +。将打开一个新的供应商报价页面，用户需要输入数量、单价并提交。
![图片](../../images/471_supplier-quotation-from-sup.png)

### 4.2 供应商创建的供应商报价

- 如果为供应商创建了[Contact](/erpnext/contact)并将电子邮件地址与该联系人关联，则在选择供应商时将获取联系人详细信息和电子邮件地址。如果尚不存在，请先创建联系人和电子邮件地址。

- 点击**Tools > Send Emails to Suppliers**。

**如果供应商账户不存在**：系统将创建供应商账户并向供应商发送详细信息。供应商需要点击邮件中的链接（密码更新）。更新密码后，供应商可以使用"Request for Quotation"表单访问他们的门户。供应商将被创建为网站用户。

![图片](../../images/471_supplier-email-with-update-password.png)

**如果供应商账户存在**：系统将向供应商发送询价单链接。供应商必须使用其凭据登录才能在门户上查看询价单表单。

![图片](../../images/471_supplier-email-normal.png)
3. 无论哪种方式，当供应商登录时，将向他们显示以下屏幕。从这里他们可以向您发送报价：
![图片](../../images/471_rfq-supplier-quotation.png)

供应商需要在表单上输入金额和备注（付款条款），然后点击提交。在报价部分可以看到之前的报价。
4. 提交后，ERPNext 将为该供应商创建一份供应商报价（草稿模式）。用户需要审核供应商报价并提交。当供应商对询价单中的所有物料都进行报价后，询价单"Suppliers"表中的报价状态将在询价单的"Suppliers"表中更新为"Received"。
![图片](../../images/471_rfq-supplier-quoted.png)

阅读[供应商报价](/erpnext/supplier-quotation)了解更多。

- 视频

### 6. 相关主题

- [采购订单](/erpnext/purchase-order)

- [Supplier](/erpnext/supplier)

- [供应商报价](/erpnext/supplier-quotation)

- [报价单](/erpnext/quotation)

- [物料请求](/erpnext/material-request)

---
original_url: https://docs.frappe.io/erpnext/request-for-quotation
translated_by: AI (Claude Code)
translation_date: 2026-04-18