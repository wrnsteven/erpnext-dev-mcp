```markdown
---
description: 了解如何在 ERPNext 中设置和使用 LDAP（轻量级目录访问协议）进行集中式身份验证。
keywords: LDAP, 身份验证, 集成, 用户管理, 目录服务
---
```

# 轻量级目录访问协议（LDAP）集成

轻量级目录访问协议（LDAP）是一种被许多中小型组织使用的集中式访问控制系统。

通过设置 LDAP 服务，您可以使用 LDAP 凭据登录 ERPNext 账户。

## 1. 前置条件

要使用 LDAP，您需要先安装 `ldap3` Python 模块。为此，请在托管 ERPNext 实例的服务器上打开一个终端会话。进入 `frappe-bench` 目录。
运行命令：`./env/pip install ldap3`

现在您可以在 ERPNext 中启用 LDAP 服务了。

## 2. 设置 LDAP

要设置 LDAP，请进入

> 首页 > 集成 > LDAP 设置

有许多参数是必需的，用于允许 ERPNext 连接到 LDAP。它们是：

**LDAP 服务器 URL**：这是您 LDAP 服务器的 URL。必须采用 `ldap://yourserver:port` 或 `ldaps://yourserver:port` 的形式。

**基础可分辨名称（DN）**：这是拥有在 LDAP 服务器上查找用户详细信息权限的用户的可分辨名称。该用户应该是在 LDAP 服务器上仅有只读权限的用户。

**基础 DN 的密码**：这是上述用户的密码，用于在 LDAP 服务器上查找用户详细信息。

**用户组织单位**：这是 LDAP 服务器上所有用户的组织单位的可分辨名称，这些用户必须属于该组织单位才能登录 ERPNext。

**创建时的默认角色**：当用户在 ERPNext 中创建时，他们将在首次登录时被分配此默认角色。

**LDAP 搜索字符串**：此字段允许 ERPNext 将 ERPNext 登录屏幕上输入的用户/电子邮件与 LDAP 服务器进行匹配。例如，您可以使用电子邮件地址或用户名，取决于您的偏好。

必须以以下格式输入：`LDAPFIELD={0}`

Active Directory 用户名示例：`sAMAccountName={0}`

Open LDAP 用户名示例：`uid={0}`

- **LDAP 电子邮件字段**：指定包含用户电子邮件地址的 LDAP 字段。

Active Directory 和 Open LDAP 示例：`mail`

- **LDAP 用户名字段**：指定包含用户名的 LDAP 字段。

Active Directory 示例：`sAMAccountName`

Open LDAP 示例：`uid`

- **LDAP 名字段**：指定包含用户名字的 LDAP 字段。

Active Directory 示例：`givenName`

Open LDAP 示例：`sn`

还有许多其他非必填字段可用于将您的 LDAP 用户字段映射到 ERPNext 用户字段。它们是：

- 中间名
- 电话
- 手机

设置正确后，您可以点击顶部的 `已启用` 复选框。尝试启用 LDAP 时，ERPNext 将尝试连接到 LDAP 服务器以确保设置正确。如果失败，您将无法启用 LDAP，并将收到错误消息。

错误消息将指出需要解决的问题才能继续。

设置启用 LDAP 后，在登录页面上，系统将启用 **通过 LDAP 登录** 选项。

### 2.1 LDAP 安全

在 LDAP 安全部分，您有多种选项可以安全地连接到 LDAP 服务器。

##### SSL/TLS 模式

指定是否要在初始连接到 LDAP 服务器时启动 TLS 会话。

##### 需要可信证书

指定是否需要可信证书才能连接到 LDAP 服务器。

如果您要指定可信证书，则需要指定证书文件的路径。这些文件应放置在 ERPNext 服务器上，以下字段应为服务器上文件的绝对路径。
证书字段包括：

私钥文件路径

服务器证书路径

CA 证书文件路径

### 2.2 LDAP 组映射

ERPNext 还允许您自动将多个 LDAP 组映射到相应的 ERPNext 角色。
例如，您可能希望所有会计人员自动拥有"账户用户"角色。
请确保填写 LDAP 组字段以允许此操作。这是 LDAP 上用户对象中找到的 LDAP 字段，包含用户所属的所有组。

对于 Active Directory 和 Open LDAP，此字段应设置为 `memberOf`。

Open LDAP 可能需要在 LDAP 服务器上启用此字段。请参阅互联网上的示例以获取更多详细信息。

> 请注意，每次用户登录时都会检查所有 ERPNext 角色，并会从用户的权限中移除或添加到用户权限中。

在 LDAP 设置区域，有两个下拉菜单。

- **SSL/TLS 模式** - 将其设置为 **StartTLS** 以使用 StartTLS 连接到 LDAP 服务器。如果您的 LDAP 服务器不支持 StartTLS，将其设置为 StartTLS 将导致错误 `StartTLS is not supported`。如果收到此错误，请检查 LDAP 服务器上的配置。

- **需要可信证书** - 如果将其更改为 **是**，则 LDAP 服务器提供的证书必须被 Frappe/ERPNext 服务器信任。如果您更愿意使用自签名（不受信任）证书使用 StartTLS，请将其设置为 **否**。如果您不使用 StartTLS，则此设置会被忽略。

---

original_url: https://docs.frappe.io/erpnext/ldap-integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18