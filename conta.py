
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

    def __verifica_saque(self, valor_saque):
        valor_limnite = self.__saldo + self.__limite
        return valor_saque <= valor_limnite
    def saque(self, valor):
        if(self.__verifica_saque(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite.')

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {f'BB: {"001"}, Caixa: {"104"}, Bradesco: {"237"}'}