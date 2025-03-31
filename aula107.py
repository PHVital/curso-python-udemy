def zipper(l1, l2):
    intervalo_maximo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo_maximo)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

# Existe um comando chamado zip
print(list(zip(l1, l2)))
# Existe um comando chamado zip_longest, para usar precisa importar

from itertools import zip_longest
print(list(zip_longest(l1, l2, fillvalue="Sem Cidade")))