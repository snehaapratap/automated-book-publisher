import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "mixtral-8x7b-32768"

def review_chapter(content):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You're a professional editor. Improve grammar, coherence, and clarity."},
            {"role": "user", "content": content}
        ],
        "temperature": 0.5
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
