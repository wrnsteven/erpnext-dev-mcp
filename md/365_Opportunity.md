---
original_url: https://docs.frappe.io/erpnext/opportunity
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

**商机是一个合格的潜在客户。**

当你得到潜在客户正在寻找你提供的产品/服务的提示时，你可以将该潜在客户转化为商机。你也可以针对现有客户创建商机。一个潜在客户或客户可以对应多个商机。

要访问商机列表，请转到：

> 主页 > CRM > 销售管道 > 商机

## 1. 如何创建商机

- 进入商机列表，点击"添加商机"。

- 在"商机来源"中，如果商机来自潜在客户，请选择"潜在客户"。

![图片](../images/365_creating-opportunity.gif)

- 你也可以进入状态为"开放"的潜在客户，然后在下图所示的**创建**下拉菜单中选择"商机"。

![图片](../images/365_lead-to-opportunity.png)

在"商机来源"中，如果商机来自客户，请选择"客户"。

选择商机类型。这表示商机的广泛类别，如销售、支持、维护等。

你可以在"销售"部分添加更多详细信息，如商机金额、转化概率、货币等。

你可以通过勾选"带物料"复选框来录入所需产品/服务的详细信息，并在"物料"部分添加物料和数量详情。

![图片](../images/365_item-details-in-opportunity.png)

- 在"来源"部分输入商机的来源。

## 2. 功能

### 2.1 跟进提醒

及时与商机方联系并建立关系非常重要。你可以设置"下次联系日期"和"下次联系人"字段，系统将为"下次联系人"字段中选择的用户添加日历事件，并在指定日期显示通知。

### 2.2 自动分配商机给销售人员

> 版本 12 中引入

你可以定义[分配规则](/erpnext/assignment-rule)来自动将商机分配给销售人员。

![图片](../images/365_opportunity-assignment-rule.png)

### 2.3 自动关闭商机

如果你在一定天数内未收到商机的回复，你可能希望该商机被自动关闭。

你可以在[销售设置](/erpnext/selling-settings)中设置天数。

![图片](../images/365_auto-close-opportunities.png)

### 2.4 创建报价单

你可以从**制作**下拉菜单创建[报价单](/erpnext/quotation)。相关字段值将被复制过来。

![图片](../images/365_create-quotation-from-opportunity.png)

### 2.5 创建供应商报价单

你可能需要根据客户需求从供应商处获取报价单，然后基于该报价单为客户准备报价。使用 ERPNext，你可以直接从商机制作[供应商报价单](/erpnext/supplier-quotation)。

> 最佳实践：潜在客户和商机通常被称为你的"销售管道"，如果你想预测未来将获得多少业务，就需要跟踪这些数据。跟踪即将到来的业务以便调整资源总是一个好主意。

### 2.6 记录丢失原因和竞争对手

当商机丢失时，你可以记录原因、竞争对手和丢失的详细原因。这将帮助你长期分析趋势，并识别组织各领域改进所需的洞察。

![图片](../images/365_opportunity-lost-reason.png)

### 2.7 首次响应时间

当你发送对商机的第一封回复邮件时，系统会计算首次响应时间并显示在字段中。

系统会生成一份名为"商机首次响应时间"的报告。了解更多详情请阅读 [CRM 报表](/erpnext/crm_reports)。

### 3. 相关主题

- [报价单](/erpnext/quotation.html)

- [客户](/erpnext/customer)

- [潜在客户](/erpnext/lead)

- [供应商报价单](/erpnext/supplier-quotation)

- [潜在客户、联系人和客户之间的区别](/erpnext/difference_between_lead_contact_and_customer)