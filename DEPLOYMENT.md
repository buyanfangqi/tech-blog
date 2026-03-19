# 技术博客自动化系统 - 完整部署指南

## 🎯 系统概述

这是一个自动化技术博客系统，通过 OpenClaw 飞书机器人实现：
1. 飞书发送技术链接 → 自动抓取内容
2. AI 智能总结 → 生成 Markdown 博客
3. 自动分类 → AI Infra / Agent / LLM
4. 自动提交 → GitHub 仓库
5. 自动部署 → GitHub Pages

---

## 📦 环境要求

### 1. 安装 Hugo（静态网站生成器）

**Windows:**
```powershell
# 使用 Chocolatey
choco install hugo-extended

# 或者从官网下载：https://gohugo.io/installation/windows/
```

**验证安装:**
```powershell
hugo version
```

### 2. 安装 Python 3.8+

如果还没有安装，从 https://python.org/downloads/ 下载安装

**验证安装:**
```powershell
python --version
```

### 3. 安装 Git

如果还没有安装，从 https://git-scm.com/download/win 下载安装

**验证安装:**
```powershell
git --version
```

---

## 🚀 部署步骤

### Step 1: 创建 GitHub 仓库

1. 登录 GitHub
2. 创建新仓库，命名为 `tech-blog`
3. 设置为 Public（公开）
4. 记下你的 GitHub 用户名

### Step 2: 配置 GitHub Pages

1. 进入仓库的 **Settings** → **Pages**
2. **Source** 选择 **GitHub Actions**
3. 保存

### Step 3: 修改配置文件

编辑 `C:\Users\zx\openclaw\.openclaw\workspace\tech-blog\config.toml`：

```toml
baseURL = "https://你的GitHub用户名.github.io/tech-blog/"
```

编辑 `C:\Users\zx\openclaw\.openclaw\workspace\tech-blog\git_commit.py`：

```python
GITHUB_REPO = "你的GitHub用户名/tech-blog"
```

### Step 4: 初始化 Git 仓库并推送

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 初始化 Git
python git_commit.py

# 或者手动执行
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:你的GitHub用户名/tech-blog.git
git push -u origin main
```

### Step 5: 本地测试网站

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 生成网站
hugo

# 启动本地服务器
hugo server -D

# 浏览器访问 http://localhost:1313
```

---

## 📱 飞书机器人配置

### 方式 1：通过飞书直接发送链接

在飞书中发送消息，OpenClaw 会自动处理：

```
https://example.com/tech-article
```

### 方式 2：自定义 OpenClaw 技能

创建一个技能文件，自动处理链接：

**文件路径**: `C:\Users\zx\openclaw\.openclaw\workspace\skills\tech-blog\SKILL.md`

```markdown
# 技术博客自动生成技能

## 触发条件
当用户在飞书中发送包含 HTTP 链接的消息时触发

## 处理流程
1. 提取消息中的 URL
2. 使用 web_fetch 获取网页内容
3. 使用 LLM 分析并总结：
   - 提取文章标题
   - 生成 3-5 个核心要点
   - 识别技术标签
4. 调用 `tech-blog/generate_blog.py` 生成博客
5. 调用 `tech-blog/git_commit.py` 提交到 GitHub

## Python 脚本调用
```python
import sys
sys.path.insert(0, r'C:\Users\zx\openclaw\.openclaw\workspace\tech-blog')

from generate_blog import process_link

result = process_link(
    url="提取的URL",
    title="文章标题",
    summary="文章摘要",
    core_points=["要点1", "要点2", "要点3"],
    tags=["标签1", "标签2"]
)

# 提交到 GitHub
from git_commit import commit_and_push
commit_and_push()
```
```

---

## 📝 使用示例

### 示例 1：手动生成博客

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 测试生成博客
python generate_blog.py
```

### 示例 2：通过 Python API 调用

```python
from tech_blog.generate_blog import process_link
from tech_blog.git_commit import commit_and_push

# 生成博客
result = process_link(
    url="https://pytorch.org/blog/introducing-torchcompile/",
    title="PyTorch 2.0 编译器介绍",
    summary="TorchCompile 是 PyTorch 2.0 的核心功能，通过编译优化提升推理速度",
    core_points=[
        "TorchCompile 基于 TorchDynamo 后端",
        "支持多种后端编译器（AOTAutograd、PrimTorch、Inductor）",
        "在推理场景下平均提升 2-3 倍速度",
        "对训练场景也有显著优化"
    ],
    tags=["PyTorch", "Compiler", "Performance"]
)

print(f"博客已生成: {result['filepath']}")

# 提交到 GitHub
commit_and_push()
```

---

## 🔧 故障排查

### 问题 1: Hugo 网站无法访问

**检查点:**
- GitHub Pages 设置是否为 "GitHub Actions"
- `.github/workflows/deploy.yml` 文件是否存在
- 仓库是否为 Public

### 问题 2: Git 推送失败

**检查点:**
- SSH 密钥是否配置：`ssh -T git@github.com`
- 远程仓库地址是否正确：`git remote -v`
- 是否有写权限

### 问题 3: 博客分类不准确

**解决方案:**
编辑 `generate_blog.py` 中的 `CATEGORY_KEYWORDS`，添加更多关键词

---

## 📊 监控和统计

### 查看 GitHub Actions 部署状态

访问: `https://github.com/你的用户名/tech-blog/actions`

### 查看网站访问统计

1. 进入仓库 Settings → Pages
2. 查看访问数据（需要启用 GitHub Analytics）

---

## 🎨 自定义主题

### 修改网站样式

编辑 `themes/tech-theme/layouts/_default/baseof.html` 中的 CSS 样式

### 添加新分类

1. 在 `content/` 下创建新目录
2. 在 `config.toml` 中添加菜单项
3. 在 `generate_blog.py` 中添加分类关键词

---

## 🔄 完整工作流程图

```
飞书消息
    ↓
[提取 URL]
    ↓
[获取网页内容]
    ↓
[AI 分析总结]
    ↓
[生成 Markdown]
    ↓
[保存到 content/分类/]
    ↓
[Git 提交]
    ↓
[推送 GitHub]
    ↓
[GitHub Actions 构建]
    ↓
[部署到 Pages]
    ↓
✅ 网站在线访问
```

---

## 📚 参考资源

- Hugo 官方文档: https://gohugo.io/documentation/
- GitHub Pages 指南: https://docs.github.com/en/pages
- OpenClaw 文档: https://docs.openclaw.ai

---

## 💡 提示

1. **第一次部署可能需要几分钟** - GitHub Actions 需要时间构建
2. **建议使用 SSH 密钥** - 比 HTTPS token 更安全
3. **定期备份** - Git 版本控制本身就是最好的备份
4. **测试本地预览** - 使用 `hugo server -D` 在本地预览

---

**Happy Blogging! 🚀**