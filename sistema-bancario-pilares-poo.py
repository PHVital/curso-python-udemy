from abc import ABC, abstractmethod

class Conta(ABC):
    limite_extra = 500

    def __init__(self, agencia, numero_conta, saldo=0):
        self.agencia = agencia
        self.conta = numero_conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        self.saldo -= valor

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        total_disponivel = self.saldo + self.limite_extra
        if valor > total_disponivel:
            return 'Saldo insuficiente'

        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0
            self.limite_extra -= restante

        return f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}"



class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo=0):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor):
        if self.saldo <= 0:
            return 'Saldo insuficiente'
        if valor > self.saldo:
            return 'Saldo insuficiente'
        self.saldo -= valor
        return f"Saque de {valor} realizado com sucesso. Saldo atual: {self.saldo}"



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