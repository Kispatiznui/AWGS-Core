class RelationalEngine:

    def connect(self, processes):

        relations = []

        for p in processes:
            for q in processes:
                if p != q:
                    relations.append({
                        "from": p["process"],
                        "to": q["process"],
                        "type": "interaction"
                    })

        return relations
