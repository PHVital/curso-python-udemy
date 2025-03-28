import os

lista = []

while True:
    opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system("cls")
        item = input("Valor: ")
        lista.append(item)
    elif opcao == 'a':
        indice_apagar = input("Escolha o índice para apagar: ")
        if not indice_apagar.isdigit():
            print("Valor inválido")
            continue
        indice_apagar = int(indice_apagar)
        if indice_apagar > len(lista) - 1 or indice_apagar < 0:
            print("Não possível apagar esse índice")
            continue
        lista.pop(indice_apagar)
        os.system("cls")
    elif opcao == 'l':
        os.system("cls")
        for indice, nome in enumerate(lista):
            print(indice, nome)
    else:
        print("Digite um valor válido!")