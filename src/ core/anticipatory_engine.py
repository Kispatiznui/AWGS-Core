class AnticipatoryEngine:

    def predict(self, world_state):

        predictions = []

        for p in world_state.processes:

            if p.name == "survival_process":
                predictions.append({
                    "scenario": "migration",
                    "probability": 0.7
                })

        return predictions
