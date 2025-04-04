path = "aula116.txt"

# arquivo = open(path, 'w')
# arquivo.close()

with open(path, 'w') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.seek(0,0)

with open(path, 'r') as arquivo:
    print(arquivo.read())