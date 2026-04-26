import os
import json
import openai

class NLPEngine:

    def __init__(self, config_path="config/llm_config.json"):

        with open(config_path) as f:
            config = json.load(f)

        self.model = config["model"]
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def extract(self, text):

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Extract key concepts as a JSON list."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        return response["choices"][0]["message"]["content"]
