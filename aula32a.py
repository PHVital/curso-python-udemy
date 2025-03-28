numero = input("Digite um número inteiro: ")
if numero.isdigit():
    numero = int(numero)
    print("O número é Par" if numero % 2 == 0 else "O número é Impar")
else:
    print("Número não é inteiro")