import json
import os
import time

from core.nlp_engine import NLPEngine
from core.ontology_engine import OntologyEngine
from core.relational_engine import RelationalEngine
from core.rule_engine import RuleEngine
from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory


# ---------------------------
# UTILIDADES
# ---------------------------

def clean_json(output):
    try:
        return json.loads(output)
    except:
        start = output.find("[")
        end = output.rfind("]")
        return json.loads(output[start:end+1])


def print_section(title):
    print("\n" + "="*50)
    print(f"🧠 {title}")
    print("="*50)


# ---------------------------
# CONFIG
# ---------------------------

def load_config():
    with open("config/system_config.json") as f:
        return json.load(f)


# ---------------------------
# MAIN ENGINE
# ---------------------------

def run():

    config = load_config()
    steps = config.get("simulation_steps", 3)
    debug = config.get("debug", True)

    print_section("AWGS-Core Simulation Engine")

    text = input("Describe your world:\n> ")

    # ---------------------------
    # INICIALIZACIÓN
    # ---------------------------
    nlp = NLPEngine()
    ontology = OntologyEngine()
    relations = RelationalEngine()
    rules = RuleEngine()
    world = WorldEngine()
    anticipation = AnticipatoryEngine()
    memory = WorldMemory()

    state_manager = StateManager(world, anticipation, memory)

    # ---------------------------
    # NLP
    # ---------------------------
    print_section("NLP Processing")

    raw_concepts = nlp.extract(text)
    concepts = clean_json(raw_concepts)

    print("Concepts:", concepts)

    # ---------------------------
    # ONTOLOGY
    # ---------------------------
    print_section("Ontology Generation")

    processes = ontology.build(concepts)
    print(json.dumps(processes, indent=2))

    # ---------------------------
    # RELATIONS
    # ---------------------------
    print_section("Relations")

    rels = relations.connect(processes)
    print(json.dumps(rels[:5], indent=2))  # muestra parcial

    # ---------------------------
    # RULES
    # ---------------------------
    print_section("Rules")

    rls = rules.generate(rels)
    print(json.dumps(rls[:5], indent=2))

    # ---------------------------
    # INITIAL STATE
    # ---------------------------
    world_state = {
        "processes": processes,
        "relations": rels,
        "rules": rls,
        "time": 0
    }

    print_section("Initial World State")
    print(json.dumps(world_state, indent=2))

    # ---------------------------
    # SIMULATION LOOP
    # ---------------------------
    print_section("Simulation Start")

    for step in range(steps):

        print(f"\n--- Step {step+1} ---")

        result = state_manager.step(world_state)
        world_state = result["state"]

        if debug:
            print("Time:", world_state["time"])
            print("Processes state snapshot:")
            print(json.dumps(world_state["processes"][:2], indent=2))

        time.sleep(0.5)

    # ---------------------------
    # FINAL PREDICTION
    # ---------------------------
    print_section("Final Prediction")

    print(json.dumps(result["prediction"], indent=2))

    # ---------------------------
    # MEMORY SUMMARY
    # ---------------------------
    print_section("Memory Summary")

    print(f"Stored states: {len(memory.history)}")

    # ---------------------------
    # END
    # ---------------------------
    print_section("Simulation Completed")


# ---------------------------
# ENTRYPOINT
# ---------------------------

if __name__ == "__main__":
    run()
