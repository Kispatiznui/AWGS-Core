class StateManager:

    def __init__(self, world_engine, ant_engine, memory):
        self.world_engine = world_engine
        self.ant_engine = ant_engine
        self.memory = memory

    def step(self, state):

        new_state = self.world_engine.step(state)
        prediction = self.ant_engine.predict(new_state)

        self.memory.store(new_state)

        return {
            "state": new_state,
            "prediction": prediction
        }
