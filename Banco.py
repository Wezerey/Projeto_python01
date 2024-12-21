import random

class ContaCorrente():
    contas = {}
    def __init__(self, nome,senha, saldo, conta):
        self._nome = nome
        self._senha = senha
        self._conta = conta
        self.saldo = saldo
        ContaCorrente.contas[self._conta] = {
            "nome": self._nome,
            "senha": self._senha,
            "saldo": self.saldo
        }
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def depositar(self, valor):
        self.saldo += valor
    @classmethod
    def listar_contas(cls):
        return cls.contas
    
    def exibir_saldo(self):
        return f'Seu saldo atual: {self.saldo:.2f}'


