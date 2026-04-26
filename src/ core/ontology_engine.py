class OntologyEngine:

    def build(self, concepts):

        processes = []

        for c in concepts:
            processes.append({
                "process": f"{c}_process",
                "type": "dynamic",
                "state": {}
            })

        return processes
