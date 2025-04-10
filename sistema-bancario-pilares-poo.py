from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0):
        self.agencia = agencia
        self.conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositado {valor}, seu saldo agora é {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0, limite=0):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        # Verifica se o valor solicitado não ultrapassa o saldo + limite
        total_disponivel = self.saldo + self.limite
        if valor > total_disponivel:
            return 'Saldo insuficiente'

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            # Quando o saldo for insuficiente, o restante é retirado do limite
            restante = valor - self.saldo
            self.saldo = 0
            self.limite -= restante

        # Garantir que o limite não seja negativo
        if self.limite < 0:
            self.limite = 0

        print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}, Limite restante: {self.limite}")





class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo=0):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        if self.saldo <= 0:
            return 'Saldo insuficiente'
        if valor > self.saldo:
            return 'Saldo insuficiente'
        self.saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}")



class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta

    def sacar(self, valor):
        if not Banco.autenticar(self._conta.agencia, self, self._conta):
            return 'Não é possível sacar'
        return self._conta.sacar(valor)


class Banco:
    _contas = []
    _clientes = []


    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    @classmethod
    def autenticar(cls, agencia, cliente, conta):
        if cliente not in cls._clientes:
            return False
        if conta not in cls._contas:
            return False
        if cliente._conta != conta:
            return False
        if conta.agencia != agencia:
            return False
        return True
    

cp1 = ContaPoupanca(111, 222)
cp1.sacar(1)
cp1.depositar(1)
cp1.sacar(1)
cp1.sacar(1)
print('##')
cc1 = ContaCorrente(111, 222, 0, 100)
cc1.sacar(1)
cc1.depositar(1)
cc1.sacar(1)
cc1.sacar(1)
cc1.sacar(98)
cc1.sacar(1)
print('##')