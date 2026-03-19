"""
自动化博客生成脚本
用于处理飞书机器人发送的技术链接，自动生成并发布博客
"""

import re
import json
from datetime import datetime
from pathlib import Path

# 配置
BLOG_DIR = Path(r"C:\Users\zx\openclaw\.openclaw\workspace\tech-blog")

# 分类关键词映射
CATEGORY_KEYWORDS = {
    "ai-infra": [
        "infrastructure", "infra", "部署", "架构", "基础设施",
        "k8s", "kubernetes", "docker", "容器", "服务网格",
        "service mesh", "监控", "observability", "可观测性",
        "分布式", "microservices", "微服务", "load balancing"
    ],
    "agent": [
        "agent", "代理", "agent framework", "langchain", "autogen",
        "autonomous agent", "智能体", "多智能体", "multi-agent",
        "agent orchestration", "agent tool", "function calling"
    ],
    "llm": [
        "llm", "大模型", "transformer", "attention", "预训练",
        "微调", "训练", "推理", "inference", "fine-tuning",
        "rlhf", "alignment", "tokenization", "embedding",
        "parameter", "model", "architecture", "scaling law"
    ]
}

def extract_url_from_message(message: str) -> str:
    """从消息中提取URL"""
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(url_pattern, message)
    return urls[0] if urls else None

def categorize_content(title: str, content: str) -> str:
    """根据标题和内容自动分类"""
    combined_text = f"{title} {content}".lower()

    scores = {
        "ai-infra": sum(1 for kw in CATEGORY_KEYWORDS["ai-infra"] if kw.lower() in combined_text),
        "agent": sum(1 for kw in CATEGORY_KEYWORDS["agent"] if kw.lower() in combined_text),
        "llm": sum(1 for kw in CATEGORY_KEYWORDS["llm"] if kw.lower() in combined_text)
    }

    # 返回得分最高的分类
    return max(scores.items(), key=lambda x: x[1])[0]

def generate_filename(title: str) -> str:
    """生成文件名"""
    # 移除特殊字符，只保留中文、字母、数字
    clean_title = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', title)
    # 替换空格和连字符
    clean_title = re.sub(r'[\s-]+', '-', clean_title).strip('-')
    # 添加日期
    date_str = datetime.now().strftime("%Y-%m-%d")
    return f"{date_str}-{clean_title[:50]}.md"

def create_blog_post(title: str, summary: str, core_points: list,
                     category: str, original_url: str, tags: list = None) -> str:
    """创建博客文章"""

    filename = generate_filename(title)
    category_dir = BLOG_DIR / "content" / category
    filepath = category_dir / filename

    # Front matter
    front_matter = f"""---
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")}
draft: false
categories: ["{category.capitalize()}"]
tags: {json.dumps(tags or [], ensure_ascii=False)}
original_url: "{original_url}"
---

"""

    # 内容
    content = front_matter + f"""## 核心要点

{summary}

## 技术亮点

"""

    for i, point in enumerate(core_points, 1):
        content += f"{i}. {point}\n"

    content += """

## 总结

这是一篇值得深入学习的技术文章，建议阅读原文了解更多细节。

---

*本文由 OpenClaw 飞书机器人自动生成*
"""

    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return str(filepath)

def process_link(url: str, title: str = None, content: str = None,
                 summary: str = None, core_points: list = None,
                 tags: list = None) -> dict:
    """处理技术链接，生成博客文章"""

    if not url:
        return {"success": False, "error": "未找到有效的URL"}

    if not title:
        title = f"技术文章 - {datetime.now().strftime('%Y-%m-%d')}"

    if not content:
        content = ""

    # 自动分类
    category = categorize_content(title, content)

    # 如果没有提供摘要，使用标题
    if not summary:
        summary = title

    # 如果没有提供核心要点，使用简单总结
    if not core_points:
        core_points = [summary]

    # 创建博客文章
    filepath = create_blog_post(
        title=title,
        summary=summary,
        core_points=core_points,
        category=category,
        original_url=url,
        tags=tags
    )

    return {
        "success": True,
        "category": category,
        "filepath": filepath,
        "title": title,
        "url": url
    }

# 使用示例
if __name__ == "__main__":
    # 测试用例
    result = process_link(
        url="https://example.com/article",
        title="Transformer模型架构详解",
        summary="本文深入讲解了Transformer模型的核心架构设计",
        core_points=[
            "Self-Attention机制的实现原理",
            "多头注意力机制的优势",
            "位置编码的必要性",
            "Encoder-Decoder架构设计"
        ],
        tags=["Transformer", "Attention", "LLM"]
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))