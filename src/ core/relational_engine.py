from models.relation import Relation

class RelationalEngine:

    def build_relations(self, processes):

        relations = []

        for p in processes:
            if p.name == "survival_process":
                relations.append(Relation(
                    source=p.name,
                    target="resource_depletion_process",
                    type="dependency"
                ))

        return relations
