class RelationalEngine:

    def connect(self, processes):

        relations = []

        for p in processes:

            relations.append({
                "from": p["name"],
                "type": p["type"],
                "relation": "exists"
            })

        return relations
