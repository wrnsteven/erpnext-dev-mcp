---
original_url: "https://docs.frappe.io/erpnext/appointment-booking-settings"
translated_by: "Claude"
translation_date: "2026-04-17"
---

# 预约预订设置

您可以在预约预订设置中找到与预订预约相关的所有设置。

<img src="/images/38_appointment-booking-settings.png" alt="Appointment Booking Settings" />

## 1. 启用预约调度

此复选框将启用预约调度，并同时为网站用户（您的客户）启用<code>/book_appointment</code>路由。您的客户将看到一个门户视图。了解更多，请访问<a href="/erpnext/appointment">预约页面</a>

## 2. Agent 详情

在本节中，您可以添加有关 Agent 的详细信息，例如他们的工作时间和假期。

### 2.1 时段可用性

在这里您可以设置 Agent 参加预约的时间段。这是按每周的每一天设置的。每一行代表一个连续的时间块，您可以为每周的每一天创建多个条目。

例如，如果您的 Agent 周一至周五工作，时间是上午9点到下午5点，但下午1:30有半小时的午餐休息。您需要为每一天创建两个条目。一个从上午9点到下午1:30，另一个从下午2点到5点。

### 2.2 Agent

这是将自动分配给预约的 Agent 列表。一个时间段可以存在的预约数量也取决于此列表中的员工数量。

### 2.3 假日列表

您可以在此处链接一个<a href="https://erpnext.com/docs/v13/user/manual/en/human-resources/holiday-list">假日列表</a>以应用于预约计划。如果当天是假期，则不允许在该天预约。

## 3. 预约详情

本节包含预约本身的详细信息。

### 3.1 预约时长（分钟）

预约时长（分钟）。这用于为网络门户计算预约时间段。更改此设置不会影响在此之前创建的预约。

### 3.2 通过电子邮件通知

启用此复选框将在预约当天向预约参与者（即您的员工和客户）发送电子邮件。更改此复选框不会影响在此之前创建的预约。

### 3.3 预约可以提前预订的天数

这是可以提前预订预约的天数。如果上述假日列表结束日期早于使用此数字计算的日期，预约调度将在假日列表结束时停止。

## 4. 成功设置

### 4.1 成功重定向 URL

这是用户在通过网页门户成功创建预约后将被重定向到的 URL。 通过 Desk UI 创建预约时不会发生此重定向。
留空则返回首页。这是相对于站点 URL 的，例如"about"将重定向到"https://yoursitename.com/about"