import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class NarratorEngine:

    def __init__(self):

        # -------------------------------------------------
        # 1. CARGA DE API KEY
        # -------------------------------------------------
        self.api_key = os.getenv("GEMINI_API_KEY")

        self.use_llm = bool(self.api_key)

        self.model = None

        # -------------------------------------------------
        # 2. CONFIGURAR GEMINI SI EXISTE KEY
        # -------------------------------------------------
        if self.use_llm:

            try:
                genai.configure(api_key=self.api_key)

                # 🔥 NO hardcodear modelo, detectar automáticamente
                self.model = self._init_model()

            except Exception as e:
                print("⚠️ Gemini config failed:", e)
                self.model = None

    # -------------------------------------------------
    # 3. SELECCIÓN AUTOMÁTICA DE MODELO (CRÍTICO)
    # -------------------------------------------------
    def _init_model(self):

        try:
            models = genai.list_models()

            for m in models:

                # Solo modelos que soportan generación de texto
                if "generateContent" in m.supported_generation_methods:

                    print(f"🧠 Narrator model selected: {m.name}")
                    return genai.GenerativeModel(m.name)

        except Exception as e:
            print("⚠️ Model discovery failed:", e)

        return None

    # -------------------------------------------------
    # 4. FUNCIÓN PRINCIPAL
    # -------------------------------------------------
    def generate(self, world_state, prediction=None):

        summary = {
            "time": world_state.get("time"),
            "processes": world_state.get("processes", [])[:3],
            "relations": world_state.get("relations", [])[:3],
            "rules": world_state.get("rules", [])[:3]
        }

        # -------------------------------------------------
        # 5. MODO IA (SI DISPONIBLE)
        # -------------------------------------------------
        if self.model:

            try:

                prompt = f"""
You are a scientific system narrator.

Describe emergent behavior in 3–5 lines.

Focus on:
- system stability
- interaction pressure
- emergent structures
- evolution over time

WORLD STATE:
{json.dumps(summary, indent=2)}

PREDICTION:
{json.dumps(prediction, indent=2) if prediction else "None"}
"""

                response = self.model.generate_content(prompt)

                # 🔥 seguridad: evitar None o respuestas vacías
                if response and hasattr(response, "text"):
                    return response.text

            except Exception as e:
                print("⚠️ Gemini runtime failed, using fallback:", e)

        # -------------------------------------------------
        # 6. FALLBACK LOCAL (SEGURO SIEMPRE)
        # -------------------------------------------------
        processes = summary.get("processes", [])
        relations = summary.get("relations", [])
        rules = summary.get("rules", [])

        active = len(processes)
        rel = len(relations)
        rls = len(rules)

        # lógica narrativa emergente simple
        if rel > active:
            trend = "dominancia de estructuras relacionales"
        elif active > rel:
            trend = "expansión de entidades activas"
        else:
            trend = "equilibrio dinámico emergente"

        return (
            f"El sistema evoluciona en el tiempo {summary.get('time')}. "
            f"Se observan {active} procesos interactuando con {rel} relaciones y {rls} reglas. "
            f"El entorno muestra {trend}, manteniendo coherencia sistémica."
        )