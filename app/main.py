import os
from typing import Optional

from openai import OpenAI


class AIEngine:
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "")
        self.model_name = model_name or os.getenv("MODEL_NAME", "gpt-4o-mini")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def _fallback_response(self, prompt: str, mode: str) -> str:
        mode_map = {
            "chat": "You are in local chatbot mode. The AI engine is not configured yet, but your message was received and can be processed once an API key is set.",
            "assistant": "Code assistant mode is active. Add your model key and prompt the assistant with repository context for full code generation support.",
            "task": "Task automation mode is active. This starter is ready to orchestrate workflows once LLM access is configured.",
        }
        return f"{mode_map.get(mode, 'AI mode active')}\n\nOriginal input: {prompt}"

    def chat(self, message: str, context: str = "") -> str:
        if not self.client:
            return self._fallback_response(f"{message}\nContext: {context}", "chat")

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant for chatbot conversations."},
                {"role": "user", "content": f"{message}\n\nContext: {context}"},
            ],
        )
        return response.choices[0].message.content or "No response returned."

    def code_assist(self, prompt: str, repo_context: str = "") -> str:
        if not self.client:
            return self._fallback_response(f"{prompt}\nRepo context: {repo_context}", "assistant")

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a senior software engineer and coding assistant."},
                {"role": "user", "content": f"Provide a practical engineering answer.\n\nPrompt: {prompt}\n\nRepo context: {repo_context}"},
            ],
        )
        return response.choices[0].message.content or "No result generated."

    def automate_task(self, task: str) -> str:
        if not self.client:
            return self._fallback_response(task, "task")

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a task automation planner that creates actionable steps."},
                {"role": "user", "content": task},
            ],
        )
        return response.choices[0].message.content or "No task plan returned."
