# Hugo 本地开发快速指南

## 解决 404 问题

如果访问 http://localhost:1313 出现 404，请按以下步骤操作：

### 方法 1: 使用正确的命令启动

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog

# 先清理旧的构建
hugo --cleanDestinationDir

# 启动开发服务器
hugo server --bind 127.0.0.1 --port 1313 --disableFastRender

# 或者在后台运行
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog; hugo server"
```

### 方法 2: 检查配置文件

确保 `config.toml` 中的 `baseURL` 设置为 `/`（本地开发）：

```toml
baseURL = "/"
```

### 方法 3: 直接访问构建后的文件

如果 Hugo server 有问题，可以直接访问构建后的 HTML 文件：

```powershell
# 构建网站
hugo

# 用浏览器打开
start public/index.html
```

### 方法 4: 使用 Python HTTP 服务器

```powershell
cd C:\Users\zx\openclaw\.openclaw\workspace\tech-blog/public
python -m http.server 1313
```

---

## 常见问题

### Q: Hugo server 启动失败？
**A:**
1. 检查端口是否被占用：`netstat -ano | findstr 1313`
2. 杀掉占用进程：`taskkill /F /PID <进程ID>`
3. 重新启动

### Q: 访问还是 404？
**A:**
1. 检查浏览器是否缓存了旧页面（Ctrl+F5 强制刷新）
2. 清理浏览器缓存
3. 尝试使用其他浏览器

### Q: 想看到最新的修改？
**A:**
Hugo server 会自动监听文件变化并重新构建，但有时候需要：
1. 刷新浏览器（Ctrl+F5）
2. 停止并重启 Hugo server

---

## 推荐的工作流程

### 本地开发

```powershell
# 1. 启动服务器
hugo server --disableFastRender

# 2. 在另一个终端修改文件

# 3. 浏览器自动刷新（或手动 Ctrl+F5）
```

### 查看最终效果

```powershell
# 1. 构建
hugo

# 2. 用浏览器打开
start public/index.html
```

---

## 提示

- Hugo server 默认运行在 http://localhost:1313
- 修改文件后会自动重新构建
- 浏览器可能需要强制刷新（Ctrl+F5）
- 如果 server 有问题，直接用 `start public/index.html` 查看