---
original_url: https://docs.frappe.io/erpnext/raw-printing
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

> 版本 12 中引入

**直接向打印机发送一串以其原生语言编写的命令，这种方式称为 Raw Printing。**

许多热敏打印机需要接收这些原始命令才能执行条形码打印、收据打印、标签打印等功能。Raw Printing 在大多数情况下会绕过打印机的驱动程序，使打印速度非常快且可靠。Raw Printing 还能实现一些高级功能，如切纸、弹出钱箱等。

## 1. 在 ERPNext 中设置 Raw Printing

### 1.1 在客户端计算机上安装 QZ Tray 应用程序

在与热敏打印机相连的计算机上下载并安装 QZ Tray 应用程序。该应用程序可在其[官方网站](https://qz.io/download/)找到。QZ Tray 目前支持 Windows、macOS 和 Linux 系统。安装过程中，如果尚未安装 Java，系统会提示您安装，请安装 Java 以完成安装。

有关安装 QZ Tray 应用程序的更多说明，请参见[此处](https://qz.io/wiki/using-qz-tray)。

### 1.2 创建 Raw Commands 打印格式

要能够向打印机发送原始命令，您需要首先创建一个使用原始命令的打印格式。与 [HTML 自定义打印格式](/erpnext/print-format)一样，原始命令中也使用 Jinja 模板语言。

创建 Raw Printing 新打印格式的步骤：

- 进入打印格式列表：**首页 > 设置 > 打印 > 打印格式**

- 点击"新建"。

- 选择相关的 DocType。

- 勾选**自定义格式**和**Raw Printing**选项。

- 在**原始命令**字段中填写要发送到打印机的所需原始命令。

- 点击保存。

![图片](../../images/458_raw-command-print-format.png)

目前，打印格式的 `Raw Commands` 字段中可以使用任何基于字符串的打印机语言。编写原始命令需要具备打印机制造商提供的打印机原生语言知识。请参阅打印机制造商提供的开发手册，了解如何编写其原生命令。

### 1.3 在打印设置中启用 Raw Printing

启用 Raw Printing 的步骤：

- 进入：**首页 > 设置 > 打印 > 打印设置 > Raw Printing**。

- 勾选**启用 Raw Printing**选项。

- 保存。

## 2. 在 ERPNext 中使用 Raw Printing 的方法

有两种方式可以将 Raw Printing 命令发送到您的打印机。

### 2.1 在打印预览页面点击打印

从文档打印预览中打印原始命令打印格式的步骤：

- 选择相应的打印格式。对于使用原始命令的打印格式，将显示"无可用预览"消息来代替打印预览。

- 点击打印按钮。

- 请允许 QZ Tray 的连接提示，以执行您启动的操作（快捷键：Alt + A）。

- ![图片](../../images/458_qz-tray-prompt.png)

- 系统可能会要求您选择"打印格式 - 打印机映射"。

- 此映射用于将打印命令发送到相应的打印机。

打印机需要安装在您的计算机上，才能将其映射到打印格式。

![图片](../../images/458_printer-settings.png)

- 此映射存储在同一台计算机的本地，需要在每个客户端计算机上单独设置。

- 您也可以通过点击**打印机设置**按钮进行编辑。

![图片](../../images/458_raw-printing-from-print-view.gif)

### 2.2 从客户端脚本调用 Raw Print 函数

通常有这样的需求：需要在某个事件（如提交、保存、修订等）时触发打印命令。您可以编写一个[客户端脚本](/erpnext/client-scripts)来实现此功能。

以下是相关的 Raw Print 函数：

- 函数：`frappe.ui.form.qz_connect`

- 一个连接封装器，用于与 QZ Tray 应用程序建立连接。

- 返回一个 promise，连接成功建立后 resolve。

- 无论连接是活动状态还是非活动状态都会 resolve。因此，每次发送命令前都可以调用此函数。

- 使用示例：

```javascript
 frappe.ui.form.qz_connect()
 .then(function () {
 return qz.print(config, data);
 })
 .then(frappe.ui.form.qz_success)
 .catch(err => {
 frappe.ui.form.qz_fail(err);
 });
```

此处，`qz` 是由 `qz-tray.js` 库提供的全局对象。

- 函数：`frappe.ui.form.qz_get_printer_list`

- 返回 QZ Tray 应用程序可用的打印机列表。

- 返回一个 resolve 为打印机列表的 promise。

使用示例：

```javascript
 frappe.ui.form.qz_get_printer_list().then(
 // 获取打印机列表后执行所需操作。
 // 注意：打印机列表是一个字符串数组。
 );
```

- 函数：`frappe.ui.form.qz_success`

- 向用户显示"打印已发送到打印机！"提示。可以在打印命令成功后调用。

- 函数：`frappe.ui.form.qz_fail`

- 向用户显示错误消息。QZ Tray 连接失败时应调用此函数。

您也可以通过 `qz` 对象直接访问 `qz-tray.js` 库提供的函数。[点击此处查看 qz-tray.js 库文档](https://qz.io/api/)。注意：`qz` 对象只有在首次调用 `frappe.ui.form.qz_connect` 后才会初始化。如果在此之前需要使用 `qz` 对象，您可以使用 `frappe.ui.form.qz_init`。

### 3. 相关主题

- [打印设置](/erpnext/print-settings)

- [打印格式](/erpnext/print-format)

- [打印样式](/erpnext/print-style)