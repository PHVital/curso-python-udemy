class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motorV8 = Motor('V8')
fusca.fabricante = volkswagen
fusca.motor = motorV8
print(fusca.fabricante.nome, fusca.nome, fusca.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
motorV8 = Motor('V8')
fiat_uno.fabricante = fiat
fiat_uno.motor = motorV8
print(fiat_uno.fabricante.nome, fiat_uno.nome, fiat_uno.motor.nome)

fit = Carro('Fit')
honda = Fabricante('Honda')
motor_1_6 = Motor('1.6')
fit.fabricante = honda
fit.motor = motor_1_6
print(fit.fabricante.nome, fit.nome, fit.motor.nome)