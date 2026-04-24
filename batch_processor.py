#!/usr/bin/env python3
"""
文档批量处理调度器
- 处理 id=1 时等待用户确认
- 确认后批量处理剩余页面
"""

import json
import os
import sys
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
except ImportError:
    print("请安装 requests: pip install requests")
    sys.exit(1)

# 配置
WORKSPACE = Path("/home/xyw/erpnext")

# 根据 JSON 文件名确定子目录
def get_dirs_for_json(json_filename: str):
    """根据 JSON 文件名返回对应的目录路径"""
    if "erpnext" in json_filename.lower():
        base = WORKSPACE / "erpnext"
    else:
        base = WORKSPACE / "framework"
    return {
        "source": base / "source",
        "images": base / "images",
        "md": base / "md",
        "doc_cn": base / "doc_cn",
        "base": base
    }

# 翻译规则（来自 workflow.md）
TRANSLATION_RULES = """### 翻译规则（大模型执行时严格遵守）

#### ⚠️ 核心原则：禁止对照表翻译
- 禁止使用任何形式的术语对照表、映射表、词对词替换、硬编码替换。
- 必须完全依赖大模型对上下文的理解，进行自然、流畅的翻译。
- 术语库仅作为背景参考，用于识别"哪些词必须保留原文"，绝不能用于机械替换。

#### 必须原样保留的内容（不翻译）
- 所有代码、命令、文件路径、文件名、环境变量、命令输出
- 所有超链接（URL 及 Markdown 链接格式）
- 所有图片语法（Markdown `![alt](url)` 保持原样，但**后续要将 url 替换为本地路径**）
- Frappe/ERPNext 专有术语（见下方列表）
- 版本号、哈希值、占位符、默认值（`default: 'red'` 中的 `'red'`）

#### 必须保留原文的 Frappe/ERPNext 术语
`Frappe`, `ERPNext`, `bench`, `DocType`, `doctype`, `report`, `page`, `dashboard`, `workspace`, `web form`, `print format`, `letter head`, `role`, `permission`, `frappe.db`, `frappe.get_doc`, `frappe.call`, `hooks.py`, `patches.txt`, `doc_events`, `cur_frm`, `frm`, `Jinja`, `Nginx`, `MariaDB`, `Redis`, `octicons`, `Sales Invoice`, `Stock Entry`, `Leave Application`, `Payment Entry`, `BOM`, `Work Order`, `Project`, `Task`, `Issue`, `Customer`, `Supplier`, `Employee` 等。

#### 需要翻译的内容
- 普通英文句子、段落、标题、列表说明文字、表格中的非术语内容。
- 界面提示文本：翻译提示部分，保留默认值原样。

#### 特殊处理
- 图片链接：将原始 URL 替换为本地相对路径 `images/{id}_{文件名}`。注意：这个替换由大模型在翻译时完成，不要留给调度器。
- 元信息块：在 Markdown 文件开头添加：
  ```yaml
  ---
  original_url: [原始URL]
  translated_by: AI (Claude Code)
  translation_date: [当前日期 YYYY-MM-DD]
  ---
  ```

#### 输出格式要求
- 输出应为两个部分：第一部分是中文 Markdown 内容，第二部分是中文 HTML 内容（可以用分隔线 `---` 分开，或分别标注 `## MARKDOWN` 和 `## HTML`）。
- 保持原文的 Markdown 格式（标题、代码块、列表、表格等）。
"""


def setup_directories(dirs: dict):
    """确保所有目标目录存在"""
    for key in ["source", "images", "md", "doc_cn"]:
        d = dirs[key]
        d.mkdir(parents=True, exist_ok=True)
        print(f"目录已就绪: {d}")


