---
original_url: https://docs.frappe.io/erpnext/blog_post
translated_by: AI (Claude Code)
translation_date: 2026-04-17
---

# 博客文章

**博客文章是你网站上的文章。**

博客是与大家分享关于你的业务想法的好方法。它有助于让你的客户和读者了解与你业务相关的最新消息。

在互联网时代，写作具有重要意义，因为当人们访问你的网站时，他们想了解你和你的产品。

要访问博客文章，请前往：

> 首页 > 网站 > 博客 > 博客文章

## 1. 如何创建博客文章

1. 转到博客文章列表，点击"新建"。
2. 输入标题、博客分类、博主和内容。
3. 启用"已发布"并点击"保存"。

博客简介是博客的简短描述，显示在标题之后、内容之前。

![](/files/new-blog-post.png)

你可以使用富文本、Markdown 或 HTML 编写博客。如果你想写简单的内容页面，富文本和 Markdown 是很好的选择。在此了解如何为你的博客[附加图片](erpnext/web-page#images)。

> 在几分钟内学习 Markdown，请访问 [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)。

![](/files/blog-post-in-markdown.png)
*Markdown 格式的博客文章*

通过侧栏中的"在网站上查看"查看你的博客文章。
![](/files/blog-post.png)
*博客文章*

如果你想禁用读者添加评论的功能，请勾选"禁用评论"选项。
![](/files/blog-post-disable-comments.png)

![](/files/blog-post-no-comments.png)
*评论功能已禁用*

## 2. 功能

### 2.1 博主

博主是可以发布博客的用户。要创建博主，请前往：

**首页 > 网站 > 博客 > 博主**。

你可以在此添加博主的简短简介并设置头像。

![](/files/blogger.png)
*博主*

预览将显示在博客文章的末尾。
![](/files/blogger-preview.png)
*博主预览*

### 2.2 博客分类

你可以将博客分组到分类中。要创建新的博客分类，请前往：

**首页 > 网站 > 博客 > 博客分类**。

![](/files/blog-category.png)
*博客分类*

如果你点击侧栏中的"在网站上查看"，你将被重定向到该分类下的博客列表。

![](/files/blog-category-web-view.png)
*博客分类 - 常规*

### 2.3 元标签

元标签是描述页面及其内容给搜索引擎或社交媒体平台的 HTML 标签。元描述提供网页的简短描述。

在 HTML 中，元描述标签的写法如下：

```html

```

在 SEO 部分，你可以为你的博客文章添加元描述和图片。当在 Google 搜索结果中列出时，ERPNext 将生成博客预览。

如果你将此部分留空，博客简介或博客的前 140 个字符将显示为元描述。同样，如果你将元图片留空，博客中的第一张图片将被选中。

![](/files/blog-post-seo-meta.png)
*博客文章 Google 搜索预览*

提交博客后，你还可以预览博客在 Facebook 或 Twitter 等社交媒体平台上分享时的样子。要检查这一点，请使用平台提供的调试工具：

- Facebook: [Sharing Debugger](https://developers.facebook.com/tools/debug/)
- Twitter: [Card Validator](https://cards-dev.twitter.com/validator)
- LinkedIn: [Post Inspector](https://www.linkedin.com/post-inspector/inspect/)

要检查帖子预览，只需在工具中输入网页/博客链接：

![](/files/blog-post-facebook-debugger.png)
*使用 Facebook 的 Sharing Debugger 工具*

使用这些工具，你可以优化博客文章以便分享。
