# 🚀 GitHub Pages 部署步骤

## ✅ 已完成

- [x] 代码已推送到 GitHub：https://github.com/buyanfangqi/tech-blog
- [x] GitHub Actions workflow 已配置
- [x] Git 远程仓库已切换到 GitHub

---

## 🔧 手动配置步骤（只需做一次）

### Step 1: 访问 GitHub Pages 设置

打开浏览器，访问：
```
https://github.com/buyanfangqi/tech-blog/settings/pages
```

### Step 2: 配置部署方式

1. 找到 **Build and deployment** 部分
2. 在 **Source** 下拉菜单中，选择 **GitHub Actions**
3. 点击 **Save** 保存

### Step 3: 触发首次部署

配置完成后，GitHub Actions 会自动触发部署流程。

或者手动触发：
1. 访问 Actions 页面：https://github.com/buyanfangqi/tech-blog/actions
2. 点击左侧 **Deploy to GitHub Pages** workflow
3. 点击 **Run workflow** → **Run workflow**

### Step 4: 等待部署完成

部署通常需要 2-5 分钟。

查看部署状态：
```
https://github.com/buyanfangqi/tech-blog/actions
```

### Step 5: 访问网站

部署成功后访问：
```
https://buyanfangqi.github.io/tech-blog/
```

---

## 🔄 后续自动部署

完成上述配置后，每次推送代码到 GitHub main 分支，GitHub Pages 会自动更新。

### 自动部署流程

```powershell
# 1. 生成博客
python generate_blog.py

# 2. 提交代码
python git_commit.py
```

`git_commit.py` 会自动：
1. 添加所有修改的文件
2. 提交更改
3. 推送到 GitHub
4. GitHub Actions 自动触发部署

---

## 📱 飞书自动生成

在飞书中发送任何技术文章链接，OpenClaw 会：
1. 提取链接内容
2. AI 分析总结
3. 生成 Markdown 博客
4. 自动提交到 GitHub
5. 自动触发部署

无需任何手动操作！

---

## 📊 部署工作流说明

GitHub Actions 会执行以下步骤：

```yaml
1. Checkout 代码
2. 安装 Hugo（最新版本）
3. 构建 Hugo 网站（hugo --minify）
4. 上传构建产物到 GitHub Pages
```

---

## 🆘 常见问题

### Q: 部署失败怎么办？

检查 GitHub Actions 日志：
```
https://github.com/buyanfangqi/tech-blog/actions
```

常见错误：
- Hugo 版本问题 → workflow 会自动使用最新版
- 构建错误 → 检查 config.toml 和 content 目录

### Q: 网站无法访问？

等待 2-5 分钟让部署完成。
检查：https://github.com/buyanfangqi/tech-blog/actions

### Q: 如何自定义域名？

在 GitHub Pages 设置中：
1. Custom domain → 输入你的域名（如：blog.example.com）
2. 按照提示配置 DNS

---

## 🎉 完成！

访问你的博客：
```
https://buyanfangqi.github.io/tech-blog/
```

现在在飞书中发送链接，博客会自动生成并部署！