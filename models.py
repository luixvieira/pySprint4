from sqlalchemy import Column, Integer, String, Date, Sequence
from database import Base


# Definindo uma sequência para o campo id
id_sequence = Sequence('problema_id_seq', start=1, increment=1)

class Problema(Base):
    __tablename__ = "problemas"
    id = Column(Integer, id_sequence, primary_key=True, server_default=id_sequence.next_value())
    descricao = Column(String(255))


class Diagnostico(Base):
    __tablename__ = "diagnosticos"
    id = Column(Integer, primary_key=True)
    problema_id = Column(Integer)
    descricao = Column(String(255))

class Prontuario(Base):
    __tablename__ = "prontuarios"
    id = Column(Integer, primary_key=True)
    placa = Column(String(10))
    data = Column(Date)
    descricao = Column(String(255))
