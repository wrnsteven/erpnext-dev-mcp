ERPNext 提供通过名为 [Plaid](https://plaid.com/) 的服务同步银行账户的功能。请查看 [Plaid 常见问题](https://support-my.plaid.com/hc/en-us) 确认您的国家是否受支持。

如果您的实例已连接到 Plaid，您可以同步银行账户交易，无需手动导入 CSV 或 XLSX 文件。

## 设置

要授予 ERPNext 访问 Plaid 的权限，您需要在 `site_config.json` 文件中添加以下三个参数。

- `plaid_env`
- `plaid_public_key`
- `plaid_secret`

## 激活

要在实例上激活 Plaid，请在 Plaid Settings DocType 中点击"启用"按钮。

![图片](../../images/389_plaid_enable.gif)

激活后，您可以直接从银行对账仪表板创建新账户。

## 创建银行账户

要将您现有的银行账户关联到 ERPNext，请点击"关联新银行账户"并按照 Plaid 提供的步骤操作。

![图片](../../images/389_new_account_creation.gif)

## 银行同步

要将银行账户与 ERPNext 同步，请选择一个账户并点击"操作"按钮，选择"同步此账户"。

![图片](../../images/389_plaid_synchronization.gif)

同步基于"Bank Account" doctype 中可用的"上次集成日期"。

如果由于任何原因您需要重新执行同步，可以更改此日期并再次同步账户。由于所有银行交易都带有特定的交易 ID，同步将是增量进行的。

## 自动同步

您可以通过在 Plaid Settings 中选择"每小时同步所有账户"，允许 Plaid 每小时将您的银行账户与 ERPNext 同步。

---

original_url: https://docs.frappe.io/erpnext/plaid_integration
translated_by: AI (Claude Code)
translation_date: 2026-04-18