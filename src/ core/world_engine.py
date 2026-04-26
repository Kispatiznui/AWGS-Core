from models.world_state import WorldState

class WorldEngine:

    def step(self, world_state: WorldState):

        # simulación básica
        for rule in world_state.rules:
            if rule.condition == "water_level == low":
                for p in world_state.processes:
                    if p.name == "survival_process":
                        p.state_variables["thirst"] = "critical"

        world_state.time += 1
        world_state.history.append(world_state.dict())

        return world_state
