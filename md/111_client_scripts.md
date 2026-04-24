---
original_url: https://docs.frappe.io/erpnext/client-scripts
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

# 客户端脚本

客户端脚本是在浏览器中执行的小代码片段，用于扩展或自定义 ERPNext 的标准功能。

构建 > 脚本 > 客户端脚本

![客户端脚本](images/111_customize-erpnext-client-scripts.png)

## 如何创建自定义脚本

创建自定义脚本（您必须拥有系统管理员角色）：

- 进入自定义脚本列表，点击"新建"。

- 您将被重定向到一个页面，在那里您需要输入要创建自定义脚本的 DocType。

- 编写您的自定义脚本并确保它已启用。

- 保存。

- 注意事项

- 服务器自定义脚本仅对管理员可用。

- 客户端自定义脚本使用 JavaScript，服务器自定义脚本使用 Python。

- 为了测试，更新自定义脚本后请确保前往工具 > 清除缓存并刷新。