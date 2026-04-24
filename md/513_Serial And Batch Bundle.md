> 注意：用户必须为每个库存交易创建单独的 **Serial and Batch Bundle**。不能在多个库存交易中使用相同的 **Serial and Batch Bundle**。

从版本 15 开始，序列号/批次物品的"允许负库存"功能已被移除。从版本 15 起，即使在**库存设置**中启用了"允许负库存"，用户也无法对序列号/批次物品进行负库存交易。

在版本 15 中，我们引入了 **Serial and Batch Bundle**。此功能用于在库存交易中关联序列号/批次号。

在版本 15 之前，*序列号*字段是一个短文本字段，这意味着一个列可以容纳多个序列号。由于这种设计，存在很多数据完整性问题。为了解决这个问题，在版本 15 中我们将 *序列号*字段从短文本改为链接字段。由于我们无法在子表中添加子表，因此添加了一个新的 DocType：**Serial and Batch Bundle**，用于在入库/出库时选择多个序列号/批次号。

![图片](../../images/513_serial-and-batch-bundle.png)

## 工作原理

每当处理序列号/批次号时，用户需要创建一个 **Serial and Batch Bundle** 并将其链接到库存交易。用户必须为每笔交易创建单独的 **Serial and Batch Bundle**，不能将同一个 **Serial and Batch Bundle** 链接到多笔交易。

### 入库单自动创建 Serial and Batch Bundle

如果用户想要自动创建入库单的 **Serial and Batch Bundle**，必须确保为序列号物品设置了*序列号序列*，并且为批次物品启用了*自动创建新批次*复选框（并设置了*批次号序列*）。

#### 序列号

![图片](../../images/513_auto-serial-creation.png)

#### 批次号

![图片](../../images/513_auto-batch-creation.png)

配置完成后，当用户创建**采购收货**或类型为"物料入库"的**库存调整**时，系统将在记录提交时自动创建入库的 **Serial and Batch Bundle**。

![图片](../../images/513_auto-create-serial-batch-for-inward.gif)

### 出库单自动创建 Serial and Batch Bundle

如果用户想要自动创建出库单的 **Serial and Batch Bundle**，必须在**库存设置**中启用复选框"出库自动创建 Serial and Batch Bundle"。用户还可以在**库存设置**中设置"拣货序列号/批次依据"为"FIFO / LIFO / 到期日"。

![图片](../../images/513_auto-outward-configuration.png)

配置完成后，当用户创建**送货单**或类型为"物料出库"的**库存调整**时，系统将在记录提交时自动创建出库的 **Serial and Batch Bundle**。

![图片](../../images/513_auto-create-serial-batch-for-outward.gif)

### 入库单手动创建 Serial and Batch Bundle

对于 **Serial and Batch Bundle**，**序列号**和**批次**记录必须已存在于系统中。使用手动选项时，用户必须首先在系统中创建**序列号**/**批次**记录。用户可以使用 CSV 导入选项来创建**序列号**/**批次**记录。空白 CSV 模板可以通过序列号和批次选择器下载。

![图片](../../images/513_create-using-csv.png)

入库单手动创建 **Serial and Batch Bundle** 的完整演示如下：

![图片](../../images/513_manually-create-serial-no-inward.gif)

### 出库单手动创建 Serial and Batch Bundle

使用序列号和批次选择器，用户可以根据"FIFO / LIFO / 到期日"方法选择序列号/批次号。

![图片](../../images/513_serial-batch-selector-outward.png)

出库单手动创建 **Serial and Batch Bundle** 的完整演示如下：

![图片](../../images/513_manually-create-serial-no-outtward.gif)

### 使用 CSV 出库单创建 Serial and Batch Bundle

现在用户可以通过导入 CSV 文件来为出库单创建序列号和批次包。

![图片](../../images/513_Screenshot%202026-01-20%20at%2012.19.18%20PM.png)

## 序列号历史

要查看序列号历史，请参阅"序列号台账"报表。

![图片](../../images/513_Screenshot%202026-01-20%20at%201.15.35%20PM.png)

## 序列号/批次选择器

此功能用于手动选择序列号/批次。如果序列号/批次不存在，此弹出窗口也可用于自动创建。

![图片](../../images/513_serial-batch-selector.gif)

## 禁用序列号/批次选择器

如果用户不想使用序列号和批次选择器（弹出窗口），可以通过**库存设置**禁用。禁用方法：进入**库存设置** > 序列号和批次物品（标签页）> 启用*禁用序列号和批次选择器*，然后保存。

![图片](../../images/513_disable-serial-batch-selector.png)

## 旧的序列号/批次字段

许多客户要求我们保留旧的序列号和批次字段，以解决用户体验问题。为了响应这一需求，我们保留了旧的序列号/批次字段。这些字段仅用于输入序列号和批次。系统将在库存交易提交时自动创建 **Serial and Batch Bundle**。要启用此功能，用户必须导航到**库存设置**并启用*使用序列号/批次字段*选项（见下图）。

![图片](../../images/513_use-serial-batch-fields-global.png)

之后，当用户创建库存交易（例如**送货单**）时，系统将显示旧的序列号/批次字段。更多详情，请参阅下面的演示。

![图片](../../images/513_user-old-serial-batch-fieldsd.gif)

用户也可以在交易级别禁用旧的序列号/批次字段。

![图片](../../images/513_use-serial-batch-for-dn.gif)

## 创建自动包时更新序列号/批次

如果用户想要在创建 **Serial and Batch Bundle** 时自动更新序列号/批次字段中的序列号/批次，请进入**库存设置**并禁用*创建自动包时不更新序列号/批次*。

![图片](../../images/513_update-Serial-Batch-on-creation-of-auto-bundle.png)

场景：

- 用户在**库存设置**中启用了*使用序列号/批次字段*

- 用户想要为每个批次创建 **Serial and Batch Bundle**

- 用户在**物品**主数据中设置了自动创建批次。

- 提交**采购收货**时，系统已创建自动**批次**和 **Serial and Batch Bundle**，并在**采购收货**行项目中设置了*批次*和 *Serial and Batch Bundle* 字段。

- 更新批次值需要时间。如果想跳过此步骤，请在**库存设置**中启用*创建自动包时不更新序列号/批次*。

- 启用后，批次列保持空白，但 **Serial and Batch Bundle** 将包含自动创建的包的值。

## 如何使用 **Serial and Batch Bundle**

[https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s](https://www.youtube.com/watch?v=-VjZvRtdjDQ&t=820s)

---
original_url: https://docs.frappe.io/erpnext/serial-and-batch-bundle
translated_by: AI (Claude Code)
translation_date: 2026-04-18