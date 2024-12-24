import random

class ContaCorrente():
    contas = {}
    def __init__(self, nome,senha, saldo, conta,cheque=600):
        self._nome = nome
        self._senha = senha
        self._conta = conta
        self.saldo = saldo
        self.cheque = cheque
        ContaCorrente.contas[self._conta] = {
            "nome": self._nome,
            "senha": self._senha,
            "saldo": self.saldo
        }
    def sacar(self, valor):
        if self.saldo - valor >= -self.cheque:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def depositar(self, valor):
        if self.cheque < 0: 
            self.cheque += valor
            if self.cheque > 0:
                self.saldo += self.cheque
                self.cheque = 0
        self.saldo += valor
        return self.cheque
    def exibir_saldo(self):
        cheque_disponivel = max(0, self.cheque + self.saldo)
        if self.saldo > 0:
            return (
                f'Seu saldo atual: R$ {self.saldo:.2f}\n'
                f'Seu limite de cheque especial disponível: R$ {self.cheque:.2f}'
            )
        else:
            return (
                f'Seu saldo atual: R$ {self.saldo:.2f}\n'
                f'Seu limite de cheque especial disponível: R$ {cheque_disponivel:.2f}'
            )