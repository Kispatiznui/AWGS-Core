from pydantic import BaseModel

class Relation(BaseModel):
    source: str
    target: str
    type: str  # dependency, conflict, cooperation, etc.
