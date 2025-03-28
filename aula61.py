import random

# cpf = "746.824.890-70".replace('.', '').replace('-', '')
cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

cont = 10
soma = 0

for n in cpf:
    soma += int(n) * cont
    cont -= 1

digito1 = (soma * 10) % 11

digito1 = digito1 if digito1 <= 9 else 0

numeros = cpf + str(digito1)

soma2 = 0
cont = 11
for n in numeros:
    soma2 += int(n) * cont
    cont -= 1

digito2 = (soma2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_gerado = f'{numeros}{digito2}'

# if cpf == cpf_gerado:
#     print("Valido")
# else:
#     print("Invalido")

print(cpf_gerado)
