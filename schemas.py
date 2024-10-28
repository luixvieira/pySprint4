from pydantic import BaseModel
from datetime import date

class ProblemaCreate(BaseModel):
    descricao: str

class DiagnosticoCreate(BaseModel):
    problema_id: int
    descricao: str

class ProntuarioCreate(BaseModel):
    placa: str
    data: date
    descricao: str
