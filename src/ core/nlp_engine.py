import openai

class NLPEngine:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def extract_concepts(self, text: str):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Extract key semantic concepts as a JSON list."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response["choices"][0]["message"]["content"]
