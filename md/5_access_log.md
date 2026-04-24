---
original_url: https://docs.frappe.io/erpnext/access-log
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 访问日志

> Version 13 中新增

**访问日志是一个安全功能，用于记录系统中所有用户的所有数据导出。**

它是系统管理员跟踪哪些文件被系统上的用户访问或导出的工具。这对于跟踪你公司的敏感信息（如交易或财务数据）非常有用。

访问日志在以下事件中创建：

- 所有表单和报告的打印
- 私有文件下载
- 通过 XLSX/CSV 格式导出

在 ERPNext 中，访问日志可供系统管理员使用，可以通过全局搜索或以下方式访问：

> Home > Users and Permissions > Logs > Access Log

![Access Log](images/5_using-access-log-3.png)

如果在导出报告的事件中创建了访问日志，相应的日志中将生成一个 **Show Report** 按钮。点击此按钮，可以查看导出的报告以及设置的过滤器。

![Access Log](images/5_using-access-log-1.png)

同样，在与文档直接相关的事件（如文档打印和私有文件下载）的情况下，会生成 **Show Document** 按钮。

![Access Log](images/5_using-access-log-2.png)

诸如 Raw Printing 等事件会随所选模板一起保存文档信息。

![Access Log](images/5_using-acces-log-4.png)
