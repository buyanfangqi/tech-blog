"""
Git 自动提交脚本（Gitee + Vercel 部署版本）
用于将生成的博客自动提交到 Gitee 仓库，Vercel 自动部署
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

# 配置
BLOG_DIR = Path(r"C:\Users\zx\openclaw\.openclaw\workspace\tech-blog")
GITEE_REPO = "buyanfangqi/tech-blog"  # Gitee 仓库

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

def commit_and_push():
    """提交并推送到 Gitee"""

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

    print("博客已成功推送到 Gitee！")
    print("Vercel 将自动检测并部署（约 1-2 分钟）")
    return True

if __name__ == "__main__":
    # 确保目录存在
    BLOG_DIR.mkdir(parents=True, exist_ok=True)

    # 提交并推送
    commit_and_push()