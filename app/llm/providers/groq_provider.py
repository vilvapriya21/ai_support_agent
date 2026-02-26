import requests
from app.llm.config import LLMConfig


class GroqProvider:
    BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {LLMConfig.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": LLMConfig.GROQ_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0
        }

        try:
            response = requests.post(
                self.BASE_URL,
                headers=headers,
                json=payload,
                timeout=LLMConfig.TIMEOUT
            )

            response.raise_for_status()
            result = response.json()

            return result["choices"][0]["message"]["content"].strip()

        except requests.exceptions.RequestException as e:
            return f"LLM connection error: {str(e)}"
