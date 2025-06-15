from openai import OpenAI
openai = OpenAI()

def review_chapter(content):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a professional editor. Provide grammar fixes and style improvements."},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content
