from groq import Groq
from app.config import GROQ_API_KEY, GROQ_MODEL

client = Groq(
    api_key=GROQ_API_KEY
)


class LLMService:

    @staticmethod
    def ask(message: str):

        completion = client.chat.completions.create(
            model=GROQ_MODEL,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a multilingual AI assistant.\n"
                        "Always reply in the SAME language as the user's input.\n"
                        "Do not translate unless the user explicitly asks."
                    )
                },
                {
                    "role": "user",
                    "content": message
                }
            ],

            temperature=0.3,
        )

        return completion.choices[0].message.content