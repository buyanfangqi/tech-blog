# 博客部署迁移记录 - Gitee → GitHub

## 📅 时间
2026-03-27 21:22

## 🎯 目标
- 将博客部署从 Vercel + Gitee 切换回 GitHub Pages
- 恢复 GitHub Actions 自动部署配置

## ✅ 已完成的操作

### 1. 切换 Git 远程仓库
```bash
cd tech-blog
git remote remove origin
git remote add origin git@github.com:buyanfangqi/tech-blog.git
```

### 2. 恢复 GitHub Actions 配置
创建 `.github/workflows/deploy.yml`：
- 使用 `peaceiris/actions-hugo@v3` 构建 Hugo 站点
- 使用 `actions/configure-pages@v5` 配置 Pages
- 使用 `actions/deploy-pages@v4` 部署到 GitHub Pages
- 触发条件：push 到 main 分支

### 3. 推送到 GitHub
```bash
git add -A
git commit -m "chore: 切换回 GitHub，恢复 GitHub Actions 配置"
git push -u origin main
```

### 4. 更新技能配置
- `skills/tech-blog-auto/SKILL.md`：更新为使用 `git_commit.py`（GitHub 版本）
- `TOOLS.md`：更新博客配置为 GitHub Pages

## 🔧 当前配置

### Git 远程仓库
```
origin	git@github.com:buyanfangqi/tech-blog.git (fetch/push)
```

### GitHub Pages 部署
- **仓库**: buyanfangqi/tech-blog
- **分支**: main
- **部署方式**: GitHub Actions
- **工作流**: `.github/workflows/deploy.yml`
- **自定义域名**: https://aiinfraagent.com/

### 构建配置
- **Framework**: Hugo
- **Build Command**: `hugo --minify`
- **Output Directory**: `public`
- **Hugo Version**: latest (extended)

## 📝 自动化工作流

```
飞书发送链接（带"总结并发布"关键字）
    ↓
OpenClaw 识别并处理
    ↓
普通文章 → web_fetch 获取内容
微信文章 → wechat-crawler 爬取（jina 方法）
    ↓
AI 总结 + 自动分类
    ↓
生成博客文件（content/{category}/）
    ↓
调用 git_commit.py 提交
    ↓
git push 到 GitHub
    ↓
GitHub Actions 自动触发
    ↓
Hugo 构建 + 部署到 GitHub Pages
    ↓
✅ https://aiinfraagent.com/ 更新完成（约 2-3 分钟）
```

## 📊 博客分类

- **ai-infra**: 基础设施、部署、架构、监控、K8s、Docker、微服务
- **agent**: Agent 框架、LangChain、多智能体、智能体
- **llm**: 大模型、Transformer、训练、推理、微调

## ⚠️ 注意事项

1. **GitHub Pages 部署延迟**: 推送到 GitHub 后，GitHub Actions 需要 2-3 分钟完成构建和部署
2. **DNS 配置**: 确保域名 `aiinfraagent.com` 已正确配置 CNAME 到 `buyanfangqi.github.io`
3. **GitHub Pages 设置**: 在仓库 Settings → Pages 中确认自定义域名配置正确

## 🔍 故障排查

### 如果 GitHub Pages 未自动部署
1. 访问仓库 Actions 标签：https://github.com/buyanfangqi/tech-blog/actions
2. 检查最新的工作流运行状态
3. 如果失败，查看日志并重新运行

### 如果域名无法访问
1. 检查 DNS 配置：`nslookup aiinfraagent.com`
2. 验证 GitHub Pages 设置中的自定义域名
3. 等待 DNS 生效（可能需要几分钟到几小时）

### 如果推送失败
1. 检查 SSH 密钥配置：`ssh -T git@github.com`
2. 验证远程仓库地址：`git remote -v`
3. 确认 GitHub 仓库存在且有写权限

## 📚 相关文档

- GitHub Actions 配置：`tech-blog/.github/workflows/deploy.yml`
- 技术博客自动化技能：`skills/tech-blog-auto/SKILL.md`
- 微信公众号爬虫：`skills/wechat-crawler/SKILL.md`

---

**迁移完成！** 🎉

博客现在使用 GitHub Pages 部署，推送到 GitHub 后自动构建和发布。

## 📋 迁移历史

| 日期 | 操作 | 部署平台 |
|------|------|----------|
| 2026-03-27 15:42 | 初始配置 | Gitee + Vercel |
| 2026-03-27 17:06 | 切换到 Gitee | Gitee + Vercel |
| 2026-03-27 21:22 | 切换回 GitHub | GitHub Pages |
