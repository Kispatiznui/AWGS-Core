class WorldMemory:

    def __init__(self):
        self.history = []

    def store(self, state):
        self.history.append(state)
