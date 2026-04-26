class WorldMemory:

    def __init__(self):
        # historial de estados del mundo
        self.history = []

    def add_state(self, world_state):
        """
        Guarda una copia segura del estado del mundo.
        Evita referencias mutables que rompen el historial.
        """

        import copy

        if not isinstance(world_state, dict):
            return

        snapshot = copy.deepcopy(world_state)

        # 🔥 seguridad extra: normalizar estructura mínima
        snapshot.setdefault("time", 0)
        snapshot.setdefault("processes", [])
        snapshot.setdefault("relations", [])
        snapshot.setdefault("rules", [])

        self.history.append(snapshot)

    def get_history(self):
        return self.history

    def clear(self):
        self.history = []