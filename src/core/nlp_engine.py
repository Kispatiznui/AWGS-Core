import os
import json
from openai import OpenAI


class NLPEngine:
    """
    NLP real usando LLM (OpenAI)
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def extract(self, text: str):

        prompt = f"""
Eres un motor de análisis ontológico.

Convierte el texto en JSON estructurado con:
- entities: objetos o conceptos
- actions: verbos o procesos
- context: resumen del mundo

Texto:
{text}

Devuelve SOLO JSON válido.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un extractor de ontologías."},
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content

        # limpieza segura
        try:
            return json.loads(content)
        except:
            return {
                "error": "invalid_json_from_llm",
                "raw": content
            }