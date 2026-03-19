# 🚀 Gitee 版本 - 3 分钟快速开始

## ✅ 已准备就绪

系统已适配 Gitee，现在你可以：
1. 使用 Gitee Pages 免费托管（国内访问速度快）
2. 通过飞书机器人自动生成博客
3. 一键推送到 Gitee

---

## 🎯 部署步骤（仅需 3 步）

### Step 1: 修改配置文件

**编辑** `C:\Users\zx\openclaw\.openclaw\workspace\tech-blog\git_commit_gitee.py`:

```python
# 第 10 行，修改为你的 Gitee 用户名
GITEE_REPO = "你的Gitee用户名/tech-blog"
```

**编辑** `C:\Users\zx\openclaw\.openclaw\workspace\tech-blog\config.toml`:

```toml
# 第 1 行，修改为你的 Gitee 用户名
baseURL = "https://你的Gitee用户名.gitee.io/tech-blog/"
```

### Step 2: 推送到 Gitee

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 初始化 Git 并推送
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@gitee.com:你的用户名/tech-blog.git
git push -u origin main
```

### Step 3: 开启 Gitee Pages

1. 访问 `https://gitee.com/你的用户名/tech-blog`
2. 点击 **服务** → **Gitee Pages**
3. 点击 **启动**
4. **部署分支** 选择 `main`
5. **部署目录** 选择 `/public`
6. 等待 2-3 分钟
7. 访问 `https://你的用户名.gitee.io/tech-blog/`

---

## 📱 如何使用

### 方法 1: 使用 Gitee 版本脚本

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 生成博客
python generate_blog.py

# 推送到 Gitee（使用 Gitee 版本）
python git_commit_gitee.py
```

### 方法 2: 飞书机器人自动生成

在飞书中发送链接：
```
https://pytorch.org/blog/article-name
```

OpenClaw 会自动：
1. 提取链接
2. 获取内容
3. AI 总结
4. 生成博客
5. 推送到 Gitee

---

## 🔄 每次更新后的操作

**重要：** Gitee Pages 需要手动刷新！

1. 访问 `https://gitee.com/你的用户名/tech-blog/pages`
2. 点击 **更新** 按钮
3. 等待 2-3 分钟
4. 访问 `https://你的用户名.gitee.io/tech-blog/`

---

## 💡 技巧

### 批量生成博客

```python
from generate_blog import process_link
from git_commit_gitee import commit_and_push

# 批量生成
blogs = [
    {"url": "https://example1.com", "title": "文章1", ...},
    {"url": "https://example2.com", "title": "文章2", ...},
]

for blog in blogs:
    process_link(**blog)

# 一次性提交
commit_and_push()
```

### 本地预览网站

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog
hugo server -D
# 访问 http://localhost:1313
```

---

## 📋 配置 SSH 密钥（首次使用）

```powershell
# 生成 SSH 密钥
ssh-keygen -t rsa -C "your-email@example.com"

# 复制公钥
cat ~/.ssh/id_rsa.pub

# 添加到 Gitee
# 访问 https://gitee.com/profile/sshkeys
# 粘贴公钥

# 测试连接
ssh -T git@gitee.com
```

---

## 🎉 完成！

访问 `https://你的用户名.gitee.io/tech-blog/` 查看你的博客！

---

## 📚 详细文档

- 📖 **Gitee 部署完整指南**: `GITEE_DEPLOYMENT.md`
- 🚀 **快速开始**: `QUICKSTART_GITEE.md`（本文档）
- 📋 **项目总结**: `PROJECT_SUMMARY.md`

---

**🎉 恭喜！你的技术博客已部署到 Gitee！**

*国内访问速度超快！*