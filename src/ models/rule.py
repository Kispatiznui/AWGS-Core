from pydantic import BaseModel

class Rule(BaseModel):
    condition: str
    effect: str
