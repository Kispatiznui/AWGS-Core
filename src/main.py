import time
import matplotlib.pyplot as plt

from src.core.nlp_engine import NLPEngine
from src.core.ontology_engine import OntologyEngine
from src.core.relational_engine import RelationalEngine
from src.core.rule_engine import RuleEngine
from src.core.world_engine import WorldEngine
from src.core.state_manager import StateManager
from src.memory.world_memory import WorldMemory
from src.narrative.narrator_engine import NarratorEngine


# -------------------------------------------------
# UTIL
# -------------------------------------------------

def print_section(title):
    print("\n" + "=" * 60)
    print(f"🧠 {title}")
    print("=" * 60)


def clean_json(output):
    if isinstance(output, dict):
        return output

    try:
        import json
        return json.loads(output)
    except:
        return {
            "entities": [],
            "actions": [],
            "context": str(output)
        }


# -------------------------------------------------
# MAIN
# -------------------------------------------------

def run():

    print_section("AWGS-Core Simulation Engine")

    text = input("Describe your world:\n> ")

    # -------------------------
    # INIT SYSTEM
    # -------------------------
    nlp = NLPEngine()
    ontology = OntologyEngine()
    relations = RelationalEngine()
    rules = RuleEngine()
    world = WorldEngine()
    memory = WorldMemory()
    narrator = NarratorEngine()

    state_manager = StateManager(world, None, memory)

    # -------------------------
    # NLP
    # -------------------------
    print_section("NLP Processing")

    concepts = clean_json(nlp.extract(text))
    print(concepts)

    # -------------------------
    # ONTOLOGY
    # -------------------------
    print_section("Ontology")

    processes = ontology.build(concepts)
    print(processes)

    # -------------------------
    # RELATIONS
    # -------------------------
    print_section("Relations")

    rels = relations.connect(processes)
    print(rels)

    # -------------------------
    # RULES
    # -------------------------
    print_section("Rules")

    rls = rules.generate(rels)
    print(rls)

    # -------------------------
    # WORLD STATE
    # -------------------------
    world_state = {
        "processes": processes,
        "relations": rels,
        "rules": rls,
        "time": 0
    }

    # -------------------------
    # SIMULATION
    # -------------------------
    print_section("Simulation Start")

    steps = 10

    for step in range(steps):

        print(f"\n--- Step {step+1} ---")

        result = state_manager.step(world_state)
        world_state = result["state"]

        print("Time:", world_state["time"])

        time.sleep(0.2)

    # -------------------------
    # FINAL PREDICTION
    # -------------------------
    print_section("Final Prediction")

    print(result["prediction"])

    # -------------------------
    # NARRATOR (FORZADO A SALIR)
    # -------------------------
    print_section("Narrative Output")

    story = narrator.generate(world_state)

    # 🔥 FIX CRÍTICO: asegurar string
    if isinstance(story, dict):
        story = story.get("text") or str(story)

    print(story)

    # -------------------------
    # MEMORY + MATPLOTLIB
    # -------------------------
    print_section("Memory Visualization")

    history = memory.history

    if len(history) == 0:
        print("No memory recorded")
        return

    times = []
    process_counts = []

    for h in history:
        times.append(h["time"])
        process_counts.append(len(h["state"]["processes"]))

    plt.figure()
    plt.plot(times, process_counts)
    plt.title("Process Evolution Over Time")
    plt.xlabel("Time")
    plt.ylabel("Active Processes")

    plt.tight_layout()
    plt.show()

    print_section("Simulation Completed")


# -------------------------------------------------
# ENTRY
# -------------------------------------------------

if __name__ == "__main__":
    run()