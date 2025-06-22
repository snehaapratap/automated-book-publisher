import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load GROQ_API_KEY from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "mixtral-8x7b-32768"

def call_groq(messages, model=DEFAULT_MODEL, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)

    # Logging
    print(f"\n[GROQ] Status Code: {response.status_code}")
    print(f"[GROQ] Response: {response.text}\n")

    try:
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ No valid message received.")
    except Exception as e:
        return f"❌ Exception during GROQ call: {str(e)}"
