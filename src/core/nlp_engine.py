import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class NLPEngine:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")
        self.use_llm = self.api_key is not None

        if self.use_llm:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None

    # -------------------------------------------------
    # INTERFAZ PRINCIPAL
    # -------------------------------------------------
    def extract(self, text: str):

        try:
            if self.use_llm:
                return self._extract_with_llm(text)
        except Exception as e:
            print("⚠️ Gemini failed, fallback:", e)

        return self._extract_local(text)

    # -------------------------------------------------
    # GEMINI REAL
    # -------------------------------------------------
    def _extract_with_llm(self, text: str):

        prompt = f"""
You are an ontology extraction engine for a simulation system.

Extract ONLY meaningful semantic elements.

Return STRICT JSON:
{{
  "entities": [{{"name": "...", "type": "agent|object|environment"}}],
  "actions": ["..."],
  "context": "..."
}}

RULES:
- NO stopwords (a, el, en, una, etc)
- Focus on semantic meaning
- Keep ontology clean

TEXT:
{text}
"""

        response = self.model.generate_content(prompt)

        try:
            return json.loads(response.text)
        except:
            return {
                "entities": [],
                "actions": [],
                "context": text,
                "raw": response.text,
                "mode": "llm_parse_failed"
            }

    # -------------------------------------------------
    # FALLBACK LOCAL (ROBUSTO)
    # -------------------------------------------------
    def _extract_local(self, text: str):

        stopwords = {"el", "la", "una", "un", "en", "de", "y", "a", "los", "las"}

        words = [
            w for w in text.lower().split()
            if w not in stopwords
        ]

        entities = [{"name": w, "type": "object"} for w in words[:5]]

        return {
            "entities": entities,
            "actions": ["cooperación", "competencia", "adaptación", "supervivencia"],
            "context": text,
            "mode": "fallback"
        }