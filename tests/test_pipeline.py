import json

from core.ontology_engine import OntologyEngine
from core.relational_engine import RelationalEngine
from core.rule_engine import RuleEngine
from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory


def test_full_pipeline():

    concepts = ["human", "savanna", "drought"]

    ontology = OntologyEngine()
    relations = RelationalEngine()
    rules = RuleEngine()
    world = WorldEngine()
    anticipation = AnticipatoryEngine()
    memory = WorldMemory()

    state_manager = StateManager(world, anticipation, memory)

    processes = ontology.build(concepts)
    rels = relations.connect(processes)
    rls = rules.generate(rels)

    world_state = {
        "processes": processes,
        "relations": rels,
        "rules": rls,
        "time": 0
    }

    result = state_manager.step(world_state)

    assert "state" in result
    assert "prediction" in result
    assert isinstance(result["state"], dict)
