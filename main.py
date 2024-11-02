from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Cliente, Veiculo, Diagnostico, Prontuario
from schemas import ClienteCreate, VeiculoCreate, DiagnosticoCreate, ProntuarioCreate
import json
import requests

# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///./test.db"

# Criação do engine e da sessão para o banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas
Base.metadata.create_all(bind=engine)

# Inicialização do FastAPI
app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas CRUD para Cliente
@app.post("/clientes/", response_model=ClienteCreate)
def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente  # Retorna o objeto completo, incluindo id_cliente

@app.get("/clientes/", response_model=list[ClienteCreate])
def listar_clientes_http(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

# Rotas CRUD para Veículo
@app.post("/veiculos/", response_model=VeiculoCreate)
def create_veiculo(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    db_veiculo = Veiculo(**veiculo.dict())
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo  # Retorna o objeto completo, incluindo id_veiculo

@app.get("/veiculos/", response_model=list[VeiculoCreate])
def listar_veiculos_http(db: Session = Depends(get_db)):
    return db.query(Veiculo).all()

# Rotas CRUD para Diagnóstico
@app.post("/diagnosticos/", response_model=DiagnosticoCreate)
def create_diagnostico(diagnostico: DiagnosticoCreate, db: Session = Depends(get_db)):
    db_diagnostico = Diagnostico(**diagnostico.dict())
    db.add(db_diagnostico)
    db.commit()
    db.refresh(db_diagnostico)
    return db_diagnostico  # Retorna o objeto completo, incluindo id_diagnostico

@app.get("/diagnosticos/", response_model=list[DiagnosticoCreate])
def listar_diagnosticos_http(db: Session = Depends(get_db)):
    return db.query(Diagnostico).all()

# Rotas CRUD para Prontuário
@app.post("/prontuarios/", response_model=ProntuarioCreate)
def create_prontuario(prontuario: ProntuarioCreate, db: Session = Depends(get_db)):
    db_prontuario = Prontuario(**prontuario.dict())
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario  # Retorna o objeto completo, incluindo id_prontuario

@app.get("/prontuarios/", response_model=list[ProntuarioCreate])
def listar_prontuarios_http(db: Session = Depends(get_db)):
    return db.query(Prontuario).all()

# Funções de interação com o menu e a API
BASE_URL = "http://127.0.0.1:8000"

# Funções para o menu Cliente
def listar_clientes():
    response = requests.get(f"{BASE_URL}/clientes/")
    if response.status_code == 200:
        clientes = response.json()
        print("\nClientes registrados:")
        for cliente in clientes:
            print(f"- ID: {cliente['id_cliente']}, Nome: {cliente['nome_cliente']}")
    else:
        print("Erro ao listar clientes.")

def registrar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    telefone = input("Telefone do cliente: ")
    endereco = input("Endereço do cliente: ")
    response = requests.post(f"{BASE_URL}/clientes/", json={
        "nome_cliente": nome,
        "email_cliente": email,
        "telefone_cliente": telefone,
        "endereco_cliente": endereco
    })
    if response.status_code == 200:
        cliente = response.json()
        print(f"Cliente registrado com sucesso. ID do cliente: {cliente.get('id_cliente')}")
    else:
        print("Erro ao registrar cliente.")

# Funções para o menu Veículo
def listar_veiculos():
    response = requests.get(f"{BASE_URL}/veiculos/")
    if response.status_code == 200:
        veiculos = response.json()
        print("\nVeículos registrados:")
        for veiculo in veiculos:
            print(f"- ID: {veiculo['id_veiculo']}, Placa: {veiculo['placa']}, Modelo: {veiculo['modelo']}")
    else:
        print("Erro ao listar veículos.")

def registrar_veiculo():
    listar_clientes()  # Exibe os clientes e seus IDs para referência
    id_cliente = int(input("ID do cliente: "))
    placa = input("Placa do veículo: ")
    modelo = input("Modelo do veículo: ")
    ano = int(input("Ano do veículo: "))
    response = requests.post(f"{BASE_URL}/veiculos/", json={
        "id_cliente": id_cliente,
        "placa": placa,
        "modelo": modelo,
        "ano": ano
    })
    if response.status_code == 200:
        veiculo = response.json()
        print(f"Veículo registrado com sucesso. ID do veículo: {veiculo.get('id_veiculo')}")
    else:
        print("Erro ao registrar veículo.")

# Funções para o menu Diagnóstico
def listar_diagnosticos():
    response = requests.get(f"{BASE_URL}/diagnosticos/")
    if response.status_code == 200:
        diagnosticos = response.json()
        print("\nDiagnósticos registrados:")
        for diag in diagnosticos:
            print(f"- ID: {diag['id_diagnostico']}, Descrição: {diag['descricao']}")
    else:
        print("Erro ao listar diagnósticos.")

def registrar_diagnostico():
    listar_veiculos()  # Exibe os veículos e seus IDs para referência
    id_veiculo = int(input("ID do veículo: "))
    descricao = input("Descreva o diagnóstico: ")
    response = requests.post(f"{BASE_URL}/diagnosticos/", json={
        "descricao": descricao,
        "id_veiculo": id_veiculo
    })
    if response.status_code == 200:
        diagnostico = response.json()
        print(f"Diagnóstico registrado com sucesso. ID do diagnóstico: {diagnostico.get('id_diagnostico')}")
    else:
        print("Erro ao registrar diagnóstico.")

# Funções para o menu Prontuário
def listar_prontuarios():
    response = requests.get(f"{BASE_URL}/prontuarios/")
    if response.status_code == 200:
        prontuarios = response.json()
        print("\nProntuários registrados:")
        for prontuario in prontuarios:
            print(f"- ID: {prontuario['id_prontuario']}, Descrição: {prontuario['descricao_conserto']}")
    else:
        print("Erro ao listar prontuários.")

def registrar_prontuario():
    listar_clientes()  # Exibe os clientes e seus IDs para referência
    listar_veiculos()  # Exibe os veículos e seus IDs para referência
    id_cliente = int(input("ID do cliente: "))
    id_veiculo = int(input("ID do veículo: "))
    descricao = input("Descrição do conserto: ")
    data_conserto = input("Data do conserto (YYYY-MM-DD): ")
    response = requests.post(f"{BASE_URL}/prontuarios/", json={
        "descricao_conserto": descricao,
        "data_conserto": data_conserto,
        "id_cliente": id_cliente,
        "id_veiculo": id_veiculo
    })
    if response.status_code == 200:
        prontuario = response.json()
        print(f"Prontuário registrado com sucesso. ID do prontuário: {prontuario.get('id_prontuario')}")
    else:
        print("Erro ao registrar prontuário.")

# Menu principal e menus específicos
def exibir_menu():
    while True:
        print("\nBem-vindo ao sistema de auto atendimento Porto!")
        print("1. Menu Cliente")
        print("2. Menu Veículo")
        print("3. Menu Diagnóstico")
        print("4. Menu Prontuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            menu_veiculo()
        elif opcao == "3":
            menu_diagnostico()
        elif opcao == "4":
            menu_prontuario()
        elif opcao == "5":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente():
    while True:
        print("\nMenu Cliente")
        print("1. Visualizar clientes")
        print("2. Registrar cliente")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            registrar_cliente()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_veiculo():
    while True:
        print("\nMenu Veículo")
        print("1. Visualizar veículos")
        print("2. Registrar veículo")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_veiculos()
        elif opcao == "2":
            registrar_veiculo()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_diagnostico():
    while True:
        print("\nMenu Diagnóstico")
        print("1. Visualizar diagnósticos")
        print("2. Registrar diagnóstico")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_diagnosticos()
        elif opcao == "2":
            registrar_diagnostico()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_prontuario():
    while True:
        print("\nMenu Prontuário")
        print("1. Visualizar prontuários")
        print("2. Registrar prontuário")
        print("3. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_prontuarios()
        elif opcao == "2":
            registrar_prontuario()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
if __name__ == "__main__":
    exibir_menu()
