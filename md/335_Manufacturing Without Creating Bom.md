**建议使用 BOM 进行生产以保持一致性并避免重复工作。**
但是，如果您希望手动执行，替代方案是创建库存转移：

1) 创建一条**库存转移**，将**用途**设置为**发料到生产**。
![图片](../../images/335_EsxLtl4.png)

2) 创建一条**库存转移**，将**用途**设置为**生产**，其中被生产的物料将设置目标仓库，而其他物料（原材料）将设置来源仓库。
![图片](../../images/335_voUKccc.png)
*蓝点：物料正在接收。*
*橙点：物料正在发出。*

---
original_url: https://docs.frappe.io/erpnext/manufacturing-without-creating-bom
translated_by: AI (Claude Code)
translation_date: 2026-04-18