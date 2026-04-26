import os
import json


class NLPEngine:
    """
    NLP híbrido para AWGS-Core:
    - OpenAI si está disponible
    - fallback local si falla o no hay cuota
    - salida SIEMPRE consistente
    """

    def __init__(self):

        self.api_key = os.getenv("AIzaSyAf1DD3v8lF4rLa1nXZ7KRWfUZ1A8xiBd4")
        self.use_llm = self.api_key is not None

        if self.use_llm:
            from openai import OpenAI
            self.client = OpenAI()
        else:
            self.client = None

    # -------------------------------------------------
    # INTERFAZ PRINCIPAL
    # -------------------------------------------------
    def extract(self, text: str):

        try:
            if self.use_llm:
                return self._extract_with_llm(text)
        except Exception as e:
            print("⚠️ LLM failed, switching to fallback:", e)

        return self._extract_local(text)

    # -------------------------------------------------
    # IA REAL
    # -------------------------------------------------
    def _extract_with_llm(self, text: str):

        prompt = f"""
Devuelve SOLO JSON válido con este esquema:

{{
  "entities": [
    {{"name": "", "type": "agent|environment|object"}}
  ],
  "actions": [],
  "context": ""
}}

Texto:
{text}
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Eres un motor de ontologías para simulaciones de mundos."
                },
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except:
            return {
                "entities": [],
                "actions": [],
                "context": text,
                "raw": content,
                "mode": "llm_unparsed"
            }

    # -------------------------------------------------
    # FALLBACK LOCAL (ESTRUCTURADO BIEN)
    # -------------------------------------------------
    def _extract_local(self, text: str):

        words = text.lower().split()

        stopwords = {
            "un", "una", "el", "la", "en", "y", "de", "los", "las", "con", "para"
        }

        entities = []
        actions = []

        for w in words:

            if w in stopwords:
                continue

            # ENTIDADES SIMPLES
            if w in ["sabana", "bosque", "selva", "ciudad"]:
                entities.append({"name": w, "type": "environment"})

            elif w in ["hombre", "mujer", "animal", "persona"]:
                entities.append({"name": w, "type": "agent"})

            elif w in ["sentado", "corre", "come", "duerme"]:
                actions.append(w)

            else:
                entities.append({"name": w, "type": "object"})

        # eliminar duplicados
        unique_entities = []
        seen = set()

        for e in entities:
            if e["name"] not in seen:
                unique_entities.append(e)
                seen.add(e["name"])

        return {
            "entities": unique_entities,
            "actions": actions,
            "context": text,
            "mode": "fallback"
        }