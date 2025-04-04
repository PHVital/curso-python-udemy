import json

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Joao', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [vars(p1), vars(p2), vars(p3)]

with open('aula127.json', 'w') as file:
    json.dump(bd, file, indent=2)