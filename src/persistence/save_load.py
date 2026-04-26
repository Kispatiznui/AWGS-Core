import json
import os
from datetime import datetime

class SaveLoad:

    def save(self, world_state, folder="saved_worlds"):

        os.makedirs(folder, exist_ok=True)

        filename = f"{folder}/world_{datetime.now().strftime('%H%M%S')}.json"

        with open(filename, "w") as f:
            json.dump(world_state, f, indent=2)

        return filename


    def load(self, filepath):

        with open(filepath, "r") as f:
            return json.load(f)
