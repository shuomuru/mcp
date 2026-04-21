from openai import OpenAI
import requests
import json

# ===== 初始化 =====
client = OpenAI(
    base_url="https://api.siliconflow.cn/v1",  # DeepSeek可改
    api_key="sk-vluvcxirfckphzhgqkfvrxcviivenkqlqiinawkbpnaqujol"
)

MODEL = "deepseek-ai/DeepSeek-V3.2"
# ===== 工具描述（给模型）=====
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "执行加减乘除计算",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                    "operator": {"type": "string"}
                },
                "required": ["a", "b", "operator"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "列出目录文件",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                }
            }
        }
    }
]

# ===== HTTP工具调用 =====
def call_tool(name, args):
    url = f"http://127.0.0.1:8000/{name}"

    try:
        res = requests.post(url, json=args)
        data = res.json()

        if data.get("status") == "success":
            return data["result"]
        else:
            return f"错误: {data.get('message')}"

    except Exception as e:
        return f"请求失败: {str(e)}"


# ===== Agent =====
def agent(user_input):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": user_input}],
        tools=TOOLS,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    # ===== 调用工具 =====
    if msg.tool_calls:
        tool_call = msg.tool_calls[0]

        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"[调用工具] {tool_name} -> {args}")

        result = call_tool(tool_name, args)

        print("👉 工具返回:", result)

        # ===== 第二次生成（更自然）=====
        second = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": user_input},
                msg,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                }
            ]
        )

        return second.choices[0].message.content

    return msg.content


# ===== CLI =====
if __name__ == "__main__":
    while True:
        user_input = input("用户: ")
        print("AI:", agent(user_input))