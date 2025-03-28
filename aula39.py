nome = "Pedro Vital"
x = 0
novoNome = ''
while x < len(nome):
    novoNome += '*' + nome[x]
    x += 1

print(novoNome)