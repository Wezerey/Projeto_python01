import random

class ContaCorrente():
    conta = []
    def __init__(self, nome,senha, saldo, conta):
        self._nome = nome
        self._senha = senha
        self._conta = conta
        self._saldo = saldo
        ContaCorrente.conta.append(self)

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        else:
            print("Saldo insuficiente!")
            return False
    def depositar(self, valor):
        self._saldo += valor
    def exibir(self, nome,senha,saldo,conta):
        return f'{nome} {senha}{saldo}{conta}'


