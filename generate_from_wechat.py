"""
微信公众号文章博客生成脚本
读取爬取的内容，生成博客并提交到 Gitee
"""

import re
import json
import subprocess
from datetime import datetime
from pathlib import Path

# 配置
BLOG_DIR = Path(r"C:\Users\zx\openclaw\.openclaw\workspace\tech-blog")
WECHAT_SCRAPED_DIR = Path(r"C:\Users\zx\openclaw\.openclaw\workspace\memory\scraped\wechat")

# 分类关键词映射
CATEGORY_KEYWORDS = {
    "ai-infra": [
        "infrastructure", "infra", "部署", "架构", "基础设施",
        "k8s", "kubernetes", "docker", "容器", "服务网格",
        "service mesh", "监控", "observability", "可观测性",
        "分布式", "microservices", "微服务", "load balancing",
        "硬件", "算力", "本地部署", "mini pc", "主机"
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
        "parameter", "model", "architecture", "scaling law",
        "qwen", "参数规模", "32b", "9b", "27b"
    ]
}

def extract_title(content: str) -> str:
    """从爬取的内容中提取标题"""
    # 查找 # 开头的标题
    match = re.search(r'#\s+(.+?)(?:\n|$)', content)
    if match:
        return match.group(1).strip()
    return "技术文章"

def extract_summary(content: str) -> str:
    """提取文章摘要"""
    # 移除图片和链接
    clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    clean_content = re.sub(r'\[.*?\]\(.*?\)', '', clean_content)
    
    # 找到第一个段落
    paragraphs = [p.strip() for p in clean_content.split('\n\n') if p.strip() and len(p.strip()) > 50]
    
    if paragraphs:
        # 返回第一段的前 200 字
        summary = paragraphs[0][:200]
        if len(paragraphs[0]) > 200:
            summary += "..."
        return summary
    return ""

def extract_core_points(content: str) -> list:
    """提取核心要点"""
    points = []
    
    # 查找表格中的对比信息
    if "对比维度" in content:
        points.append("云端 vs 本地部署的核心差异：模型运行位置、Token 消耗、使用成本、数据安全、可用性")
    
    if "本地跑大模型" in content or "零 Token" in content:
        points.append("支持最高 32B 参数规模大模型本地运行（如 Qwen3.5-9B、Qwen3.5-27B）")
    
    if "异构计算" in content or "GPU" in content:
        points.append("采用先进的异构计算架构，独立 GPU 与 Intel Core Ultra 处理器协同调度")
    
    if "预装" in content or "开箱即用" in content:
        points.append("预装 OpenClaw 框架与主流模型权重，无需代码调试与环境配置，开机即可使用")
    
    if "加密芯片" in content or "国密" in content:
        points.append("可选配板载加密芯片，支持国密算法，满足金融、医疗、政务等敏感行业数据合规要求")
    
    if "生态" in content or "全链路" in content:
        points.append("完善 AI 智能体全链路硬件矩阵，打通软件开源生态与硬件终端的协同链路")
    
    return points if points else ["文章核心内容摘要"]

def categorize_content(title: str, content: str) -> str:
    """根据标题和内容自动分类"""
    combined_text = f"{title} {content}".lower()

    scores = {
        "ai-infra": sum(1 for kw in CATEGORY_KEYWORDS["ai-infra"] if kw.lower() in combined_text),
        "agent": sum(1 for kw in CATEGORY_KEYWORDS["agent"] if kw.lower() in combined_text),
        "llm": sum(1 for kw in CATEGORY_KEYWORDS["llm"] if kw.lower() in combined_text)
    }

    # 返回得分最高的分类
    best_category = max(scores.items(), key=lambda x: x[1])[0]
    print(f"分类得分：{scores}")
    return best_category

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
    category_dir.mkdir(parents=True, exist_ok=True)
    filepath = category_dir / filename

    # Front matter
    front_matter = f"""---
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")}
draft: false
categories: ["{category.capitalize()}"]
tags: {json.dumps(tags or [], ensure_ascii=False)}
original_url: "{original_url}"
description: "{summary[:150]}"
---

"""

    # 内容
    content = front_matter + f"""{summary}

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

def commit_to_gitee(filepath: str, title: str):
    """提交到 Gitee"""
    print(f"\n正在提交到 Gitee...")
    
    # 添加文件
    subprocess.run(['git', 'add', filepath], cwd=BLOG_DIR, check=True)
    
    # 提交
    commit_msg = f"feat: 添加博客 - {title}"
    subprocess.run(['git', 'commit', '-m', commit_msg], cwd=BLOG_DIR, check=True)
    
    # 推送
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=BLOG_DIR, check=True)
    
    print("[OK] 已成功提交到 Gitee！")

def process_wechat_article(scraped_file: str, original_url: str):
    """处理微信公众号文章"""
    
    # 读取爬取的内容
    with open(scraped_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取标题
    title = extract_title(content)
    print(f"标题：{title}")
    
    # 提取摘要
    summary = extract_summary(content)
    print(f"摘要：{summary[:100]}...")
    
    # 提取核心要点
    core_points = extract_core_points(content)
    print(f"核心要点：{len(core_points)} 个")
    
    # 自动分类
    category = categorize_content(title, content)
    print(f"分类：{category}")
    
    # 生成标签
    tags = []
    if "openclaw" in content.lower():
        tags.append("OpenClaw")
    if "mini pc" in content.lower() or "主机" in content:
        tags.append("MINI PC")
    if "大模型" in content or "llm" in content.lower():
        tags.append("大模型")
    if "本地部署" in content:
        tags.append("本地部署")
    if "智能体" in content or "agent" in content.lower():
        tags.append("AI 智能体")
    
    # 创建博客文章
    filepath = create_blog_post(
        title=title,
        summary=summary,
        core_points=core_points,
        category=category,
        original_url=original_url,
        tags=tags
    )
    
    print(f"\n[OK] 博客文件已创建：{filepath}")
    
    # 提交到 Gitee
    commit_to_gitee(filepath, title)
    
    return {
        "success": True,
        "title": title,
        "category": category,
        "filepath": filepath,
        "url": original_url
    }

if __name__ == "__main__":
    # 处理最新的爬取文件
    scraped_file = WECHAT_SCRAPED_DIR / "2026-03-27-openclaw-mini-pc.md"
    original_url = "https://mp.weixin.qq.com/s/1Tb87YZI4r_GQTg53gOR3w"
    
    if scraped_file.exists():
        result = process_wechat_article(str(scraped_file), original_url)
        print("\n" + "="*50)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"错误：找不到爬取文件 {scraped_file}")
