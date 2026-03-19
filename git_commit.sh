#!/bin/bash
# Git 自动提交脚本
# 用于将生成的博客自动提交到 GitHub 仓库

# 配置
BLOG_DIR="C:/Users/zx/openclaw/.openclaw/workspace/tech-blog"
GITHUB_REPO="your-username/tech-blog"  # 请修改为你的 GitHub 用户名和仓库名
GITHUB_TOKEN=""  # 请设置环境变量或在文件中配置

# 进入博客目录
cd "$BLOG_DIR" || exit 1

# 检查是否有新的提交
if git diff-index --quiet HEAD --; then
    echo "没有新的更改，无需提交"
    exit 0
fi

# 获取当前时间
CURRENT_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# 添加所有更改
git add .

# 提交更改
git commit -m "Auto-commit: Update blog post at $CURRENT_TIME"

# 推送到 GitHub
if [ -n "$GITHUB_TOKEN" ]; then
    # 使用 token 推送
    git push https://x-access-token:$GITHUB_TOKEN@github.com/$GITHUB_REPO.git main
else
    # 使用 SSH 推送
    git push origin main
fi

echo "博客已成功推送到 GitHub"