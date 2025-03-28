hora = int(input("Que horas são agora? "))
if hora < 12:
    print("Bom dia!")
elif hora > 11 and hora < 18:
    print("Bom tarde!")
else:
    print("Boa noite!")