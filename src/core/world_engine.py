class WorldEngine:

    def step(self, state):

        for p in state["processes"]:
            p["state"]["energy"] = p["state"].get("energy", 1) - 0.1

        return state
