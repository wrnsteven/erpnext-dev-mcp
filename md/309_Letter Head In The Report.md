在报表中，Letter Head 从 Company master 中获取。

要使报表中正确获取公司的 Letter Head，请确保您已在 Company master 中更新了默认的 Letter Head。

> 探索 &gt; 会计 &gt; 公司

![图片](../../images/309_using-print-format.png)

在 Company master 中，如果没有设置默认的 Letter Head，则报表中会获取"默认"字段被勾选的 Letter Head。

![图片](../../images/309_using-print-format-1.png)

如果您在单个 ERPNext 账户中管理多家公司，请确保为每个公司都在 Company master 中设置了默认的 Letter Head。

在 Company master 中更新 Letter Head 后，刷新您的 ERPNext 账户，然后检查报表的 print format。

---
original_url: https://docs.frappe.io/erpnext/letter-head-in-the-report
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---