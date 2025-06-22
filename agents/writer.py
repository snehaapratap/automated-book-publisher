from agents.groq_client import call_groq

def spin_chapter(content):
    messages = [
        {"role": "system", "content": "Rewrite this chapter with a modern tone, preserving meaning."},
        {"role": "user", "content": content}
    ]
    return call_groq(messages, temperature=0.8)
