---
title: "OpenClaw 接入飞书完整教程"
date: 2026-03-22T21:05:00+08:00
draft: false
categories: ["Agent"]
tags: ["OpenClaw","飞书","自动化","AI代理"]
original_url: "https://www.runoob.com/ai-agent/openclaw-feishu.html"
---

## 核心要点

OpenClaw（原 Clawdbot）是一个开源、本地优先的 AI 代理网关，能让大模型在你的电脑/服务器上 7×24 小时运行。本教程详细介绍如何将 OpenClaw 接入飞书，实现消息推送、发图、收文件、审批交互、数据同步等自动化场景。

## 技术亮点

### 1. OpenClaw 核心特性

- **本地优先**：大模型在本地服务器运行，数据安全可控
- **多平台支持**：无缝接入飞书、Telegram、Discord 等聊天平台
- **强大能力**：支持直接操作电脑、浏览网页、执行命令
- **7×24 运行**：全天候自动化工作，无需人工干预

### 2. 飞书集成步骤

**安装与配置**
```bash
# 安装 OpenClaw
npm install -g openclaw@latest --registry=https://registry.npmmirror.com

# 启用飞书插件
openclaw plugins enable feishu

# 查看插件状态
openclaw plugins list
```

**创建飞书机器人**
1. 访问飞书开放平台创建企业自建应用
2. 复制 App ID 和 App Secret 凭证
3. 使用 `openclaw channels add` 配置 channel
4. 选择国内域名，设置 Open 群聊策略

**配置机器人能力**
- 启用机器人能力
- 配置权限（消息发送、文件读写、群聊访问等）
- 订阅事件（接收消息、消息已读、机器人进出群等）
- 发布应用

### 3. 关键配置要点

**事件订阅**
- `im.message.receive_v1` - 接收消息
- `im.message.message_read_v1` - 消息已读回执
- `im.chat.member.bot.added_v1` - 机器人进群
- `im.chat.member.bot.deleted_v1` - 机器人被移出群

**权限配置**
- 消息发送与接收权限
- 文件读写权限
- 群聊成员访问权限
- 机器人菜单配置权限

### 4. 测试验证

创建飞书测试群，添加机器人后，可以 @ 机器人让自我介绍，正常回复说明流程跑通。

## 总结

OpenClaw 的飞书集成功能强大，可以快速实现各种自动化场景。通过简单的配置，就能让 AI 代理在飞书中工作，大大提升工作效率。建议在实际项目中测试各种场景，充分利用其自动化能力。

---

*本文由 OpenClaw 飞书机器人自动生成*