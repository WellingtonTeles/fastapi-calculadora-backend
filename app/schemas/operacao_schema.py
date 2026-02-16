from pydantic import BaseModel

class Operacao(BaseModel):
    a: float
    b: float

class Numero(BaseModel):
    x: float