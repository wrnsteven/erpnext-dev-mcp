---
original_url: https://docs.frappe.io/erpnext/bom_update_tool
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# BOM Update Tool

**使用 BOM Update Tool，你可以替换子装配 BOM 并更新所有父 BOM 的成本。**

使用此工具，你可以替换链接到父 BOM 的子装配项目的现有 BOM。系统将在所有使用过该 BOM 的父 BOM 中更新新的 BOM。你需要先创建一个新的 BOM。

要使用 BOM Update Tool，请前往：

> 首页 > 制造 > 工具 > BOM Update Tool

## 1. 如何使用 BOM Update Tool

让我们考虑一个场景来更好地理解这一点。

假设一家公司生产电脑，电脑的物料清单如下：

1. 显示器
2. 键盘
3. 鼠标
4. CPU

在上述所有项目中，CPU 是单独装配的。因此，将为 CPU 创建单独的 BOM。CPU 的 BOM 包含以下项目。

1. 250 GB 硬盘
2. 主板
3. 处理器
4. SMTP
5. DVD 播放器

如果需要在 CPU BOM 中添加更多项目或编辑现有项目，请为其创建新的 BOM。

1. 950 GB 硬盘
2. 主板
3. 处理器
4. SMTP
5. DVD 播放器

选择子装配项目的当前 BOM 和新 BOM：

![](/files/bom-update-tool.png)

要更新所有父 BOM 中的新 BOM（其中 CPU 被选为子装配），你可以使用 **Replace** 按钮。

点击 Replace 按钮后，成品（电脑）的 BOM 中旧的 CPU BOM 将被新的 BOM 替换。

**BOM Replace Tool 是否可以替换父 BOM 中的展开项目？**

不可以，没有自己 BOM 的展开项目无法在父 BOM 中替换。例如，如果显示器项目没有子装配，则无法使用此工具进行更新。要更新展开项目，你应该取消并修订当前 BOM，或为成品创建新的 BOM。

## 更新 BOM 成本

使用按钮 **Update latest price in all BOMs**，你可以根据原材料的最新采购价格/价格表汇率/估值汇率更新所有物料清单的成本。如果你更新的 BOM 中的材料有不同的汇率，这将非常有用。

点击此按钮后，系统将创建一个后台进程来更新所有 BOM 的成本。此过程通过后台作业处理，因为更新所有 BOM 可能需要几分钟时间（取决于 BOM 数量）。

此功能也可以每天自动执行。为此，你需要在 Manufacturing Settings 中启用 "Update BOM Cost Automatically"。
