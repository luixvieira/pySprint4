from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "tb_cliente"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String(100), nullable=False)
    email_cliente = Column(String(255), nullable=False, unique=True)
    telefone_cliente = Column(String(20))
    endereco_cliente = Column(String(255))

    # Relacionamento com veículos e problemas
    veiculos = relationship("Veiculo", back_populates="cliente")
    prontuarios = relationship("Prontuario", back_populates="cliente")


class Veiculo(Base):
    __tablename__ = "tb_veiculo"
    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    placa = Column(String(10), nullable=False, unique=True)
    modelo = Column(String(255))
    ano = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("tb_cliente.id_cliente"))

    # Relacionamento com cliente e problemas
    cliente = relationship("Cliente", back_populates="veiculos")
    problemas = relationship("Diagnostico", back_populates="veiculo")


class Diagnostico(Base):
    __tablename__ = "tb_diagnostico"
    id_diagnostico = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255), nullable=False)
    id_veiculo = Column(Integer, ForeignKey("tb_veiculo.id_veiculo"))

    # Relacionamento com o veículo
    veiculo = relationship("Veiculo", back_populates="problemas")


class Prontuario(Base):
    __tablename__ = "tb_prontuario"
    id_prontuario = Column(Integer, primary_key=True, autoincrement=True)
    descricao_conserto = Column(String(255))
    data_conserto = Column(Date)
    id_veiculo = Column(Integer, ForeignKey("tb_veiculo.id_veiculo"))
    id_cliente = Column(Integer, ForeignKey("tb_cliente.id_cliente"))

    # Relacionamento com cliente e veículo
    cliente = relationship("Cliente", back_populates="prontuarios")
    veiculo = relationship("Veiculo")
