# 博客部署迁移记录 - GitHub → Gitee

## 📅 时间
2026-03-27 17:06

## 🎯 目标
- 将博客部署从 GitHub Pages 迁移到 Vercel + Gitee
- 解决国内访问速度慢的问题
- 清理所有 GitHub 相关配置

## ✅ 已完成的操作

### 1. 切换 Git 远程仓库
```bash
cd tech-blog
git remote set-url origin git@gitee.com:buyanfangqi/tech-blog.git
```

### 2. 删除 GitHub 配置文件
- ❌ `.github/workflows/deploy.yml` - GitHub Actions 部署配置
- ❌ `GITHUB_FINAL.md` - GitHub Pages 配置文档
- ❌ `SETUP_GITHUB_PAGES.md` - GitHub Pages 设置指南
- ❌ `drafts/github-agent-hq-blog.md` - 草稿文件

### 3. 保留的内容
- ✅ `content/agent/2026-03-22-github-agent-hq-introduction.md` - 关于 GitHub Agent HQ 的技术文章（内容，非配置）
- ✅ `public/tags/github` - 生成的标签页面

### 4. 推送到 Gitee
```bash
git add -A
git commit -m "chore: 移除 GitHub 配置，切换到 Gitee"
git push -u origin main
```

## 🔧 当前配置

### Git 远程仓库
```
origin	git@gitee.com:buyanfangqi/tech-blog.git (fetch)
origin	git@gitee.com:buyanfangqi/tech-blog.git (push)
```

### Vercel 部署
- **项目 ID**: `prj_8VDIQ2I97qYAP3DOSbCYl633YvjT`
- **组织 ID**: `team_T1djMmvy4C7rr35qP2RKETVR`
- **项目名称**: `tech-blog`
- **部署平台**: Vercel
- **代码来源**: Gitee (buyanfangqi/tech-blog)
- **自定义域名**: https://aiinfraagent.com/

### 构建配置
- **Framework**: Hugo
- **Build Command**: `hugo --minify`
- **Output Directory**: `public`
- **Clean URLs**: true

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
调用 git_commit_gitee.py 提交
    ↓
git push 到 Gitee
    ↓
Vercel 自动检测变更
    ↓
Vercel 自动构建和部署（1-2 分钟）
    ↓
✅ https://aiinfraagent.com/ 更新完成
```

## 📊 博客分类

- **ai-infra**: 基础设施、部署、架构、监控、K8s、Docker、微服务
- **agent**: Agent 框架、LangChain、多智能体、智能体
- **llm**: 大模型、Transformer、训练、推理、微调

## ⚠️ 注意事项

1. **Vercel 部署延迟**: 推送到 Gitee 后，Vercel 需要 1-2 分钟完成构建和部署
2. **缓存问题**: 如果访问旧内容，尝试强制刷新（Ctrl+F5）或清除浏览器缓存
3. **Gitee Webhook**: 确保 Vercel 已正确配置 Gitee webhook 以触发自动部署

## 🔍 故障排查

### 如果 Vercel 未自动部署
1. 访问 Vercel 控制台：https://vercel.com/dashboard
2. 检查项目部署日志
3. 手动触发部署：点击 "Redeploy"

### 如果 Gitee 推送失败
1. 检查 SSH 密钥配置：`ssh -T git@gitee.com`
2. 验证远程仓库地址：`git remote -v`
3. 确认 Gitee 仓库存在且有写权限

### 如果网站访问失败
1. 检查域名 DNS 配置
2. 验证 Vercel 部署状态
3. 查看 Vercel 构建日志

## 📚 相关文档

- Vercel 部署指南：`tech-blog/VERCEL_DEPLOYMENT.md`
- 技术博客自动化技能：`skills/tech-blog-auto/SKILL.md`
- 微信公众号爬虫：`skills/wechat-crawler/SKILL.md`

---

**迁移完成！** 🎉

博客现在部署在 Vercel，使用 Gitee 作为代码源，国内访问速度更快。
