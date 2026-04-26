from core.world_engine import WorldEngine
from core.anticipatory_engine import AnticipatoryEngine

class StateManager:

    def __init__(self):
        self.world_engine = WorldEngine()
        self.anticipatory_engine = AnticipatoryEngine()

    def step(self, world_state):

        world_state = self.world_engine.step(world_state)
        predictions = self.anticipatory_engine.predict(world_state)

        return {
            "world": world_state,
            "predictions": predictions
        }