def load_urls(json_path: Path) -> dict:
    """加载 URL 列表"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_urls(json_path: Path, data: dict):
    """保存 URL 列表"""
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def sanitize_filename(name: str) -> str:
    """清理文件名，移除不合法字符"""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = name.strip("._")
    return name[:100]


def fetch_html(url: str) -> str:
    """抓取页面 HTML"""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text


def extract_main_content(html: str) -> str:
    """提取页面主要内容区域（简单实现）"""
    # 移除 script 和 style 标签
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)

    # 尝试提取 article 或 main 内容
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if article_match:
        return article_match.group(1)

    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
    if main_match:
        return main_match.group(1)

    # 如果没找到，返回整个 body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    if body_match:
        return body_match.group(1)

    return html


def html_to_markdown(html_content: str) -> str:
    """将 HTML 转换为 Markdown（简单实现）"""
    # 标题转换
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n\n', html_content, flags=re.IGNORECASE)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n\n', md, flags=re.IGNORECASE)

    # 段落和换行
    md = re.sub(r'<br\s*/?>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'</p>', '\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<p[^>]*>', '', md, flags=re.IGNORECASE)

    # 列表
    md = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<ul[^>]*>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'</ul>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<ol[^>]*>', '\n', md, flags=re.IGNORECASE)
    md = re.sub(r'</ol>', '\n', md, flags=re.IGNORECASE)

    # 代码块
    md = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', md, flags=re.DOTALL | re.IGNORECASE)
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md, flags=re.DOTALL | re.IGNORECASE)

    # 图片
    md = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', r'![\2](\1)', md, flags=re.IGNORECASE)
    md = re.sub(r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>', r'![](\1)', md, flags=re.IGNORECASE)

    # 链接
    md = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', md, flags=re.DOTALL | re.IGNORECASE)

    # 移除剩余 HTML 标签
    md = re.sub(r'<[^>]+>', '', md)

    # 清理多余空白
    md = re.sub(r'\n{3,}', '\n\n', md)
    md = md.strip()

    return md


def extract_text_only(html_content: str) -> str:
    """从 HTML 提取纯文本"""
    # 移除 script 和 style
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # 替换换行和段落
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'</div>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<div[^>]*>', '', text, flags=re.IGNORECASE)

    # 列表项
    text = re.sub(r'<li[^>]*>', '\n- ', text, flags=re.IGNORECASE)
    text = re.sub(r'</li>', '', text, flags=re.IGNORECASE)

    # 移除剩余 HTML
    text = re.sub(r'<[^>]+>', '', text)

    # 解码 HTML 实体
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')

    # 清理空白
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def download_images(html_content: str, url_id: int, page_url: str, dirs: dict) -> dict:
    """下载页面中的图片，返回 URL 到本地路径的映射"""
    img_map = {}

    # 查找所有图片标签
    img_pattern = r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>'
    img_urls = re.findall(img_pattern, html_content, re.IGNORECASE)

    # 也查找 Markdown 图片
    md_img_pattern = r'!\[([^\]]*)\]\(([^)\s]+)\)'
    md_img_urls = re.findall(md_img_pattern, html_content)
    for alt, img_url in md_img_urls:
        if img_url not in img_urls:
            img_urls.append(img_url)

    for idx, img_url in enumerate(img_urls):
        if not img_url or img_url.startswith('data:'):
            continue

        # 转换为绝对 URL
        img_url = urljoin(page_url, img_url)

        # 解析文件名
        parsed = urlparse(img_url)
        filename = os.path.basename(parsed.path)
        if not filename or '.' not in filename:
            filename = f"img_{idx}"

        # 清理文件名
        filename = sanitize_filename(filename)
        local_filename = f"{url_id}_{filename}"
        local_path = dirs["images"] / local_filename

        try:
            response = requests.get(img_url, timeout=15, stream=True)
            response.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            img_map[img_url] = f"images/{local_filename}"
            print(f"  下载图片: {local_filename}")
        except Exception as e:
            print(f"  下载图片失败 {img_url}: {e}")

    return img_map


def save_source_html(url_id: int, name: str, html: str, dirs: dict):
    """保存原始 HTML"""
    filename = f"{url_id}_{sanitize_filename(name)}.html"
    filepath = dirs["source"] / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  保存原始 HTML: {filename}")


def build_translation_prompt(original_content: str, url: str, url_id: int) -> str:
    """构建翻译提示词"""
    date_str = datetime.now().strftime('%Y-%m-%d')
    prompt = f"""你是一名网站文档翻译专家，严格遵循下面的翻译规则。

{TRANSLATION_RULES}

[原始页面内容如下，请翻译：]
{original_content}

