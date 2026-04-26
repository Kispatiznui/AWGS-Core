from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine
from core.state_manager import StateManager
from memory.world_memory import WorldMemory


def test_simulation_step():

    world = WorldEngine()
    anticipation = AnticipatoryEngine()
    memory = WorldMemory()

    state_manager = StateManager(world, anticipation, memory)

    world_state = {
        "processes": [{"process": "human", "state": {}}],
        "relations": [],
        "rules": [],
        "time": 0
    }

    result = state_manager.step(world_state)

    assert result["state"]["time"] >= 0
