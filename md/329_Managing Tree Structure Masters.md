ERPNext 中的部分主数据以树形结构进行管理。树形结构的主数据允许您设置父主数据，以及在该父主数据下方的子主数据。通过设置这种结构，您可以生成智能报表，并在层级结构的每个层级追踪增长情况。

以下是部分以树形结构进行管理的主数据列表。

- Chart of Accounts
- Chart of Cost Centers
- Customer Group
- Territory
- Sales Person
- Item Group

以下是在树形结构主数据中管理和创建记录的操作步骤。我们以 Territory 主数据为例来了解树形结构主数据的管理方法。

#### 步骤 1：进入主数据

`Selling > Setup > Territory`

#### 步骤 2：父级 Territory

![图片](../../images/329_territory-2.png)

点击父级 Territory 后，您将看到在其下方添加子级 Territory 的选项。所有默认的 Territory 组都列在名为"All Territories"的父级组下。您可以在其下方进一步添加父级或子级 Territory 组。

#### 步骤 3：添加新的 Territory

点击"Add Child"后，弹出的对话框将提供两个字段。

**Territory Group Name**

Territory 将使用此处提供的名称进行保存。

**Group Node**

如果将 Group Node 选择为"Yes"，则该 Territory 将被创建为父级，这意味着您可以进一步在其下方创建子级 Territory。如果选择"No"，则它将成为子级 Territory，您将能够在其他主数据和交易中选择它。

![图片](../../images/329_territory-1.gif)

以下是子级 Territory 如何列在父级 Territory 下方的示例。

![图片](../../images/329_territory-3.png)

遵循以上步骤，您也可以在 ERPNext 中管理其他树形结构的主数据。