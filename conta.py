
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {format(self)}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)