from core.nlp_engine import NLPEngine
from core.ontology_engine import OntologyEngine
from core.relational_engine import RelationalEngine
from core.rule_engine import RuleEngine
from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory

import json

def run():

    print("🧠 AWGS-Core Simulation")
    print("------------------------")

    text = input("Describe your world: ")

    # Inicializar motores
    nlp = NLPEngine(api_key="TU_API_KEY_AQUI")
    ontology = OntologyEngine()
    relations = RelationalEngine()
    rules = RuleEngine()
    world = WorldEngine()
    anticipation = AnticipatoryEngine()
    memory = WorldMemory()

    state_manager = StateManager(world, anticipation, memory)

    # 1. NLP
    concepts = nlp.extract(text)

    if isinstance(concepts, str):
        concepts = json.loads(concepts)

    print("\n🧠 Concepts:", concepts)

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

    print("\n🌍 Initial World:")
    print(json.dumps(world_state, indent=2))

    # 6. Simulación
    result = state_manager.step(world_state)

    print("\n🔮 Prediction:")
    print(json.dumps(result["prediction"], indent=2))

    print("\n🌍 New State:")
    print(json.dumps(result["state"], indent=2))


if __name__ == "__main__":
    run()
