import pprint

def p(v):
    pprint.pprint(v)

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

p(lista)
print(lista)