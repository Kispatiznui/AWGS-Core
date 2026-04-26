import time
import json

class ReplayEngine:

    def replay(self, memory, delay=1):

        print("\n🔁 REPLAY START\n")

        for i, state in enumerate(memory.history):

            print(f"\n--- Replay Step {i} ---")
            print(json.dumps(state, indent=2))

            time.sleep(delay)
