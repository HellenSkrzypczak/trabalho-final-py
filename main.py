lista_tarefas = []
lista_tarefas_concluidas = []

class Tarefa:
    def __init__(self, id, descricao, prioridade):
        self.id = id
        self.descricao = descricao
        self.prioridade = prioridade  # 1- Alta, 2 - Média, 3 - Baixa
        self.situacao = True          # True = Ativa, False = Concluída

def nova_tarefa():
    print("*" * 40)
    print("Cadastro de nova tarefa\n")

    proximo_id = len(lista_tarefas) + len(lista_tarefas_concluidas) + 1
    
    descricao = input("Informe a descrição da tarefa: ")
    prioridade = int(input("Informe o valor de prioridade (1 - Alta, 2 - Média, 3 - Baixa): "))
    
    tarefa = Tarefa(proximo_id, descricao, prioridade)
    lista_tarefas.append(tarefa)

    print("\nTarefa adicionada com sucesso!\n")

def visualizar_tarefa():
    print("*" * 40)
    print("Tarefas Cadastradas\n")

    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return
    
    for tarefa in lista_tarefas:
        status = "Ativa" if tarefa.situacao else "Concluída"
        print(f"ID: {tarefa.id:<5} | Descrição: {tarefa.descricao:<20} | Prioridade: {tarefa.prioridade:<5} | Status: {status}")
    
    print("\n")
        
def concluir_tarefa():
    print("*" * 40)
    print("Concluir Tarefas\n")

    tarefa_concluida = int(input("Informe o ID da tarefa que deseja concluir: "))
    encontrada = False

    for tarefa in lista_tarefas:
        if tarefa.id == tarefa_concluida:
            tarefa.situacao = False
            encontrada = True
            
            lista_tarefas_concluidas.append(tarefa)
            lista_tarefas.remove(tarefa)
            print(f"Tarefa com ID {tarefa.id} alterada para concluída com sucesso!\n")
            break

    if not encontrada:
        print("ID de tarefa inexistente!\n")

def reabrir_tarefa():
    print("*" * 40)
    print("Reabrir Tarefa\n")

    tarefa_reabrir = int(input("Informe o ID da tarefa que deseja reabrir: "))
    encontrada = False

    for tarefa in lista_tarefas_concluidas:
        if tarefa.id == tarefa_reabrir:
            tarefa.situacao = True
            encontrada = True
            
            lista_tarefas.append(tarefa)
            lista_tarefas_concluidas.remove(tarefa)
            print(f"Tarefa com ID {tarefa.id} reaberta com sucesso!\n")
            break

    if not encontrada:
        print("ID de tarefa inexistente nas concluídas!\n")

def editar_tarefa():
    print("*" * 40)
    print("Editar Tarefas\n")

    tarefa_editar = int(input("Informe o ID da tarefa que deseja editar: "))
    encontrada = False

    for tarefa in lista_tarefas:
        if tarefa.id == tarefa_editar:
            print(f"ID: {tarefa.id} | Descrição atual: {tarefa.descricao} | Prioridade atual: {tarefa.prioridade}")
            
            descricao_nova = input("\nDescrição nova (aperte Enter ou digite 0 para manter como está): ")
            if descricao_nova and descricao_nova != '0':
                tarefa.descricao = descricao_nova

            prioridade_nova = input("Prioridade nova (aperte Enter ou digite 0 para manter como está): ")
            if prioridade_nova and prioridade_nova != '0':
                tarefa.prioridade = int(prioridade_nova)

            print(f"\nTarefa com ID {tarefa.id} alterada com sucesso!\n")
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
    print("5 - Editar Tarefa")
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
        case _:
            print("Opção inválida!\n")