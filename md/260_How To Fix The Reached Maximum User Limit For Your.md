您的 ERPNext 订阅取决于您订阅的 System User 数量。一旦超过该限制，系统将不允许您再创建任何用户。例如，您订阅了 10 个用户。如果您的账户中已经创建了 10 个 System User，系统将不允许您创建第 11 个 System User，您将收到以下消息。

![图片](../../images/260_oP3RzNx.png)

要解决这个问题，您可以：

购买新用户或

禁用当前用户

但是，有时候即使您还没有用完订阅计划中的 System User 数量，仍然可能遇到此问题。例如，您的配额是 5 个 System User，而您只创建了 3 个用户，但在创建第 4 个用户时却收到了上述消息。原因是某些用户的"Simultaneous Sessions"字段值大于 1。

每个并发会话都被视为 1 个 System User。例如，如果您创建了 3 个用户，其中一个用户的"Simultaneous Session"设置为 3，那么您实际上有 5 个用户，即 3 + 1 + 1 = 5 个并发会话/System User。

要允许系统创建更多用户，您需要减少这些用户的并发会话数。为此，请进入该用户的个人资料，在 Security Settings 下相应地设置/减少"Simultaneous Session"的值。

![图片](../../images/260_YQQ8cHw.png)

**注意：** 您仍然可以创建 Website User，因为没有数量限制。