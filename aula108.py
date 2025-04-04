# def soma_listas(l1, l2):
#     intervalo = min(l1, l2)
#     return [
#         l1[i] + l2[i]
#         for i in range(len(intervalo))
#     ]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 40]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)
# print(soma_listas(lista_a, lista_b))