**使用 Print Format，您可以设置打印时文档类型的外观。**

每个交易都配有一个名为"Standard"的默认 Print Format。您可以通过以下方式更改 Print Format：

- 使用 Print Format 表单
- 使用 Print Format 下的 Jinja/JS 脚本
- 使用 [Print Format Builder](/erpnext/print-format-builder) 通过界面创建打印格式
- 使用 Customize Form 隐藏/显示字段

要访问 Print Format，请进入：

> 首页 > 设置 > Print Format

## 1. 如何创建 Print Format

- 进入 Print Format 列表，点击"新建"。
- 输入名称并选择要应用 Print Format 的 DocType。
- 将自动选择适用的模块。

![图片](../../images/403_print-format-menu.png)

- 保存。

在样式设置下，有更改样式选项的功能。利用这些选项，您可以更改字体、将标签一起左对齐或右对齐、为各部分添加标题等。

要使用自定义 Jinja/JS 设置 Print Format 样式，请点击"Custom Format"。如果选择此选项，将有一个用于原始打印的复选框。要了解更多关于原始打印的信息，[请点击此处](/erpnext/raw-printing)。

如果开发者模式已启用，您可以将"Standard"选择为"yes"，将打印格式作为系统中的标准（预设）打印格式贡献出来。

## 1.1 使用 Customize Form 更改 Print Format 项目

可以使用 Customize Form 隐藏/显示交易及其子表中的字段。
例如，如果要在打印报价单时隐藏"Item Code"，请点击打印图标进入打印屏幕。
进入菜单 > Customize，在"Enter Form Type"字段中选择"Quotation Item"。
![图片](../../images/403_print-format-customize1.png)
要了解更多，请访问 [Customize Print Format](/erpnext/print-format) 页面。

在字段表中，展开"Item Code"行，向下滚动并勾选"Print Hide"复选框。
![图片](../../images/403_print-format-customize2.png)
新创建的 Print Format 可以从交易的打印屏幕中选择。从那里您可以查看其外观并进行打印。
![图片](../../images/403_print-format-selection.png)

## 2. 视频

### 3. 相关主题

- [Print Style](/erpnext/print-style)
- [Print Headings](/erpnext/print-headings)
- [Letter Head](/erpnext/letter-head)
- [Cheque Print Template](/erpnext/cheque-print-template)
- [Disabling Line Breaks in Print Format Sections](/erpnext/print-format-sections)

---
original_url: https://docs.frappe.io/erpnext/print-format
translated_by: AI (Claude Code)
translation_date: 2026-04-18