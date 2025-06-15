from openai import OpenAI
openai = OpenAI()

def spin_chapter(content):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Rewrite this chapter with a modern tone, preserving meaning."},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content
