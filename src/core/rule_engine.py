class RuleEngine:

    def generate(self, relations):

        rules = []

        for r in relations:

            rules.append({
                "if": f"exists_{r['from']}",
                "then": f"affect_{r['from']}",
                "type": r["type"]
            })

        return rules