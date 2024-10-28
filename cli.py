import requests

# URL base da API
BASE_URL = "http://127.0.0.1:8000"

def exibir_menu():
    # Menu inicial
    while True:
        print("\nBem vindo ao sistema de auto atendimento Porto!")
        print("1. Menu Mecânico Porto")
        print("2. Menu Segurado Porto")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_mecanico()
        elif opcao == "2":
            menu_segurado()
        elif opcao == "3":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_mecanico():
    while True:
        print("\nMenu Mecânico Porto")
        print("1. Visualizar prontuários")
        print("2. Adicionar prontuário")
        print("3. Alterar prontuário")
        print("4. Excluir prontuário")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_prontuarios()
        elif opcao == "2":
            adicionar_prontuario()
        elif opcao == "3":
            alterar_prontuario()
        elif opcao == "4":
            excluir_prontuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_segurado():
    while True:
        print("\nMenu Segurado Porto")
        print("1. Registrar problema")
        print("2. Alterar problema")
        print("3. Excluir problema")
        print("4. Visualizar problemas")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_problema()
        elif opcao == "2":
            alterar_problema()
        elif opcao == "3":
            excluir_problema()
        elif opcao == "4":
            listar_problemas()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Funções de interação com a API
def listar_problemas():
    response = requests.get(f"{BASE_URL}/problemas/")
    if response.status_code == 200:
        problemas = response.json()
        print("\nProblemas registrados:")
        for p in problemas:
            print(f"- ID: {p['id']}, Descrição: {p['descricao']}")
    else:
        print("Erro ao listar problemas.")

def registrar_problema():
    descricao = input("Descreva o problema: ")
    response = requests.post(f"{BASE_URL}/problemas/", json={"descricao": descricao})
    if response.status_code == 200:
        print("Problema registrado com sucesso.")
    else:
        print(f"Erro ao registrar o problema. Código: {response.status_code}, Erro: {response.text}")

def alterar_problema():
    problema_id = int(input("ID do problema a alterar: "))
    descricao = input("Nova descrição: ")
    response = requests.put(f"{BASE_URL}/problemas/{problema_id}", json={"descricao": descricao})
    if response.status_code == 200:
        print("Problema atualizado com sucesso.")
    else:
        print("Erro ao atualizar o problema.")

def excluir_problema():
    problema_id = int(input("ID do problema a excluir: "))
    response = requests.delete(f"{BASE_URL}/problemas/{problema_id}")
    if response.status_code == 200:
        print("Problema excluído com sucesso.")
    else:
        print("Erro ao excluir o problema.")

def listar_problemas():
    response = requests.get(f"{BASE_URL}/problemas/")
    if response.status_code == 200:
        problemas = response.json()
        print("Dados recebidos da API:", problemas)  # Exibe o conteúdo completo para depuração
        print("\nProblemas registrados:")
        for p in problemas:
            print(f"Descrição: {p['descricao']}")
    else:
        print("Erro ao listar problemas.")

def adicionar_prontuario():
    placa = input("Placa do carro: ")
    data = input("Data da reforma (yyyy-mm-dd): ")
    descricao = input("Descrição da reforma: ")
    response = requests.post(f"{BASE_URL}/prontuarios/", json={"placa": placa, "data": data, "descricao": descricao})
    if response.status_code == 200:
        print("Prontuário adicionado com sucesso.")
    else:
        print("Erro ao adicionar prontuário.")

def alterar_prontuario():
    prontuario_id = int(input("ID do prontuário a alterar: "))
    descricao = input("Nova descrição: ")
    data = input("Nova data (yyyy-mm-dd): ")
    response = requests.put(f"{BASE_URL}/prontuarios/{prontuario_id}", json={"descricao": descricao, "data": data})
    if response.status_code == 200:
        print("Prontuário atualizado com sucesso.")
    else:
        print("Erro ao atualizar prontuário.")

def excluir_prontuario():
    prontuario_id = int(input("ID do prontuário a excluir: "))
    response = requests.delete(f"{BASE_URL}/prontuarios/{prontuario_id}")
    if response.status_code == 200:
        print("Prontuário excluído com sucesso.")
    else:
        print("Erro ao excluir prontuário.")

if __name__ == "__main__":
    exibir_menu()
