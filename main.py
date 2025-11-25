lista = []

executar = True
print("LISTA DE TAREFAS")

while executar:
    print("-------------------------\n"
          "Opções:\n"
          "1- Adicionar Tarefa\n"
          "2- Remover Tarefa\n"
          "3- Visualizar Tarefas\n"
          "4- Sair\n"
          "-------------------------")
    escolha = input("O que deseja fazer? ")
    if escolha == "1":
        print("Adicione a sua tarefa!")
        tarefa = input("Tarefa desejada: ")
        lista.append(tarefa)

    elif escolha == "2":
        print("Remova sua tarefa!\n"
              "-------------------------")
        tarefa = input("Tarefa desejada: ")
        lista.remove(tarefa)

    elif escolha == "3":
        print("Lista de Tarefas Atualizada\n"
              "------------------------")
        for numero, tarefa in enumerate(lista, start=1):
            print(f"{numero}. {tarefa}")

    else:
        print("Lista de Tarefas encerrada!\n"
              "-------------------------")
        executar = False

#Projeto Finalizado!!

