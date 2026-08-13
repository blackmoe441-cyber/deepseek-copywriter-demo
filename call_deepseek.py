import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件里的配置
load_dotenv()

# 从环境变量读取 API key
api_key = os.getenv("DEEPSEEK_API_KEY")

# 创建 DeepSeek 客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

# 让用户选择模板
print("请选择要使用的模板：")
print("1. 电商种草文案")
print("2. 教培招生顾问")
choice = input("输入数字 1 或 2：")

if choice == "1":
    template_file = "prompt-template-ecom-copywriter-v1.md"
    user_input = input("请输入商品描述：")
elif choice == "2":
    template_file = "prompt-template-edu-consultant-v1.md"
    user_input = input("请输入家长咨询的问题：")
else:
    print("无效选择，默认使用电商模板。")
    template_file = "prompt-template-ecom-copywriter-v1.md"
    user_input = input("请输入商品描述：")

# 读取选中的 prompt 模板
with open(template_file, "r", encoding="utf-8") as f:
    system_prompt = f.read()

# 调用 API
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
)

# 打印结果
print("\n--- AI 输出 ---\n")
print(response.choices[0].message.content)