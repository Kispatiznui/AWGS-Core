from models.process import Process
import uuid

class OntologyEngine:

    def build_processes(self, concepts):

        processes = []

        if "human" in concepts:
            processes.append(Process(
                id=str(uuid.uuid4()),
                name="survival_process",
                actors=["human"],
                environment="unknown",
                state_variables={
                    "hunger": "medium",
                    "thirst": "high"
                }
            ))

        if "drought" in concepts:
            processes.append(Process(
                id=str(uuid.uuid4()),
                name="resource_depletion_process",
                actors=["environment"],
                environment="global",
                state_variables={
                    "water_level": "low"
                }
            ))

        return processes
