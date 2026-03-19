"""
Git 自动提交脚本（Gitee 版本）
用于将生成的博客自动提交到 Gitee 仓库
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

# 配置
BLOG_DIR = Path(r"C:\Users\zx\openclaw\.openclaw\workspace\tech-blog")
GITEE_REPO = "buyanfangqi/tech-blog"  # 请修改为你的 Gitee 用户名和仓库名
GITEE_TOKEN = ""  # 可选：Gitee Personal Access Token（用于 HTTPS 推送）

def run_command(command: list, cwd: Path = None) -> tuple:
    """运行 shell 命令"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def init_git_repo():
    """初始化 Git 仓库（如果还没有）"""
    git_dir = BLOG_DIR / ".git"

    if not git_dir.exists():
        print("初始化 Git 仓库...")
        success, output = run_command(["git", "init"], cwd=BLOG_DIR)

        if not success:
            print(f"Git 初始化失败: {output}")
            return False

        # 创建 .gitignore
        gitignore = BLOG_DIR / ".gitignore"
        if not gitignore.exists():
            with open(gitignore, 'w', encoding='utf-8') as f:
                f.write("""# Hugo
/public/
/resources/_gen/
.hugo_build.lock

# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/
""")

        # 初始提交
        run_command(["git", "add", "."], cwd=BLOG_DIR)
        run_command(["git", "commit", "-m", "Initial commit"], cwd=BLOG_DIR)

        print("Git 仓库初始化完成")
        return True
    else:
        print("Git 仓库已存在")
        return True

def commit_and_push():
    """提交并推送更改"""

    # 检查是否有更改
    success, output = run_command(["git", "status", "--porcelain"], cwd=BLOG_DIR)

    if not success:
        print(f"检查 Git 状态失败: {output}")
        return False

    if not output.strip():
        print("没有新的更改，无需提交")
        return True

    # 添加所有更改
    print("添加更改到 Git...")
    success, output = run_command(["git", "add", "."], cwd=BLOG_DIR)

    if not success:
        print(f"Git add 失败: {output}")
        return False

    # 提交更改
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto-commit: Update blog post at {current_time}"

    print(f"提交更改: {commit_message}")
    success, output = run_command(
        ["git", "commit", "-m", commit_message],
        cwd=BLOG_DIR
    )

    if not success:
        print(f"Git commit 失败: {output}")
        return False

    # 推送到 Gitee
    print("推送到 Gitee...")
    success, output = run_command(["git", "push"], cwd=BLOG_DIR)

    if not success:
        print(f"Git push 失败: {output}")
        print("请确保已配置 Gitee 远程仓库并设置好认证")
        return False

    print("✅ 博客已成功推送到 Gitee")
    return True

def setup_gitee_remote():
    """设置 Gitee 远程仓库"""
    success, output = run_command(["git", "remote", "-v"], cwd=BLOG_DIR)

    if success and "origin" in output:
        print(f"远程仓库已配置: {output}")
        return True

    # 添加远程仓库（使用 SSH）
    remote_url = f"git@gitee.com:{GITEE_REPO}.git"
    print(f"添加远程仓库: {remote_url}")

    success, output = run_command(
        ["git", "remote", "add", "origin", remote_url],
        cwd=BLOG_DIR
    )

    if success:
        print("✅ 远程仓库配置完成")
        return True
    else:
        print(f"❌ 远程仓库配置失败: {output}")
        return False

if __name__ == "__main__":
    # 确保目录存在
    BLOG_DIR.mkdir(parents=True, exist_ok=True)

    # 初始化 Git 仓库
    if not init_git_repo():
        print("❌ Git 仓库初始化失败")
        exit(1)

    # 设置远程仓库（需要修改配置）
    if "your-gitee-username" in GITEE_REPO:
        print("\n⚠️  请先修改配置文件中的 GITEE_REPO 变量")
        print("   GITEE_REPO = \"your-gitee-username/tech-blog\"")
        print("   改为: GITEE_REPO = \"你的Gitee用户名/tech-blog\"")
        exit(1)

    setup_gitee_remote()

    # 提交并推送
    commit_and_push()