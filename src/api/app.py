from fastapi import FastAPI
from pydantic import BaseModel

# Importar motores
from core.nlp_engine import NLPEngine
from core.ontology_engine import OntologyEngine
from core.relational_engine import RelationalEngine
from core.rule_engine import RuleEngine
from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory

app = FastAPI()

# ----------- MODELO DE INPUT -----------
class SimulationInput(BaseModel):
    text: str


# ----------- INICIALIZACIÓN -----------
nlp = NLPEngine(api_key="TU_API_KEY_AQUI")
ontology = OntologyEngine()
relations = RelationalEngine()
rules = RuleEngine()
world = WorldEngine()
anticipation = AnticipatoryEngine()
memory = WorldMemory()

state_manager = StateManager(world, anticipation, memory)


# ----------- ENDPOINT PRINCIPAL -----------
@app.post("/simulate")
def simulate(input: SimulationInput):

    # 1. NLP
    concepts = nlp.extract(input.text)

    #  si viene como string JSON
    if isinstance(concepts, str):
        import json
        concepts = json.loads(concepts)

    # 2. Ontología
    processes = ontology.build(concepts)

    # 3. Relaciones
    rels = relations.connect(processes)

    # 4. Reglas
    rls = rules.generate(rels)

    # 5. Estado inicial
    world_state = {
        "processes": processes,
        "relations": rels,
        "rules": rls,
        "time": 0
    }

    # 6. Simulación
    result = state_manager.step(world_state)

    return result
