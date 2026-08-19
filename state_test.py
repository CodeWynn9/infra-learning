from agent_app.state import AgentState, Message


state = AgentState(
    system_prompt="你是一个简洁的AI助手。"
)

state.history.append(
    Message(
        role="user",
        content="什么是 AI Agent？"
    )
)

print(state)
print(state.model_dump())
