import requests
from app.llm.config import LLMConfig


class OllamaProvider:

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        full_prompt = self._format_prompt(system_prompt, user_prompt)

        try:
            response = requests.post(
                f"{LLMConfig.OLLAMA_BASE_URL}/api/generate",
                json={
                    "model": LLMConfig.OLLAMA_MODEL,
                    "prompt": full_prompt,
                    "stream": False
                },
                timeout=LLMConfig.TIMEOUT
            )

            response.raise_for_status()
            result = response.json()

            return result.get("response", "").strip()

        except requests.exceptions.RequestException as e:
            return f"LLM connection error: {str(e)}"

    def _format_prompt(self, system_prompt: str, user_prompt: str) -> str:
        return f"""
{system_prompt}

{user_prompt}
"""
