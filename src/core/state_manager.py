class StateManager:

    def __init__(self, world_engine, anticipation_engine, memory):
        self.world = world_engine
        self.anticipation = anticipation_engine
        self.memory = memory
        self.time = 0

    def step(self, world_state):

        # -------------------------------------------------
        # 🧠 0. PROTECCIÓN: evitar string como estado vivo
        # -------------------------------------------------
        if isinstance(world_state, str):
            import json
            world_state = json.loads(world_state)

        # -------------------------------------------------
        # 1. AVANZAR TIEMPO GLOBAL
        # -------------------------------------------------
        self.time += 1
        world_state["time"] = self.time

        processes = world_state.get("processes", [])
        relations = world_state.get("relations", [])
        rules = world_state.get("rules", [])

        # -------------------------------------------------
        # 2. EVOLUCIÓN DEL SISTEMA (DINÁMICA ONTOLÓGICA)
        # -------------------------------------------------

        for p in processes:

            if not isinstance(p, dict):
                continue

            # 🔥 asegurar estado consistente
            if "state" not in p:
                p["state"] = {"status": "active", "variation": 0}

            if isinstance(p["state"], str):
                p["state"] = {"status": p["state"], "variation": 0}

            # evolución de intensidad
            if p["state"].get("status") == "active":
                intensity = p.get("intensity", 1)
                p["intensity"] = intensity + 0.1 * max(1, len(relations))

        # -------------------------------------------------
        # 3. DINÁMICA DE REGLAS
        # -------------------------------------------------

        for r in rules:
            if isinstance(r, dict):
                r["stability"] = r.get("stability", 1.0) - 0.01

        # -------------------------------------------------
        # 4. 🧠 MEMORIA (FIX IMPORTANTE: SNAPSHOT INMUTABLE)
        # -------------------------------------------------

        import copy

        snapshot = {
            "time": self.time,
            "state": copy.deepcopy({
                "processes": processes,
                "relations": relations,
                "rules": rules
            })
        }

        self.memory.history.append(snapshot)

        # -------------------------------------------------
        # 5. MÉTRICAS EMERGENTES
        # -------------------------------------------------

        active_processes = len([
            p for p in processes
            if isinstance(p, dict)
            and isinstance(p.get("state"), dict)
            and p["state"].get("status") == "active"
        ])

        relation_count = len(relations)
        rule_count = len(rules)

        system_density = active_processes + relation_count + rule_count

        # -------------------------------------------------
        # 6. PREDICCIÓN EMERGENTE
        # -------------------------------------------------

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

        # -------------------------------------------------
        # 7. SALIDA FINAL
        # -------------------------------------------------

        return {
            "state": world_state,
            "prediction": prediction
        }