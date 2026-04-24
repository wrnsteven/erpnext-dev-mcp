### **POS 工作流程**

#### **开启 POS 收银会话**

- 进入 **POS** 工作区。

- 选择一个 **POS 配置文件**。

- 选择客户。

- 从商品列表中添加商品。

- 根据需要编辑数量。

*注意：* 您需要为库存影响设置一个默认仓库。如果商品和 POS 配置文件都定义了仓库，则 POS 配置文件的仓库优先。

**如何创建 POS 发票**

- 在 POS 屏幕上将商品添加到购物车。

- 如果需要编辑价格/折扣，请在 POS 配置文件中启用相应选项。

- 点击 **支付** 并选择支付方式。

- 提交 — 系统将创建一个 **POS 发票**。

**POS 开账条目**

在开始销售之前，使用 **开账条目** 开启一个会话。
这将设置会话的开始时间，并可在需要时记录期初现金。

**POS 结账条目**

在会话结束时：

- 进入 **POS 结账条目**

- 选择 POS 配置文件和结账期间

- 提交 — 系统将执行库存和会计分录。

**忠诚度积分集成**

ERPNext 支持将忠诚度计划关联到客户，实现以下功能：

- 在 POS 发票上赚取积分

- 结账时兑换积分

要设置忠诚度计划，请参阅 ++[忠诚度计划](https://docs.frappe.io/erpnext/user/manual/en/loyalty-points-redemption-in-pos)++ 文档。

---
original_url: https://docs.frappe.io/erpnext/pos-workflows
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---