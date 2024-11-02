from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração para o SQLite (um banco de dados leve que não requer instalação)
DATABASE_URL = "sqlite:///./test.db"

# Criação do engine para SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para os modelos
Base = declarative_base()
