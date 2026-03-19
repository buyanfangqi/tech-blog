# Tech Blog - AI Infra & Agent & LLM

自动化技术博客系统，通过OpenClaw飞书机器人自动生成和发布技术总结。

## 目录结构

```
tech-blog/
├── content/           # 博客内容目录
│   ├── ai-infra/     # AI Infra 技术
│   ├── agent/        # Agent 技术
│   └── llm/          # 大模型算法技术
├── static/           # 静态资源
├── themes/           # Hugo 主题
├── archetypes/       # 博客模板
├── data/            # 数据文件
└── config.toml      # Hugo 配置
```

## 工作流程

1. 飞书发送技术链接
2. OpenClaw自动获取内容并总结
3. AI分类并生成Markdown博客
4. 自动提交到GitHub仓库
5. GitHub Actions自动部署网站