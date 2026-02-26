import json
import re
from app.llm.config import LLMConfig
from app.llm.providers.ollama_provider import OllamaProvider
from app.llm.providers.ollama_provider import OllamaProvider
from app.llm.providers.groq_provider import GroqProvider

class LLMService:
    def __init__(self):
        self.provider = self._load_provider()

    def _load_provider(self):
        if LLMConfig.PROVIDER == "ollama":
            return OllamaProvider()
        elif LLMConfig.PROVIDER == "groq":
            return GroqProvider()
        else:
            raise ValueError("Unsupported LLM provider")

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        return self.provider.generate(system_prompt, user_prompt)

    def classify_intent(self, system_prompt: str, user_message: str) -> str:
        raw_response = self.provider.generate(system_prompt, user_message)

        try:
            parsed = json.loads(raw_response)
            return parsed.get("intent", "general_support")
        except json.JSONDecodeError:
            return "general_support"

    def _validate_response(self, response: dict) -> dict:
        allowed_types = {"answer", "clarification", "out_of_scope"}

        if (
            not isinstance(response, dict)
            or "type" not in response
            or "message" not in response
            or response["type"] not in allowed_types
        ):
            return {
                "type": "answer",
                "message": "Unable to process request at the moment."
            }

        return response

    def generate_structured(self, system_prompt: str, user_prompt: str) -> dict:
        raw_response = self.provider.generate(system_prompt, user_prompt)
        print("RAW LLM RESPONSE:")
        print(raw_response)

        if raw_response.startswith("LLM connection error"):
            return {
                "type": "answer",
                "message": "Unable to process request at the moment."
            }

        try:
            parsed = json.loads(raw_response)
            return self._validate_response(parsed)

        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", raw_response, re.DOTALL)
            if match:
                try:
                    parsed = json.loads(match.group())
                    return self._validate_response(parsed)
                except json.JSONDecodeError:
                    pass

        return {
            "type": "answer",
            "message": "Unable to process request at the moment."
        }
