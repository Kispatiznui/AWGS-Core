import copy

class BranchingEngine:

    def generate_branches(self, world_state, variations=3):

        branches = []

        for i in range(variations):

            new_state = copy.deepcopy(world_state)

            # pequeña variación artificial
            for p in new_state["processes"]:
                p["state"]["variation"] = i

            branches.append(new_state)

        return branches
