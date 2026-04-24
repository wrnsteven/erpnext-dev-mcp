---
original_url: https://docs.frappe.io/erpnext/auto-email-reports
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 自动电子邮件报告

**自动电子邮件报告会自动发送所选文档的报告。**

你可以设置 **Auto Email Report** 以定期发送报告。这些必须是任何类型的已保存报告（Report Builder、Script 或 Query Report）。

你可以在以下位置找到自动电子邮件报告：

> Home > Settings > Auto Email Report

1. 如何创建自动电子邮件报告

---

1. 进入 Auto Email Report 列表，点击新建。
2. 选择你要为其生成电子邮件的报告。
3. 选择你要为其创建此报告的用户（权限将适用于此用户）。
4. 设置你要发送此报告的电子邮件地址和报告的频率。电子邮件将在午夜发送。如果频率是每周/每月/每年，日期将重复。

![With Filters](images/57_auto-email-2.png)

5. 保存。

你可以通过点击"下载"或"立即发送"来测试报告。以下是你将收到的总账报告电子邮件示例：

![Report by Email](images/57_auto-email-4.png)

2. 功能

---

### 2.1 筛选数据

- **仅在有数据时发送**：如果启用，如果报告中没有数据，则不会发送电子邮件。
- **仅发送最近 X 小时内更新的记录**：如果设置为 24，则电子邮件将仅包含最近 24 小时内更新的记录。
- **行数**：电子邮件中发送的行数。最大值为 500。

### 2.2 报告筛选器

如果你的报告有筛选器，你将能够看到它们。点击表格进行编辑：

![Edit Filters](images/57_auto-email-3.png)

例如，如果电子邮件是关于"项目计费摘要"报告的，请选择项目。此处的日期范围是"项目计费摘要"的日期范围。

### 2.3 消息

也可以添加与电子邮件报告一起发送的消息。例如，"这是你的每月项目计费摘要报告："。

你还可以更改创建报告的文件格式。可用选项为 HTML、XLSX 和 CSV。

### 2. 相关主题

1. Email Digest
2. Document Follow
