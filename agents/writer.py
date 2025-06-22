import requests
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "mixtral-8x7b-32768"

def spin_chapter(content):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Rewrite this chapter with a modern tone, preserving meaning."},
            {"role": "user", "content": content}
        ],
        "temperature": 0.7
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
