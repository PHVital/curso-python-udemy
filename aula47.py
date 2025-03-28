tentativas = 0
palavra = "roteador"
letrasAcertadas = ""

while True:
    letra = input("Digite uma letra: ")
    tentativas += 1
    
    if len(letra) > 1: continue
    
    if letra in palavra:
        letrasAcertadas += letra

    palavraFormada = ""
    for x in palavra:
        if x in letrasAcertadas:
            palavraFormada += x
        else:
            palavraFormada += "*"
    print(palavraFormada)
    
    if palavraFormada == palavra:
        break

print(f"O número de tentativas foi {tentativas}")