---
original_url: {url}
translated_by: AI (Claude Code)
translation_date: {date_str}
---"""
    return prompt


def parse_translation_result(result: str) -> tuple:
    """解析翻译结果，返回 (markdown, html) 元组"""
    # 尝试分隔 MARKUP 和 HTML 部分
    parts = result.split('## HTML')
    if len(parts) == 2:
        md_content = parts[0].replace('## MARKDOWN', '').strip()
        html_content = parts[1].strip()
    else:
        # 尝试用分隔线
        parts = result.split('---')
        if len(parts) >= 3:
            md_content = parts[0].strip()
            html_content = parts[-1].strip()
        else:
            md_content = result
            html_content = result

    # 如果 HTML 内容看起来像 Markdown（没有 HTML 标签），尝试转换
    if '<' not in html_content[:500]:
        # 简单转换：标题
        html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
        html_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
        # 段落
        html_content = re.sub(r'\n\n+', '</p><p>', html_content)
        html_content = f'<p>{html_content}</p>'

    return md_content, html_content


def save_translations(url_id: int, name: str, markdown: str, html: str, dirs: dict):
    """保存翻译结果"""
    safe_name = sanitize_filename(name)

    # 保存 Markdown
    md_filename = f"{url_id}_{safe_name}.md"
    md_path = dirs["md"] / md_filename
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"  保存 Markdown: {md_filename}")

    # 保存 HTML
    html_filename = f"{url_id}_{safe_name}.html"
    html_path = dirs["doc_cn"] / html_filename
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  保存中文 HTML: {html_filename}")


def update_url_status(json_path: Path, url_id: int, status: str):
    """更新 URL 状态"""
    data = load_urls(json_path)
    for url_entry in data['urls']:
        if url_entry['id'] == url_id:
            url_entry['status'] = status
            url_entry['processed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    data['completed'] = sum(1 for u in data['urls'] if u['status'] == 'completed')
    data['pending'] = sum(1 for u in data['urls'] if u['status'] == 'pending')
    data['failed'] = sum(1 for u in data['urls'] if u['status'] == 'failed')
    save_urls(json_path, data)


def process_single_url(json_path: Path, url_entry: dict, dirs: dict) -> bool:
    """处理单个 URL"""
    url_id = url_entry['id']
    url = url_entry['url']
    name = url_entry['name']

    print(f"\n{'='*60}")
    print(f"处理 ID={url_id}: {name}")
    print(f"URL: {url}")
    print('='*60)

    try:
        # 1. 抓取 HTML
        print("步骤 1: 抓取页面...")
        raw_html = fetch_html(url)

        # 2. 提取主要内容
        print("步骤 2: 提取主要内容...")
        main_content = extract_main_content(raw_html)

        # 3. 保存原始 HTML
        print("步骤 3: 保存原始 HTML...")
        save_source_html(url_id, name, main_content, dirs)

        # 4. 下载图片
        print("步骤 4: 下载图片...")
        download_images(main_content, url_id, url, dirs)

        # 5. 提取文本并构建翻译提示
        print("步骤 5: 准备翻译...")
        text_content = extract_text_only(main_content)
        markdown_content = html_to_markdown(main_content)

        prompt = build_translation_prompt(markdown_content, url, url_id)

        # 6. 显示翻译提示（供用户确认或后续处理）
        print("步骤 6: 翻译提示已准备，长度:", len(prompt), "字符")

        # 保存提示到临时文件，供 Claude 调用
        prompt_file = dirs["base"] / f"prompt_{url_id}.txt"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"  翻译提示已保存到: {prompt_file}")

        # 7. 更新状态为待翻译
        update_url_status(json_path, url_id, 'pending_translation')

        return True

    except Exception as e:
        print(f"处理失败: {e}")
        update_url_status(json_path, url_id, 'failed')
        return False


def process_first_then_wait(json_path: Path, dirs: dict):
    """处理第一个 URL，等待用户确认"""
    data = load_urls(json_path)
    first_url = data['urls'][0]

    success = process_single_url(json_path, first_url, dirs)

    if success:
        print("\n" + "="*60)
        print("页面 id=1 处理完成！")
        print(f"请检查生成的 prompt_1.txt 和 {dirs['base']}/source/ 目录下的文件")
        print("确认质量合格后回复'继续'以处理剩余页面")
        print("="*60)

    return success


def batch_process(json_path: Path, dirs: dict, start_id: int = 2):
    """批量处理后续 URL"""
    data = load_urls(json_path)

    pending_urls = [u for u in data['urls'] if u['id'] >= start_id and u['status'] in ['pending', 'failed']]

    print(f"\n开始批量处理，共 {len(pending_urls)} 个页面")

    for idx, url_entry in enumerate(pending_urls, 1):
        print(f"\n[{idx}/{len(pending_urls)}] 进度")
        try:
            process_single_url(json_path, url_entry, dirs)
            time.sleep(1)  # 避免请求过快
        except Exception as e:
            print(f"处理 ID={url_entry['id']} 失败: {e}")
            update_url_status(json_path, url_entry['id'], 'failed')

    print("\n批量处理完成！")


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  python batch_processor.py <json文件> [start_id]")
        print("  python batch_processor.py framework_urls.json")
        print("  python batch_processor.py erpnext_urls.json")
        print("  python batch_processor.py framework_urls.json 2  # 从 ID=2 开始批量处理")
        sys.exit(1)

    json_file = sys.argv[1]
    json_path = Path(json_file)

    if not json_path.exists():
        # 尝试在 workspace 目录下查找
        json_path = WORKSPACE / json_file

    if not json_path.exists():
        print(f"文件不存在: {json_path}")
        sys.exit(1)

    # 根据 JSON 文件名获取对应的目录
    dirs = get_dirs_for_json(json_file)
    print(f"使用目录: {dirs['base']}")

    setup_directories(dirs)

    if len(sys.argv) >= 3:
        # 直接批量处理
        start_id = int(sys.argv[2])
        batch_process(json_path, dirs, start_id)
    else:
        # 首次执行：处理 id=1 并等待确认
        process_first_then_wait(json_path, dirs)


if __name__ == "__main__":
    main()
