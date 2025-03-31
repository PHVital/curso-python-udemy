import copy

from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(produtos, key=lambda p: p['nome'], reverse=True)
print()
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(produtos, key=lambda p: p['preco'])
print()
print(*produtos_ordenados_por_preco, sep='\n')

# Meu código

# for i in range(len(produtos)):
#     produtos[i]['preco'] = produtos[i]['preco'] * 1.1
    
# print(*produtos, sep='\n')

# novos_produtos = produtos.copy()
# print()
# print(*novos_produtos, sep='\n')

# print()
# produtos = sorted(produtos, key=lambda item: item['nome'], reverse=True)
# print(*produtos, sep='\n')

# produtos_ordenados_por_nome = produtos.copy()
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

# print()
# produtos = sorted(produtos, key=lambda item: item['preco'])
# print(*produtos, sep='\n')

# produtos_ordenados_por_preco = produtos.copy()
# print()
# print(*produtos_ordenados_por_preco, sep='\n')