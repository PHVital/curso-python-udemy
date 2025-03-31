perguntas = [{
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4'
}, 
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25'
}, 
{
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5'
}]

acertos = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}")
    print()
    print(f"Opções:")
    for indice, value in enumerate(pergunta['Opções']):
        print(f"{indice}) {value}")
    resposta = input("Escolha uma opção: ")
    print()
    try:
        resposta = int(resposta)
        if pergunta['Opções'][resposta] == pergunta['Resposta']:
            print("Acertou")
            acertos +=1
        else:
            print("Errou")
    except:
        print("Errou")
    print()
print(f"Você acertou {acertos} de 3 perguntas")