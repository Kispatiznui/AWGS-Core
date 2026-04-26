from src.models.world_state import WorldState


class StateManager:

    def __init__(self, world_engine, anticipation_engine, memory):
        self.world = world_engine
        self.anticipation = anticipation_engine
        self.memory = memory
        self.time = 0

    # -------------------------------------------------
    # STEP PRINCIPAL (COMPATIBLE)
    # -------------------------------------------------
    def step(self, world_state):

        # ---------------------------
        # 0. NORMALIZAR INPUT
        # ---------------------------
        if isinstance(world_state, WorldState):
            state = world_state
        else:
            state = WorldState.from_dict(world_state)

        # ---------------------------
        # 1. AVANZAR TIEMPO GLOBAL
        # ---------------------------
        self.time += 1
        state.time = self.time

        processes = state.processes
        relations = state.relations
        rules = state.rules

        # ---------------------------
        # 2. EVOLUCIÓN DEL SISTEMA
        # ---------------------------

        for p in processes:
            if p.get("state") == "active":
                intensity = p.get("intensity", 1)
                p["intensity"] = intensity + 0.1 * max(1, len(relations))

        for r in rules:
            if isinstance(r, dict):
                r["stability"] = r.get("stability", 1.0) - 0.01

        # ---------------------------
        # 3. MEMORIA DEL MUNDO
        # ---------------------------

        self.memory.history.append({
            "time": self.time,
            "state": {
                "processes": processes,
                "relations": relations,
                "rules": rules
            }
        })

        # ---------------------------
        # 4. MÉTRICAS DEL SISTEMA
        # ---------------------------

        active_processes = len([
            p for p in processes if p.get("state") == "active"
        ])

        relation_count = len(relations)
        rule_count = len(rules)

        system_density = active_processes + relation_count + rule_count

        # ---------------------------
        # 5. PREDICCIÓN EMERGENTE
        # ---------------------------

        if active_processes > relation_count:
            trend = "expansión de procesos"
        elif relation_count > active_processes:
            trend = "formación de estructuras relacionales"
        else:
            trend = "equilibrio dinámico del sistema"

        instability = abs(active_processes - relation_count)

        prediction = {
            "time": self.time,
            "active_processes": active_processes,
            "relations": relation_count,
            "rules": rule_count,
            "system_density": system_density,
            "instability_index": instability,
            "trend": trend,
            "summary": f"El sistema evoluciona hacia {trend}"
        }

        # ---------------------------
        # 6. SALIDA FINAL (COMPATIBLE MAIN)
        # ---------------------------

        return {
            "state": state.to_dict(),   # 🔥 clave para no romper main
            "prediction": prediction
        }