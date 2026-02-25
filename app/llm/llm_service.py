from app.llm.config import LLMConfig
from app.llm.providers.ollama_provider import OllamaProvider
import json


class LLMService:

    def __init__(self):
        self.provider = self._load_provider()

    def _load_provider(self):
        if LLMConfig.PROVIDER == "ollama":
            return OllamaProvider()
        elif LLMConfig.PROVIDER == "grok":
            raise NotImplementedError("Grok provider not implemented yet")
        else:
            raise ValueError("Unsupported LLM provider")

    # 🔹 Generic generation
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        return self.provider.generate(system_prompt, user_prompt)

    # 🔹 Intent classification (structured)
    def classify_intent(self, system_prompt: str, user_message: str) -> str:
        raw_response = self.provider.generate(system_prompt, user_message)

        try:
            parsed = json.loads(raw_response)
            return parsed.get("intent", "general_support")
        except json.JSONDecodeError:
            # fallback safety
            return "general_support"
