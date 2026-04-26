class StateManager:

    def __init__(self, world_engine, anticipation_engine, memory):
        self.world = world_engine
        self.anticipation = anticipation_engine
        self.memory = memory
        self.time = 0

    def step(self, world_state):

        # ---------------------------
        # 1. AVANZAR TIEMPO GLOBAL
        # ---------------------------
        self.time += 1
        world_state["time"] = self.time

        processes = world_state.get("processes", [])
        relations = world_state.get("relations", [])
        rules = world_state.get("rules", [])

        # ---------------------------
        # 2. EVOLUCIÓN DEL SISTEMA
        # ---------------------------

        for p in processes:
            if p.get("state") == "active":
                intensity = p.get("intensity", 1)
                p["intensity"] = intensity + 0.1 * max(1, len(relations))

        # pequeñas dinámicas en reglas (si existen)
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

        # densidad del sistema (simple pero útil)
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

        # inestabilidad simple
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
        # 6. SALIDA FINAL
        # ---------------------------

        return {
            "state": world_state,
            "prediction": prediction
        }