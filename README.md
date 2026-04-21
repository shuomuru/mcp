# 🚀 MCP HTTP Agent 项目

基于 **大模型 API + HTTP 工具服务（FastAPI）** 构建的智能 Agent 系统，实现自动工具调用（Function Calling）、服务解耦与多工具协同。

---

# 📌 项目简介

本项目实现了一个完整的 Agent 架构：

* 🤖 使用大模型（DeepSeek / OpenAI）作为决策大脑
* 🔧 使用 FastAPI 提供工具服务（计算器 / 文件系统）
* 🔗 使用 HTTP 进行客户端与服务端通信
* 🧠 支持 Function Calling 自动调用工具
* 🔁 支持二次推理生成自然语言结果

---

# 🏗️ 项目架构

```
用户输入
   ↓
Agent（LLM）
   ↓
Function Calling（是否调用工具）
   ↓
HTTP 请求
   ↓
FastAPI 工具服务
   ↓
返回结果
   ↓
LLM 二次生成
   ↓
最终回答
```

---

# 📁 项目结构

```
mcp-http-agent/
├── server.py        # FastAPI 工具服务
├── agent.py         # Agent 主程序
├── requirements.txt # 依赖
└── README.md
```

---

# ⚙️ 环境安装

```bash
pip install fastapi uvicorn requests openai
```

---

# 🔑 配置说明

在 `agent.py` 中配置你的 API Key：

```python
client = OpenAI(
    api_key="你的API_KEY",
    base_url="https://api.deepseek.com"  # 或 https://api.openai.com/v1
)

MODEL = "deepseek-chat"  # 或 gpt-4.1
```

---

# ▶️ 运行项目

## 1️⃣ 启动工具服务

```bash
uvicorn server:app --reload
```

访问地址：

```
http://127.0.0.1:8000
```

---

## 2️⃣ 启动 Agent

```bash
python agent.py
```

---

# 🧪 示例测试

输入：

```
帮我算 25 * 4
```

输出：

```
[调用工具] calculator -> {'a': 25, 'b': 4, 'operator': '*'}
👉 工具返回: 100
AI: 25乘以4的结果是100
```

---

# 🛠️ 已实现功能

* ✅ 基于 Function Calling 的自动工具调用
* ✅ HTTP 工具服务（FastAPI）
* ✅ 工具解耦（服务端独立）
* ✅ 多工具支持（计算器 / 文件操作）
* ✅ 二次推理生成（结果自然语言化）

---

# 🚀 可扩展方向

## 🔥 1. RAG（检索增强生成）

```python
@app.post("/retrieve")
def retrieve(data: dict):
    return {"result": "知识库内容"}
```

---

## 🔥 2. 多工具链调用（ReAct / AutoGPT）

支持模型连续调用多个工具：

```
查文件 → 分析 → 计算 → 总结
```

---

## 🔥 3. Web UI

* Gradio
* FastAPI + 前端页面

---

## 🔥 4. 多轮对话（记忆）

在 Agent 中加入历史消息：

```python
messages.append({"role": "user", "content": user_input})
```

---

# 💡 项目亮点

* 🔹 使用 HTTP 替代 stdio，提升稳定性
* 🔹 实现 Agent + Tool Calling 完整闭环
* 🔹 服务端与客户端完全解耦
* 🔹 贴近企业真实 Agent 架构

---


---

# 📌 技术栈

* Python
* FastAPI
* OpenAI API / DeepSeek API
* Requests
* Function Calling

---

# 📎 后续优化

* ⏩ 接入向量数据库（FAISS）实现 RAG
* ⏩ 增加任务规划能力（多步推理）
* ⏩ 引入流式输出（Streaming）
* ⏩ 构建前端交互界面

---

# ⭐ 总结

本项目实现了一个完整的 Agent 系统，从：

* 工具服务
* 到模型决策
* 到自动调用
* 再到结果生成

形成完整闭环，具备良好的扩展性与工程价值。

---
