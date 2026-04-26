from pydantic import BaseModel
from typing import List
from .process import Process
from .relation import Relation
from .rule import Rule

class WorldState(BaseModel):
    time: int
    processes: List[Process]
    relations: List[Relation]
    rules: List[Rule]
    history: List[dict]
