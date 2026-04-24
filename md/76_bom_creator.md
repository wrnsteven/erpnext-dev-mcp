---
original_url: https://docs.frappe.io/erpnext/bom_creator
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 多级 BOM 创建器

BOM 创建器使用户能够通过单个屏幕创建多级 BOM。

![](/files/bom_creator_tree.png)

## 为什么使用 BOM 创建器？

用户经常质疑为什么需要单独的 BOM 创建器来创建 BOM。答案在于消除不必要的往返。使用标准 BOM 屏幕，用户需要首先创建所有子装配 BOM，然后为最终产品创建 BOM。这个过程通常涉及大量往返。此外，有时使用标准 BOM 很难可视化完整的层次结构。

为了解决所有这些问题，我们引入了 BOM 创建器。在 BOM 创建器中，用户可以使用树组件构建多级 BOM。

工作原理如下：

- 用户选择最终产品并保存记录。

![](/files/bom-creator.png)

- 在表单中，用户将找到添加与最终产品相关的原材料和子装配项目的选项。

![](/files/toolbar_bom_creator.png)

- 如果用户想将原材料转换为子装配项目，他们需要首先点击该项目，然后点击"转换为子装配"按钮。

![](/files/convert_to_sub_assembly.gif)

- 用户可以根据需要编辑数量。

## 最后一步

一旦使用树组件完成 BOM 结构，用户必须提交 BOM 创建器。提交 BOM 创建器后，系统将使用后台作业生成 BOM。

![](/files/submit-bom.gif)
