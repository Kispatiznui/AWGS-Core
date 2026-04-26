class OntologyEngine:
    """
    Convierte conceptos en procesos ontológicos del mundo
    """

    def __init__(self):
        pass

    def build(self, concepts):
        """
        Convierte entidades del NLP en procesos del sistema
        """

        processes = []

        for entity in concepts.get("entities", []):
            processes.append({
                "name": entity,
                "type": "process",
                "state": "active"
            })

        return processes
