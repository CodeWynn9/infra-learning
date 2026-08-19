from typing import Literal, TypedDict
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class AgentState(BaseModel):
    system_prompt: str
    history: list[Message] = Field(default_factory=list)
    summary_memory: str=""
