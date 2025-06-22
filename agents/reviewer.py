from agents.groq_client import call_groq

def review_chapter(content):
    messages = [
        {"role": "system", "content": "You're a professional editor. Improve grammar, clarity, and flow."},
        {"role": "user", "content": content}
    ]
    return call_groq(messages, temperature=0.6)
