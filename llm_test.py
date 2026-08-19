import os
from dotenv import load_dotenv
from agent_app.llm_client import LLMClient

load_dotenv()

llm = LLMClient(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3.8-max"
)
messages = [
    {"role": "system", "content": "你是一个简洁的AI助手。"},
    {"role": "user", "content": "什么是AI Agent？"}
]

answer = llm.chat(messages)

print(answer)
