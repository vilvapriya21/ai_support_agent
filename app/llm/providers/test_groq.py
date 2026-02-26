import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "You are a JSON generator."},
        {"role": "user", "content": "Return exactly this JSON: {\"test\": \"working\"}"}
    ],
    "temperature": 0
}

response = requests.post(URL, headers=headers, json=payload)

print("STATUS:", response.status_code)
print("RAW RESPONSE:")
print(response.text)
