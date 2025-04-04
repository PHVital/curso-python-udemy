import json
from aula127_a import Pessoa

with open('aula127.json', 'r') as file:
    pessoas = json.load(file)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])


print(p1.nome)
print(p2.nome)
print(p3.nome)