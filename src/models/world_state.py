from pydantic import BaseModel
from typing import List, Dict, Any


class WorldState(BaseModel):
    time: int = 0
    processes: List[Dict[str, Any]] = []
    relations: List[Dict[str, Any]] = []
    rules: List[Dict[str, Any]] = []