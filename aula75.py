# def duplica(n):
#     return n*2

# def triplica(n):
#     return n*3

# def quadruplica(n):
#     return n*4

def criar_multiplicador(m):
    def multiplicar(n):
        return n * m
    return multiplicar

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadruplica = criar_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))