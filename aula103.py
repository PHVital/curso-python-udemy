def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O resultado foi {resultado}')
        print("Ok, agora você foi decorada")
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma str")
    

inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro(123)
print(invertida)