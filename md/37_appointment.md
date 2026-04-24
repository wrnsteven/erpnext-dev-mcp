---
original_url: "https://docs.frappe.io/erpnext/appointment"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 预约

<strong>预约是您公司的 Lead 与员工之间的预先安排的会议。</strong>

Appointment 文档类型可用于安排和管理与 <a href="/erpnext/lead">Lead</a> 或 <a href="/erpnext/opportunity">Opportunity</a> 的互动。

要访问 Appointment 列表，请前往：

> Home > CRM > Sales Pipeline > Appointment

## 1. 前置条件

1. <a href="/erpnext/appointment-booking-settings">Appointment Booking Settings</a></li>
2. <a href="/hr/holiday-list">Holiday List</a></li>
3. <a href="/hr/employee">Employee</a></li>
4. <a href="/erpnext/lead">Lead</a></li>
5. <a href="/erpnext/email-account">Email</a></li>

## 2. 如何创建预约

1. 前往 Appointment 列表，点击新建</li>
2. 选择预约时间</li>
3. 输入客户详情</li>
4. 在关联文档中，如果您已经为客户创建了 Lead，可以在此处设置。否则系统将自动使用上一步中的客户详情创建一个新的 lead。</li>
5. 保存。
<img src="/images/37_new-appointment.png" alt="New Appointment" /></li>

### 2.1 通过网站创建预约

您的客户/Lead 可以使用网页 <code>yoursitename.com/book_appointment</code> 创建预约。

首先，他们需要设置日期和时间。
<img src="/images/37_appointment-webform.png" alt="Appointment Webform" /></p>

然后，添加更多详情：
<img src="/images/37_appointment-details.png" alt="Appointment Details" /></p>

系统会匹配客户邮箱与系统中的 Lead，如果找到，则会关联到该文档。
如果未找到 Lead，预约将被标记为"未验证"，并会向客户发送一封电子邮件以确认其邮箱地址

## 3. 功能

### 3.1 自动分配

预约会根据 <a href="/erpnext/appointment-booking-settings">Appointment Booking Settings</a> 中的 <code>Agents</code> 列表自动分配给员工。该预约当天的分配任务最少且在预定时间空闲的代理将被分配到该预约。

### 3.2 电子邮件确认

如果您的系统中没有匹配的 Lead，系统会向预约中的电子邮件地址发送一封电子邮件，以确认电子邮件地址是否有效。确认后，系统将同时创建一个新的 Lead 以及 Appointment。