import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class LLMConfig:
    PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral:latest")

    TIMEOUT = int(os.getenv("LLM_TIMEOUT", 60))
