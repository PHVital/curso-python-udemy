import os
import json

def listar(tarefas):
    print()
    print('TAREFAS:')
    print()
    for tarefa in tarefas:
        print(tarefa)
    print()


def desfazer(desfeitas, tarefas):
    if not tarefas:
        print()
        print('Nada a desfazer')
        print()
        return
    desfeitas.append(tarefas.pop())
    with open('exercicios\\listaEmJson.json', 'w') as file:
        json.dump(tarefas, file, indent=2)
    print()


def refazer(desfeitas, tarefas):
    if not desfeitas:
        print()
        print('Nada a refazer')
        print()
        return
    tarefas.append(desfeitas.pop())
    with open('exercicios\\listaEmJson.json', 'w') as file:
        json.dump(tarefas, file, indent=2)
    print()


tarefas = []
desfeitas = []


with open('exercicios\\listaEmJson.json', 'r') as file:
    tarefas = json.load(file)


while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')

    if acao == 'listar':
        listar(tarefas)
        continue
    elif acao == 'desfazer':
        desfazer(desfeitas, tarefas)
        continue
    elif acao == 'refazer':
        refazer(desfeitas, tarefas)
        continue
    elif acao == 'clear':
        os.system('cls')
        continue
    else:
        tarefas.append(acao)
    print()
    print()
    with open('exercicios\\listaEmJson.json', 'w') as file:
        json.dump(tarefas, file, indent=2)
    