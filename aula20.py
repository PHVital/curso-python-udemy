primeiro = int(input("Digite um valor: "))
segundo = int(input("Digite outro valor: "))

if primeiro > segundo:
    print(f"O primeiro valor {primeiro} é maior que o segundo {segundo}")
elif primeiro < segundo:
    print(f"O segundo valor {segundo} é maior que o primeiro {primeiro}")
else:
    print(f"O primeiro valor {primeiro} é igual ao segundo {segundo}")