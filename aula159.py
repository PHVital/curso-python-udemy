from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Pedro', 'Henrique')
    p1.nome_completo = 'João da Silva Pereira'
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'X'), Pessoa('C', 'Z')]
    ordenado = sorted(lista, reverse=True, key=lambda p: p.nome)
    print(p1)
    print(p1.nome_completo)
    print(ordenado)