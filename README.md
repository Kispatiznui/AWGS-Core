AWGS-Core

Adaptive World Generative System

AWGS-Core es un framework de simulación basado en procesos que genera mundos dinámicos a partir de entradas en lenguaje natural mediante extracción semántica asistida por modelos de IA, modelado relacional y sistemas de reglas evolutivas.

Este proyecto fue desarrollado como un experimento de investigación con apoyo de herramientas de inteligencia artificial (incluyendo asistencia de modelos tipo ChatGPT) para acelerar la exploración de arquitectura, ideas y estructuración del sistema.

Overview

AWGS-Core transforma descripciones en lenguaje natural en mundos simulados en evolución.

En lugar de modelar entidades estáticas, el sistema trabaja con:

Procesos en lugar de objetos
Reglas dinámicas en lugar de lógica fija
Espacios de estado en evolución
Simulación anticipatoria de futuros posibles
Core Principle

La realidad puede modelarse mejor como un sistema de procesos interactuando entre sí, en lugar de entidades aisladas.

System Architecture

Natural Language Input
→ NLP Engine
→ Process Ontology Engine
→ Relational Engine
→ Rule Generation Engine
→ World Simulation Engine
→ Anticipatory Engine
→ Feedback Loop (Evolución del sistema)

Modules
1. NLP Engine (asistido por IA)

Convierte texto en conceptos estructurados.

Ejemplo de entrada:
“Un humano en una sabana enfrentando sequía”

Salida:

{
  "concepts": ["human", "savanna", "drought"]
}

Tecnologías: modelos LLM, extracción semántica, normalización de texto.

2. Process Ontology Engine

Convierte conceptos en procesos dinámicos.

{
  "processes": [
    {
      "name": "survival_process",
      "actors": ["human"],
      "environment": "savanna",
      "state_variables": ["resource_availability"]
    }
  ]
}
3. Relational Engine

Define relaciones entre elementos del sistema.

Tipos de relación:

dependencia
competencia
adaptación
cooperación
{
  "relations": [
    {
      "from": "human",
      "to": "resource_system",
      "type": "dependency"
    }
  ]
}
4. Rule Engine

Genera reglas dinámicas del sistema.

{
  "rules": [
    {
      "if": "resource_low",
      "then": "increase_survival_pressure"
    }
  ]
}
5. World Simulation Engine

Ejecuta la evolución del sistema en el tiempo:

State(t) → procesos + reglas → State(t+1)

6. Anticipatory Engine

Genera predicciones de posibles futuros.

{
  "scenarios": [
    {
      "name": "migration_event",
      "probability": 0.65
    }
  ]
}
System Flow

Input → NLP → Ontology → Relations → Rules → Simulation → Prediction → Feedback

Project Structure

AWGS-Core/
│
├── src/
│ ├── core/
│ │ ├── nlp_engine.py
│ │ ├── ontology_engine.py
│ │ ├── relational_engine.py
│ │ ├── rule_engine.py
│ │ ├── world_engine.py
│ │ ├── anticipatory_engine.py
│ │
│ ├── models/
│ ├── simulation/
│ ├── utils/
│ ├── api/
│ └── main.py
│
├── examples/
├── tests/
├── docs/
├── config/
└── README.md

Installation
git clone https://github.com/yourname/awgs-core.git
cd awgs-core
pip install -r requirements.txt
How to Run (MVP)
python src/main.py
Example Execution

Input:
“human in a savanna with long-term drought”

Output:

{
  "world_state": {
    "processes": ["survival", "resource_search"],
    "pressure": "high"
  },
  "prediction": {
    "migration_likelihood": 0.72
  }
}
Key Features
Extracción semántica asistida por IA
Ontología basada en procesos
Generación dinámica de reglas
Simulación emergente de sistemas
Modelado anticipatorio de futuros
Estructura evolutiva del mundo
Tech Stack
Python 3.10+
LLM APIs (OpenAI o equivalentes)
NetworkX (relaciones)
Pydantic (modelado)
JSON state engine
Research Context

Este proyecto se basa en ideas de:

Dynamic Systems Theory
Process Ontology (Rescher)
Anticipatory Systems (Rosen, Poli)
Knowledge Graphs
Agent-Based Modeling
Limitations
Prototipo de investigación en etapa temprana
Dependencia de la calidad semántica del LLM
Posible explosión del espacio de estados en simulaciones complejas
Requiere optimización para escalabilidad
Roadmap
Integración completa del NLP
Sistema de ontología estable
Motor de reglas avanzado
Motor de simulación completo
Visualización web del mundo
Editor interactivo de mundos
Sistema multi-agente evolutivo
Contribution

Este es un framework experimental de investigación. Se aceptan contribuciones mediante pull requests.

License

MIT License

Author

Proyecto de investigación explorando:

Sistemas de simulación generativa
Ontologías computacionales
Modelado anticipatorio

Desarrollado con apoyo de herramientas de IA para estructuración, diseño conceptual y asistencia en implementación.
