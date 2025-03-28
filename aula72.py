def multiplica(*n):
    multiplicacao = 1
    for i in n:
        multiplicacao *= i
    return multiplicacao


def parImpar(n):
    resultado = n % 2 == 0
    if resultado:
        return f'Par'
    return f"Impar"


print(multiplica(1,2,3,4,5))
print(parImpar(5))

