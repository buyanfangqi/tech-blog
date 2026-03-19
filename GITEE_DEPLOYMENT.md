# 🎯 Gitee 部署指南

## 📋 Gitee vs GitHub 对比

| 特性 | GitHub Pages | Gitee Pages |
|------|-------------|-------------|
| **访问速度** | 国内较慢 | ⭐ 国内速度快 |
| **自动部署** | ✅ GitHub Actions | ❌ 需手动触发 |
| **自定义域名** | ✅ 支持 | ⭐ Gitee Pages Pro |
| **免费版** | ✅ 完全免费 | ✅ 完全免费 |
| **HTTPS** | ✅ 自动支持 | ⭐ Pro 才支持 |

---

## 🚀 Gitee Pages 部署方案

### 方案 1: Gitee Pages（免费版）- 推荐

**特点：**
- 完全免费
- 国内访问速度快
- 需要手动更新（每次推送后点击"更新"）

**部署步骤：**

#### Step 1: 创建 Gitee 仓库

1. 访问 https://gitee.com/
2. 登录或注册账号
3. 创建新仓库，命名为 `tech-blog`
4. 设置为 **公开**（Public）
5. 记下你的 Gitee 用户名

#### Step 2: 推送代码到 Gitee

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 修改配置文件
# 编辑 git_commit_gitee.py，第 10 行：
# GITEE_REPO = "你的Gitee用户名/tech-blog"

# 修改 config.toml，第 1 行：
# baseURL = "https://你的Gitee用户名.gitee.io/tech-blog/"

# 初始化 Git 并推送
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@gitee.com:你的用户名/tech-blog.git
git push -u origin main
```

#### Step 3: 开启 Gitee Pages

1. 访问你的 Gitee 仓库
2. 点击 **服务** → **Gitee Pages**
3. 点击 **启动**
4. **部署分支** 选择 `main`
5. **部署目录** 选择 `/public`
6. 点击 **启动**

等待几分钟后，访问 `https://你的用户名.gitee.io/tech-blog/`

#### Step 4: 每次更新后手动刷新

每次推送新博客后：
1. 访问 Gitee Pages 页面
2. 点击 **更新** 按钮
3. 等待几分钟，网站就会更新

---

### 方案 2: 本地构建 + 手动上传

如果你不想使用 Gitee Pages，可以在本地构建，然后手动上传到任何服务器。

#### 本地构建网站

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 安装 Hugo（如果还没有）
choco install hugo-extended

# 生成静态网站
hugo

# 生成的网站在 public/ 目录下
```

#### 上传到服务器

你可以将 `public/` 目录上传到：
- Nginx 服务器
- 阿里云 OSS
- 腾讯云 COS
- 任何静态网站托管服务

---

### 方案 3: 自动化脚本（高级）

创建一个自动化脚本，每次生成博客后自动构建和上传。

**文件**: `auto_deploy_gitee.py`

```python
"""
自动化部署脚本：生成博客 → 构建 → 推送 → 更新 Gitee Pages
"""

import subprocess
from pathlib import Path
from generate_blog import process_link
from git_commit_gitee import commit_and_push

def deploy_to_gitee():
    """完整的部署流程"""

    print("=" * 50)
    print("🚀 开始部署到 Gitee")
    print("=" * 50)

    # 1. 提交代码到 Gitee
    print("\n📤 步骤 1: 推送到 Gitee...")
    if not commit_and_push():
        print("❌ 推送失败")
        return False

    # 2. 本地构建 Hugo 网站
    print("\n🔨 步骤 2: 构建 Hugo 网站...")
    result = subprocess.run(
        ["hugo"],
        cwd=Path(r"C:\Users\zx\openclaw\.openclaw\workspace\tech-blog"),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ Hugo 构建失败: {result.stderr}")
        return False

    print("✅ Hugo 构建成功")

    # 3. 提示手动更新 Gitee Pages
    print("\n📋 步骤 3: 更新 Gitee Pages")
    print("请访问以下页面并点击「更新」按钮：")
    print("https://gitee.com/你的用户名/tech-blog/pages")
    print("\n等待 2-3 分钟后访问：")
    print("https://你的用户名.gitee.io/tech-blog/")

    print("\n" + "=" * 50)
    print("✅ 部署流程完成！")
    print("=" * 50)

    return True

if __name__ == "__main__":
    deploy_to_gitee()
```

---

## 📱 配置飞书机器人（Gitee 版本）

修改 OpenClaw 技能文件，使用 `git_commit_gitee.py` 而不是 `git_commit.py`：

```python
# 使用 Gitee 版本的提交脚本
from git_commit_gitee import commit_and_push

# 提交到 Gitee
commit_and_push()
```

---

## 🔧 常用命令

### 推送到 Gitee
```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog
python git_commit_gitee.py
```

### 本地预览网站
```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog
hugo server -D
# 访问 http://localhost:1313
```

### 构建静态网站
```powershell
hugo
# 生成的网站在 public/ 目录
```

---

## 💡 优化建议

### 1. 批量更新

如果有多篇博客，可以批量生成后一次性推送：

```python
from generate_blog import process_link
from git_commit_gitee import commit_and_push

# 批量生成博客
blogs = [
    {"url": "https://example1.com", "title": "文章1", ...},
    {"url": "https://example2.com", "title": "文章2", ...},
    {"url": "https://example3.com", "title": "文章3", ...},
]

for blog in blogs:
    process_link(**blog)

# 一次性提交
commit_and_push()
```

### 2. 使用 Gitee Pages Pro

如果你有预算，可以升级到 Gitee Pages Pro：
- 自动部署（无需手动点击更新）
- 支持自定义域名
- 支持 HTTPS
- 更好的性能

价格：约 10 元/月

### 3. 使用 CI/CD 工具

可以使用第三方 CI/CD 工具实现自动部署：
- GitHub Actions（触发 Gitee 更新）
- 自建 Jenkins
- Coding CI

---

## 🆘 常见问题

### Q: Gitee Pages 无法访问？
**A:**
1. 检查仓库是否为公开
2. 检查 Pages 服务是否已启动
3. 等待 5-10 分钟让 Gitee 生效

### Q: 网站更新后没变化？
**A:**
1. 访问 Gitee Pages 页面
2. 点击 **更新** 按钮
3. 清除浏览器缓存

### Q: Git 推送失败？
**A:**
1. 检查 SSH 密钥配置：`ssh -T git@gitee.com`
2. 检查远程仓库地址：`git remote -v`
3. 确保网络可以访问 Gitee

### Q: 如何配置 Gitee SSH 密钥？
**A:**
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

## 📊 部署流程图

```
飞书发链接
    ↓
OpenClaw 处理
    ↓
生成 Markdown 博客
    ↓
git_commit_gitee.py
    ↓
Git Push 到 Gitee
    ↓
手动点击 "更新"
    ↓
✅ Gitee Pages 上线
```

---

## 🎉 总结

**Gitee Pages 优点：**
- ✅ 国内访问速度快
- ✅ 完全免费
- ✅ 简单易用

**Gitee Pages 缺点：**
- ❌ 需要手动更新（每次推送后点击"更新"）
- ❌ 免费版不支持自定义域名
- ❌ 没有 GitHub Actions 那样的自动化

**推荐：**
如果你主要面向国内读者，**Gitee Pages 是最佳选择**！虽然需要手动点击更新，但访问速度优势明显。

---

*Created by OpenClaw • 2026-03-19*