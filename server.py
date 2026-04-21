from fastapi import FastAPI
import os

app = FastAPI()

# ===== 工具1：计算器 =====
@app.post("/calculator")
def calculator(data: dict):
    a = data.get("a")
    b = data.get("b")
    op = data.get("operator")

    try:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b if b != 0 else 0
        else:
            return {"status": "error", "message": "无效运算符"}

        return {"status": "success", "result": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}


# ===== 工具2：列文件 =====
@app.post("/list_files")
def list_files(data: dict):
    path = data.get("path", ".")

    try:
        files = os.listdir(path)
        return {"status": "success", "result": files}
    except Exception as e:
        return {"status": "error", "message": str(e)}