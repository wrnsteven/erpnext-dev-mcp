---
original_url: https://docs.frappe.io/erpnext/exotel_integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18
---

# Exotel 集成

此集成允许您将 Exotel 集成到您的 ERPNext 账户中。通过 Exotel 捕获的线索及其电话号码可以直接保存到您的 ERPNext。

## 1. 功能

在您的 ERPNext 账户中跟踪来电。

- 当收到来电时，向员工显示现有线索/客户信息弹窗。

## 2. 如何设置

### 2.1 设置您的 Exotel 账户

- 登录您的 Exotel 账户并进入 App Bazar。

- 为新流程创建一个新应用。

- 按您希望的方式设置流程。

- 在您的连接 API 中的"创建弹窗..."下，粘贴以下 URL：
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

![连接小程序](images/218_connect_applet.png)
![通话弹窗部分](images/218_create_popup_section.png)

注意：将 URL 中的`<your-site>`替换为您的站点名称。例如，如果站点名称是 frappe.erpnext.com，则 URL 将是：
`https://frappe.erpnext.com/api/method/erpnext.erpnext_integrations.exotel_integration.handle_incoming_call`

- 然后在"通话结束后"下添加一个 Passthru 小程序，并粘贴以下 URL：
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_end_call`

![对话结束后部分](images/218_after_conversation_ends_section.png)

![通话结束部分](images/218_passthru_end_call.png)

注意：确保勾选"使 Passthru 异步"。

- 同样，在"如果无人接听..."部分下添加一个 Passthru 小程序，并粘贴以下 URL：
`https://<your-site>/api/method/erpnext.erpnext_integrations.exotel_integration.handle_missed_call`

![无响应部分](images/218_no_response.png)

![通话结束部分](images/218_passthru_missed_call.png)

注意：确保勾选"使 Passthru 异步"。

- 保存流程。

- 现在将此新创建的应用分配给您用于接收业务通话的 ExoPhone。

### 2.2 在 ERPNext 中设置

- 从 Awesome Bar，进入"Exotel 设置"。

- 设置您的"Exotel SID"和"Exotel Token"。您可以在您的 [Exotel 仪表板](https://my.exotel.com/apisettings/site#api-credentials) 上找到您的 Exotel API 密钥和令牌。

- 进入通信媒介。

- 添加您的 ExoPhone 并安排该号码。根据此安排，员工将收到弹窗。