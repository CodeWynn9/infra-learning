import os
from openai import OpenAI


class LLMClient:
    def __init__(self, api_key, base_url, model):
        self.model = model

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        return response.choices[0].message.content
