---
original_url: https://docs.frappe.io/erpnext/email-template
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

# 电子邮件模板

每封发送的电子邮件都不相同，但某些电子邮件可以标准化，这就是通常所说的电子邮件模板或标准回复。

访问电子邮件模板列表，请前往：

首页 > 设置 > 电子邮件 > 电子邮件模板

## 1. 如何创建电子邮件模板

进入电子邮件模板列表，点击"新建"。

- 为此电子邮件模板输入名称。

- 为此电子邮件模板输入主题。

- 正文是电子邮件的标准内容，将作为此模板的一部分。

- 保存。

![电子邮件模板](images/212_email-template-example.png)

关联 DocType：（可选）与此模板关联的 DocType。

### 1.1 如何使用电子邮件模板

您可以在 ERPNext 发送的电子邮件的"抄送、密送和电子邮件模板"字段中使用此电子邮件模板。ERPNext 将根据所选模板获取主题和正文。

您可以通过[自定义表单](/erpnext/customize-form)为每个文档类型设置默认电子邮件模板。

### 1.2 如何获取字段名

您可以在电子邮件模板中使用的字段名是您发送电子邮件的文档中的字段。您可以通过[自定义表单](/erpnext/customize-form)查看任何文档的字段，并选择文档类型（例如销售订单）。

### 1.3 使用 HTML 构建模板

有一个"使用 HTML"复选框，您可以切换它以从文本编辑器切换到代码编辑器。这允许对电子邮件正文进行更精细的控制，并使其更易于在 Jinja 中使用循环等功能。

### 1.4 模板

模板使用 Jinja 编译。要了解有关 Jinja 的更多信息，请访问[此页面](https://jinja.palletsprojects.com/en/2.10.x/)。

## 2. 相关主题

- [电子邮件账户](/erpnext/email-account)

- [电子邮件收件箱](/erpnext/email-inbox)