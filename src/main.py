import json
import time

from core.nlp_engine import NLPEngine
from core.ontology_engine import OntologyEngine
from core.relational_engine import RelationalEngine
from core.rule_engine import RuleEngine
from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory

from visualization.graph_visualizer import GraphVisualizer
from persistence.save_load import SaveLoad
from simulation.replay_engine import ReplayEngine
from simulation.branching_engine import BranchingEngine


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
    print("\n" + "="*60)
    print(f"🧠 {title}")
    print("="*60)


def load_config():
    try:
        with open("config/system_config.json") as f:
            return json.load(f)
    except:
        return {
            "simulation_steps": 3,
            "debug": True
        }


# ---------------------------
# MAIN
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

    visualizer = GraphVisualizer()
    saver = SaveLoad()
    replay = ReplayEngine()
    branch_engine = BranchingEngine()

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
    print(json.dumps(rels[:5], indent=2))

    # ---------------------------
    # RULES
    # ---------------------------
    print_section("Rules")

    rls = rules.generate(rels)
    print(json.dumps(rls[:5], indent=2))

    # ---------------------------
    # ESTADO INICIAL
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
    # SIMULACIÓN MULTI-STEP
    # ---------------------------
    print_section("Simulation Start")

    for step in range(steps):

        print(f"\n--- Step {step+1} ---")

        result = state_manager.step(world_state)
        world_state = result["state"]

        if debug:
            print("Time:", world_state["time"])
            print("Processes snapshot:")
            print(json.dumps(world_state["processes"][:2], indent=2))

        time.sleep(0.5)

    # ---------------------------
    # PREDICCIÓN FINAL
    # ---------------------------
    print_section("Final Prediction")
    print(json.dumps(result["prediction"], indent=2))

    # ---------------------------
    # VISUALIZACIÓN
    # ---------------------------
    print_section("World Visualization (Graph)")
    try:
        visualizer.visualize(world_state)
    except Exception as e:
        print("⚠️ Visualization error:", e)

    # ---------------------------
    # GUARDAR MUNDO
    # ---------------------------
    print_section("Saving World")

    try:
        filepath = saver.save(world_state)
        print(f"💾 Saved at: {filepath}")
    except Exception as e:
        print("⚠️ Save error:", e)

    # ---------------------------
    # REPLAY
    # ---------------------------
    print_section("Replay Simulation")

    try:
        replay.replay(memory, delay=0.5)
    except Exception as e:
        print("⚠️ Replay error:", e)

    # ---------------------------
    # MULTI-BRANCH
    # ---------------------------
    print_section("Parallel Futures (Branches)")

    try:
        branches = branch_engine.generate_branches(world_state, variations=3)

        for i, b in enumerate(branches):
            print(f"\n Branch {i}")
            print(json.dumps(b["processes"][:1], indent=2))

    except Exception as e:
        print(" Branching error:", e)

    # ---------------------------
    # MEMORIA
    # ---------------------------
    print_section("Memory Summary")

    print(f"Stored states: {len(memory.history)}")

    print_section("Simulation Completed")


# ---------------------------
# ENTRYPOINT
# ---------------------------

if __name__ == "__main__":
    run()
