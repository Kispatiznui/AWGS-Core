from pydantic import BaseModel
from typing import List, Dict, Any

class Process(BaseModel):
    id: str
    name: str
    actors: List[str]
    environment: str
    state_variables: Dict[str, Any]
