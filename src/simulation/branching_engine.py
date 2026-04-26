import copy


class BranchingEngine:

    def generate_branches(self, world_state, variations=3):

        branches = []

        # 🔴 protección: si viene string, no puede continuar
        if isinstance(world_state, str):
            return {"error": "invalid_world_state_string"}

        for i in range(variations):

            new_state = copy.deepcopy(world_state)

            processes = new_state.get("processes", [])

            for p in processes:

                # 🔥 asegurar estructura de state
                if not isinstance(p.get("state"), dict):
                    p["state"] = {
                        "status": p.get("state", "active"),
                        "variation": i
                    }
                else:
                    p["state"]["variation"] = i

            branches.append(new_state)

        return branches