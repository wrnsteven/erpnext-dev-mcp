---
original_url: https://docs.frappe.io/erpnext/aws_s3
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 将备份上传到 Amazon S3

> 注意：如果你使用的是 Frappe Cloud 用户，系统会自动为你创建本地和异地备份：https://frappecloud.com/docs/sites/backups

## 前置条件

- [Email Account](erpnext/email-account)

要接收失败和成功备份的邮件通知，请首先创建一个 **Email Account**。

## 创建 S3 存储桶并设置访问权限

1. 创建一个新的 S3 存储桶。

在存储桶设置中，启用"阻止所有公开访问"以保持你的数据私密性。可以根据需要自由启用加密、版本控制或对象锁定（请参阅 [Amazon 文档](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)）。

2. 打开身份和访问管理（IAM）。

3. 为" S3 "服务创建一个新策略，允许操作" ListBucket "和" PutObject "。

![AWS "Create Policy" 截图](/files/s3-backup-policy.png)

或者，使用 JSON 编辑器：

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::YOUR TARGET BUCKET"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "YOUR SERVER IP"
                }
            }
        }
    ]
}
```

4. 创建一个用于编程访问的新用户。

![AWS "Add User" 截图](/files/s3_backup_add_user.png)

5. 将你创建的策略附加到新用户。
6. 复制用户的访问密钥和密钥。

要自动删除旧备份或将其移动到更便宜的存储类别，请查看 [lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)。

## 使用 Minio 创建一个 Hetzner 存储桶

> 大写字母是你可以自由选择的变量。在本例中，我们使用 region nbg1（Nuremberg）。

1. 在 Hetzner Console 的 `https://console.hetzner.com/projects/YOUR_PROJECT/security/s3-credentials` 处创建一些 S3 访问凭证：密钥和密钥。
2. [安装 Minio](https://github.com/minio/minio)
3. 配置 Minio 访问你的 Hetzner 存储桶：`mc alias set MY_ALIAS https://nbg1.your-objectstorage.com YOUR_S3_KEY YOUR_S3_SECRET`
4. 创建一个启用对象锁定的存储桶：`mc mb MY_ALIAS/BUCKET_NAME --with-lock --region nbg1`。这确保你不会意外删除备份。
5. 将对象锁定周期设置为 90 天：`mc retention set GOVERNANCE 90d --default MY_ALIAS/BUCKET_NAME`
6. 检查一切是否配置正确：`mc retention info --json --default MY_ALIAS/BUCKET_NAME`
7. 在 **S3 Backup Settings** 中输入配置：
   - *Endpoint URL*: https://nbg1.your-objectstorage.com/
   - *Bucket Name:* `BUCKET_NAME`
   - *Access Key ID*: `YOUR_S3_KEY`
   - *Access Key Secret*: `YOUR_S3_SECRET`

## 设置 ERPNext

- 打开 **S3 Backup Settings**。
- 勾选"启用自动备份"。
- 粘贴来自 AWS 的访问密钥和密钥。
- 设置一个电子邮件地址，用于在备份失败时接收通知。如果你也希望在备份成功时收到邮件，请启用"发送备份成功邮件"。
- 指定你在步骤 1 中创建的存储桶名称。
- 选择你希望多久拍摄和上传一次备份。可以选择从每月到每天。如果只想进行手动备份，请将频率设置为"无"。

![ERPNext 中的 S3 Backup Settings](/files/s3_backup_settings.png)

## 从版本化存储桶恢复已删除的文件

- 列出所有文件版本：`mc ls -r --versions MY_ALIAS/BUCKET_NAME/`
- 下载特定版本：`mc get --vid TARGET_VERSION_ID MY_ALIAS/BUCKET_NAME/20260415_162402/20260415_162402-company_frappe_cloud-database.sql.gz ~/Downloads`
