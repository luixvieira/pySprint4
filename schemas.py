from pydantic import BaseModel
from datetime import date

class ClienteBase(BaseModel):
    nome_cliente: str
    email_cliente: str
    telefone_cliente: str = None
    endereco_cliente: str = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id_cliente: int

    class Config:
        orm_mode = True


class VeiculoBase(BaseModel):
    placa: str
    modelo: str = None
    ano: int = None

class VeiculoCreate(VeiculoBase):
    id_cliente: int

class Veiculo(VeiculoBase):
    id_veiculo: int
    cliente: Cliente

    class Config:
        orm_mode = True


class DiagnosticoBase(BaseModel):
    descricao: str

class DiagnosticoCreate(DiagnosticoBase):
    id_veiculo: int

class Diagnostico(DiagnosticoBase):
    id_diagnostico: int
    veiculo: Veiculo

    class Config:
        orm_mode = True


class ProntuarioBase(BaseModel):
    descricao_conserto: str
    data_conserto: date

class ProntuarioCreate(ProntuarioBase):
    id_veiculo: int
    id_cliente: int

class Prontuario(ProntuarioBase):
    id_prontuario: int
    veiculo: Veiculo
    cliente: Cliente

    class Config:
        orm_mode = True
