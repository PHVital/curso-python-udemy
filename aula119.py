import os

tarefas = []
desfeitas = []
while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')

    if acao == 'listar':
        print()
        print('TAREFAS:')
        print()
        for tarefa in tarefas:
            print(tarefa)
        print()
    elif acao == 'desfazer':
        if desfeitas is None:
            print()
            print('Nada a desfazer')
            print()
            continue
        desfeitas.append(tarefas.pop())
    elif acao == 'refazer':
        if desfeitas is None:
            print()
            print('Nada a refazer')
            print()
            continue
        tarefas.append(desfeitas.pop())
    elif acao == 'clear':
        os.system('cls')
        continue
    else:
        tarefas.append(acao)
    print()
    print()
    