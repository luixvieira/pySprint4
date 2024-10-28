from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
import json
from typing import List
from datetime import date

# Cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas CRUD para Problema
@app.post("/problemas/", response_model=schemas.ProblemaCreate)
def criar_problema(problema: schemas.ProblemaCreate, db: Session = Depends(get_db)):
    db_problema = models.Problema(descricao=problema.descricao)
    db.add(db_problema)
    db.commit()
    db.refresh(db_problema)
    return db_problema

@app.get("/problemas/", response_model=List[schemas.ProblemaCreate])
def listar_problemas(db: Session = Depends(get_db)):
    return db.query(models.Problema).all()

@app.put("/problemas/{problema_id}")
def atualizar_problema(problema_id: int, problema: schemas.ProblemaCreate, db: Session = Depends(get_db)):
    db_problema = db.query(models.Problema).filter(models.Problema.id == problema_id).first()
    if db_problema is None:
        raise HTTPException(status_code=404, detail="Problema não encontrado")
    db_problema.descricao = problema.descricao
    db.commit()
    db.refresh(db_problema)
    return db_problema

@app.delete("/problemas/{problema_id}")
def excluir_problema(problema_id: int, db: Session = Depends(get_db)):
    db_problema = db.query(models.Problema).filter(models.Problema.id == problema_id).first()
    if db_problema is None:
        raise HTTPException(status_code=404, detail="Problema não encontrado")
    db.delete(db_problema)
    db.commit()
    return {"message": "Problema excluído com sucesso"}

# Rota para exportar problemas para JSON
@app.get("/problemas/exportar")
def exportar_problemas(db: Session = Depends(get_db)):
    problemas = db.query(models.Problema).all()
    problemas_dict = [{"id": p.id, "descricao": p.descricao} for p in problemas]
    with open("problemas_exportados.json", "w") as f:
        json.dump(problemas_dict, f)
    return {"message": "Dados exportados para problemas_exportados.json"}

# Rotas para Prontuario
@app.post("/prontuarios/")
def criar_prontuario(prontuario: schemas.ProntuarioCreate, db: Session = Depends(get_db)):
    db_prontuario = models.Prontuario(placa=prontuario.placa, data=prontuario.data, descricao=prontuario.descricao)
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario

# Rota para listar prontuários
@app.get("/prontuarios/", response_model=List[schemas.ProntuarioCreate])
def listar_prontuarios(db: Session = Depends(get_db)):
    return db.query(models.Prontuario).all()

# Rotas para Diagnostico
@app.post("/diagnosticos/")
def criar_diagnostico(diagnostico: schemas.DiagnosticoCreate, db: Session = Depends(get_db)):
    db_diagnostico = models.Diagnostico(problema_id=diagnostico.problema_id, descricao=diagnostico.descricao)
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico

@app.get("/diagnosticos/", response_model=List[schemas.DiagnosticoCreate])
def listar_diagnosticos(db: Session = Depends(get_db)):
    return db.query(models.Diagnostico).all()
