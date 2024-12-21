from Banco import Criar

class ContaCorrente(Criar):
    def __init__(self, nome,senha, saldo, cliente):
        super().__init__(nome,cliente, senha)
        self.saldo = saldo
