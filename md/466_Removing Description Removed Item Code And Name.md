**问题：**

我想从打印格式中移除描述，因为它占用太多空间：

![图片](../../images/466_cDYxb5o.png)

但当我使用[打印格式构建器](/erpnext/print-format-builder)进行移除时，我的物料代码和名称也一起消失了。如何解决？

![图片](../../images/466_Fredaow.png)

**答案：**

这是因为您在打印设置中启用了**紧凑物料打印**选项。

![图片](../../images/466_lCGM2tO.png)

您可以禁用此选项，然后在打印格式构建器中取消勾选描述。这应该可以为您解决这个问题。

![图片](../../images/466_6MI1aNw.png)

---
original_url: https://docs.frappe.io/erpnext/removing-description-removed-item-code-and-name
translated_by: AI (Claude Code)
translation_date: 2026-04-18