---
original_url: https://docs.frappe.io/erpnext/bom_stock_analysis
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# BOM Stock Analysis

BOM Stock Analysis 是 ERPNext 中的一个制造报表，用于告诉你对于给定的物料清单（BOM），你是否有足够的原材料来完成生产运行。

该报表有两种模式：

1. 详细模式 - 根据要生产的成品项目，提供库存可用量、短缺量和采购价格的详细分解
2. 汇总模式 - 给定 BOM 和仓库，告诉你实际可以生产多少成品

要访问该报表：

> 首页 > 制造 > 报表 > BOM Stock Analysis

## Detailed Mode

此模式可用于当你有固定的生产目标并想知道哪些原材料有库存、哪些短缺、以及弥补差距需要多少成本。

> **Note**
> 在 **FG Item to make** 中直接输入值会进入详细模式

最大可生产项目定义了在原材料可用性的基础上可生产的最大可能数量。绿色表示可以根据要生产的数量生产成品。如果可生产的成品数量少于要求数量，则值会变为红色。

![](/files/image0bb381.png)

## Summarised Mode

此模式可用于快速回答诸如"我们现在可以生产多少成品？"这样的问题，而无需指定生产目标。要进入此模式，我们保持 **Fg Item to Make** 为空，并定义仓库和 BOM。

![](/files/image5f53bd.png)
