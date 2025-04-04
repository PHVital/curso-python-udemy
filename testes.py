import json

tarefas = []

with open('teste.json', 'r') as file:
    tarefas = json.load(file)

print(tarefas)