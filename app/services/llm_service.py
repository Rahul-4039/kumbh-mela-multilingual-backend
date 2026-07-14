import json

from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)


class LLMService:

    @staticmethod
    def ask(message: str):

        completion = client.chat.completions.create(
            model=GROQ_MODEL,

            messages=[
                {
                    "role": "system",
                    "content": """
You are a multilingual AI assistant.

Always reply ONLY in valid JSON.

Rules:
1. Reply in the SAME language as the user's input.
2. Detect the language yourself.
3. Return ONLY JSON.
4. Do not wrap JSON inside markdown.

Format:

{
    "language":"en",
    "answer":"Hello!"
}

Supported language codes:

en
hi
mr
ta
te
kn
ml
gu
bn
pa
od
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ],

            temperature=0.3,
        )

        content = completion.choices[0].message.content

        return json.loads(content)