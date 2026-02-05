import os
import openai
from dotenv import load_dotenv

load_dotenv()

def call_llm(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
