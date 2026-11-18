
lista_tarefas = []
lista_tarefas_concluidas = []

class Tarefa:
    id = None
    descricao = None
    prioridade = None ## 1- Alta 2 - Media 3 - Baixa
    situacao = None

def carregar_tarefas_teste():
    t1 = Tarefa()
    t1.id = 1
    t1.descricao = "Estudar estruturas de dados em Python"
    t1.prioridade = "1"
    t1.situacao = "Pendente"

    t2 = Tarefa()
    t2.id = 2
    t2.descricao = "Comprar café para o escritório"
    t2.prioridade = "3"
    t2.situacao = "Pendente"

    t3 = Tarefa()
    t3.id = 3
    t3.descricao = "Refatorar função de cadastro de tarefas"
    t3.prioridade = "2"
    t3.situacao = "Concluída"

    lista_tarefas.extend([t1, t2, t3])

def nova_tarefa():
    print("*" * 40)
    print("Cadastro de nova tarefa\n")

    tarefa = Tarefa()
    tarefa.id = len(lista_tarefas) + 1
    tarefa.descricao = input("Informe a descrição da tarefa: ")
    tarefa.prioridade = input("Informe o valor de prioridade (1, 2, 3): ")
    tarefa.situacao = True
    
    lista_tarefas.append(tarefa)

    print("\nTarefa adicionada com sucesso!\n")

def visualizar_tarefa():
    print("*" * 40)
    print("Tarefas Cadastradas\n")

    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for tarefa in lista_tarefas:
        print(f"ID: {tarefa.id:<5} | Descrição: {tarefa.descricao:<50} | Prioridade: {tarefa.situacao}")
    
    print(" ")
        
def  concluir_tarefa():
    print("*" * 40)
    print("Concluir Tarefas\n")

    tarefa_concluida = int(input("Informe o ID da tarefa que deseja concluir: "))
    encontrada = False

    for tarefa in lista_tarefas:
        if tarefa.id == tarefa_concluida:
            print(f"Tarefa com ID {tarefa.id} alterada para concluída com sucesso!\n")
            tarefa.situacao = False
            encontrada = True
            lista_tarefas_concluidas.append(tarefa)
            break

    if not encontrada:
        print("ID de tarefa inexistente!\n")

def reabrir_tarefa():
    print("*" * 40)
    print("Concluir Tarefas\n")

    tarefa = int(input("Informe o ID da tarefa que deseja reabrir: "))
    encontrada = False

    for tarefa in lista_tarefas_concluidas:
        if tarefa.id == tarefa:
            print(f"Tarefa com ID {tarefa.id} alterada para reaberta com sucesso!\n")
            tarefa.situacao = False
            encontrada = True
            lista_tarefas.append(tarefa)
            break

    if not encontrada:
        print("ID de tarefa inexistente!\n")


def editar_tarefa():
    print("*" * 40)
    print("Editar Tarefas\n")

    tarefa = int(input("Informe o ID da tarefa que deseja editar: "))
    encontrada = False

    for tarefa in lista_tarefas:
        if tarefa.id == tarefa:
            print(f"ID: {tarefa.id:<5} | Descrição: {tarefa.descricao:<50} | Prioridade: {tarefa.situacao}")
            descrição_nova = print(f"\nDescrição nova (0 para manter como está): \n")

            if descrição_nova != '0':
                tarefa.descricao = descrição_nova

            prioridade_nova = print(f"\nPrioridade nova (0 para manter como está): \n")

            if prioridade_nova != '0':
                tarefa.prioridade = prioridade_nova

            print(f"Tarefa com ID {tarefa.id} alterada para com sucesso!\n")
            encontrada = True
            break

    if not encontrada:
        print("ID de tarefa inexistente!\n")
    
while True:
    print("*" * 40)
    print("Menu de opções\n")
    print("1 - Nova Tarefa")
    print("2 - Visualizar Tarefas")
    print("3 - Concluir Tarefas")
    print("4 - Reabrir Tarefa")
    print("6 - Editar Tarefa")
    print("0 - SAIR\n")
    
    resposta = int(input("Escolha a opção que deseja visualizar: "))

    match resposta:
        case 1:
            nova_tarefa()
        case 2:
            visualizar_tarefa()
        case 3:
            concluir_tarefa()
        case 4:
            reabrir_tarefa()
        case 5:
            editar_tarefa()
        case 0:
            print("Saindo do programa...")
            break

