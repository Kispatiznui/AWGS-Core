class RuleEngine:

    def generate(self, relations):

        rules = []

        for r in relations:
            rules.append({
                "if": f"{r['from']}_changes",
                "then": f"affect_{r['to']}"
            })

        return rules
