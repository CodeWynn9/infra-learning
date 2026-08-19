import os

from dotenv import load_dotenv
from prompt_toolkit import prompt
from agent_app.llm_client import LLMClient

from agent_app.state import Agentstate,Message

# 最近最多保留 3 轮 = 6 条消息
MAX_RECENT_MESSAGES = 6


def summarize_messages(llm, old_messages, old_summary):
    messages = [
        {
            "role": "system",
            "content": "请总结对话，只保留重要事实、用户目标和重要上下文。"
        },
        {
            "role": "user",
            "content": f"""
已有摘要：
{old_summary}

需要继续总结的旧对话：
{old_messages}

请输出新的简洁摘要。
"""
        }
    ]

    return llm.chat(messages)


def update_memory(llm, state):
    history = state["history"]

    if len(history) <= MAX_RECENT_MESSAGES:
        return state

    old_messages = history[:-MAX_RECENT_MESSAGES]
    recent_messages = history[-MAX_RECENT_MESSAGES:]

    new_summary = summarize_messages(
        llm,
        old_messages,
        state["summary_memory"]
    )

    state["history"] = recent_messages
    state["summary_memory"] = new_summary

    return state

def build_messages(state, question):
    messages = [
        {
            "role": "system",
            "content": state["system_prompt"]
        }
    ]

    if state["summary_memory"]:
        messages.append({
            "role": "system",
            "content": f"之前对话摘要：{state['summary_memory']}"
        })

    messages.extend(state["history"])

    messages.append({
        "role": "user",
        "content": question
    })

    return messages

# 读取 .env
load_dotenv()


# 创建 LLM Client
llm = LLMClient(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
    model="qwen3.8-max"
)

state = {
    "system_prompt": "你是一个简洁的AI助手。",
    "history": [],
    "summary_memory": ""
}

while True:
    question = prompt("You: ")

    if question == "exit":
        break

    messages = build_messages(
        state,
        question
    )

    answer = llm.chat(messages)

    print("AI:", answer)

    state["history"].append({
        "role": "user",
        "content": question
    })

    state["history"].append({
        "role": "assistant",
        "content": answer
    })

    state = update_memory(
        llm,
        state
    )

    print("\n--- State Debug ---")
    print(state)
    print("-------------------\n")
