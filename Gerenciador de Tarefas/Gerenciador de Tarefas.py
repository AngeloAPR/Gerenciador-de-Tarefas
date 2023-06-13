import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {'titulo': titulo, 'descricao': descricao, 'completa': False}
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def exibir_tarefas():
    tarefas = carregar_tarefas()
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada.")
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            status = 'Completa' if tarefa['completa'] else 'Incompleta'
            print(f"{indice}. {tarefa['titulo']} - {status}")

def concluir_tarefa():
    tarefas = carregar_tarefas()
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa a ser concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]['completa'] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída com sucesso!")
    else:
        print("Número de tarefa inválido.")

def apagar_tarefa():
    tarefas = carregar_tarefas()
    exibir_tarefas()
    indice = int(input("Digite o número da tarefa a ser apagada: ")) - 1
    if 0 <= indice < len(tarefas):
        del tarefas[indice]
        salvar_tarefas(tarefas)
        print("Tarefa apagada com sucesso!")
    else:
        print("Número de tarefa inválido.")

def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Concluir Tarefa")
        print("4. Apagar Tarefa")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            exibir_tarefas()
        elif opcao == '3':
            concluir_tarefa()
        elif opcao == '4':
            apagar_tarefa()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    menu()
