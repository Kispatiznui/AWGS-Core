from models.rule import Rule

class RuleEngine:

    def generate_rules(self, processes, relations):

        rules = []

        for p in processes:
            if p.name == "resource_depletion_process":
                rules.append(Rule(
                    condition="water_level == low",
                    effect="increase_survival_pressure"
                ))

        return rules
