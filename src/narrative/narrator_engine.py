import os
import json
import openai

class NarratorEngine:

    def __init__(self, model="gpt-4o-mini"):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model

    def narrate(self, world_state, prediction=None):

        # Reducimos tamaño (muy importante)
        summary = {
            "time": world_state.get("time"),
            "processes": world_state.get("processes", [])[:3],
            "relations": world_state.get("relations", [])[:3]
        }

        prompt = f"""
You are a scientific narrative engine.

Describe the current state of a simulated world in a clear, immersive, but concise way.

Focus on:
- environmental conditions
- survival pressure
- interactions between processes
- possible risks or evolution

World:
{json.dumps(summary, indent=2)}

Future:
{json.dumps(prediction, indent=2) if prediction else "None"}

Respond in 3-5 lines max.
"""

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You generate concise scientific narratives."},
                {"role": "user", "content": prompt}
            ]
        )

        return response["choices"][0]["message"]["content"]
