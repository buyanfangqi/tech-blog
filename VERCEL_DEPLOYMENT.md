# 🚀 使用 Vercel 部署博客（推荐）

Vercel 在国内访问速度快，支持从 Gitee 部署，而且免费版功能足够强大。

---

## 📋 前置条件

1. ✅ 已购买域名（如果没有，可以在阿里云、腾讯云购买）
2. ✅ 拥有 Gitee 账号

---

## 🎯 部署步骤（5 分钟完成）

### Step 1: 注册 Vercel

访问：https://vercel.com/signup

可以使用 GitHub 或 GitLab 账号登录，或者邮箱注册。

### Step 2: 导入项目

1. 登录后，点击 **Add New...** → **Project**
2. 点击 **Import Git Repository**
3. 如果看到 Gitee，直接选择你的仓库
4. 如果没有 Gitee，先在 Vercel 添加 Gitee 账号

### Step 3: 配置项目

**Framework Preset:** 选择 **Hugo**

**Build Command:** `hugo --minify`

**Output Directory:** `public`

点击 **Deploy** 按钮。

### Step 4: 等待部署

Vercel 会自动：
1. 拉取代码
2. 安装 Hugo
3. 构建网站
4. 部署到全球 CDN

大约 1-2 分钟完成。

---

## 🌐 配置自定义域名

### Step 1: 添加域名

1. 在 Vercel 项目页面，点击 **Settings** → **Domains**
2. 输入你的域名（如 `blog.yourdomain.com`）
3. 点击 **Add**

### Step 2: 配置 DNS

Vercel 会显示 DNS 记录，添加到你的域名 DNS 设置中：

```
类型: CNAME
名称: blog (或你想要的前缀)
值: cname.vercel-dns.com
```

在阿里云/腾讯云的 DNS 设置中添加这条记录。

### Step 3: 验证

等待 DNS 生效（通常 5-10 分钟），访问你的域名即可。

---

## 🔄 自动部署配置

Vercel 支持自动部署，每次推送到 Gitee 会自动触发：

1. 在 Vercel 项目页面，点击 **Settings** → **Git**
2. 确保 **Automatic Deployments** 开启
3. 推送分支选择 `main`

---

## 📝 修改 Git 配置

将远程仓库改回 Gitee：

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 删除 GitHub 远程
git remote remove origin

# 添加 Gitee 远程
git remote add origin git@gitee.com:buyanfangqi/tech-blog.git

# 验证
git remote -v
```

---

## 🚀 完整工作流程

```
飞书发链接
    ↓
OpenClaw 自动生成博客
    ↓
git_commit.py 自动提交
    ↓
git push（推送到 Gitee）
    ↓
Vercel 自动检测
    ↓
Vercel 自动构建和部署
    ↓
✅ 网站在线访问（国内速度极快）
```

---

## 💡 域名推荐

如果你还没买域名，推荐：

- **阿里云**：https://wanwang.aliyun.com
- **腾讯云**：https://dnspod.cloud.tencent.com

推荐后缀：`.com`、`.cn`、`.top`（价格便宜）

---

## 🆘 常见问题

### Q: Vercel 需要付费吗？
A: 免费版完全够用，支持自定义域名、自动部署、全球 CDN。

### Q: 从 Gitee 部署需要配置什么？
A: 在 Vercel 添加 Gitee 账号授权即可。

### Q: 域名需要备案吗？
A: 如果使用 `.cn` 域名需要备案，`.com` 不需要。

### Q: 部署失败怎么办？
A: 检查 Vercel 的部署日志，通常是 Hugo 版本或配置问题。

---

## 🎨 其他选择

如果不想用 Vercel，还可以：

- **Netlify**：https://www.netlify.com（同样支持 Gitee）
- **Cloudflare Pages**：https://pages.dev（全球 CDN 最快）

---

**🎉 完成！你的博客现在部署在 Vercel，国内访问速度极快！**

以后只需推送到 Gitee，Vercel 会自动部署到你的域名。