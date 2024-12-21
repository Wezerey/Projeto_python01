import os
import random
from Banco import ContaCorrente        
conta_valida = {}
def limpar():
    os.system("cls")
def listar_opcoes():
    print("\nOpções:")
    print("1. Cadastrar novo usuario.")
    print("2. Entar.")
    print("3. Sair")
    escolher_opção()
def voltar_ao_menu():
    input('Aperte ENTER parar voltar ao menu')
    main()
def opção_invalida():
    print("Opção inválida! Tente novamente.")
    voltar_ao_menu()
def criar_conta():
    try:
        nome = str(input("Digite seu nome: "))
        if not nome.strip():
            raise ValueError("O nome esta vazio") 
        senha = str(input("Digite sua senha: "))
        saldo = float(input("Digite o saldo inicial: "))
        print("\nCadastro realizado com sucesso!")
        print(f"Nome: {nome}")
        print(f"Saldo inicial: R${saldo:.2f}")
    except ValueError:
        limpar()
        print("\nErro: Certifique-se de colocar os dados corretamente")
        criar_conta()
    conta = random.randint(1000,9999)
    conta_corrente = ContaCorrente(nome, senha, saldo, conta)
    limpar()
    print(f"Conta criada com sucesso!\nNumero da conta: {conta_corrente._conta}\nSaldo da conta: {conta_corrente.saldo}")
    voltar_ao_menu()
def escolher_opção_interna(conta_corrente1):
    try:
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            valor = float(input("Digite o valor que deseja sacar: "))
            if conta_corrente1.sacar(valor):
                print(f"Saque realizado com sucesso! Saldo atual: R${conta_corrente1.saldo:.2f}")
            else:
                print("Não foi possível realizar o saque.")
        elif escolha == 2:
            valor = float(input("Digite o valor que deseja depositar: "))
            conta_corrente1.depositar(valor)
            print(f"Depósito realizado com sucesso! Saldo atual: R${conta_corrente1.saldo:.2f}")
        elif escolha == 3:
            print(ContaCorrente.exibir_saldo(conta_corrente1))
        elif escolha == 4:
            voltar_ao_menu()
        else:
            menu_interno(conta_corrente1)
    except:
        opção_invalida()
def menu_interno(conta_corrente1):
    limpar()
    print("""
           
██████╗░███████╗███╗░░░███╗  ██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░
██╔══██╗██╔════╝████╗░████║  ██║░░░██║██║████╗░██║██╔══██╗██╔══██╗
██████╦╝█████╗░░██╔████╔██║  ╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║
██╔══██╗██╔══╝░░██║╚██╔╝██║  ░╚████╔╝░██║██║╚████║██║░░██║██║░░██║
██████╦╝███████╗██║░╚═╝░██║  ░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░
""")
    print(f"Olá, {conta_corrente1._nome}!")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Exibir saldo")
    print("4. Sair")
    escolher_opção_interna(conta_corrente1)
def entrar():
    conta_corrente1 = ContaCorrente('Weslley','123',1000,123)
    try:
        
        # conta = int(input("Digite o numero da conta: "))
        # senha = str(input("Digite a senha: "))
        conta = 123
        senha = '123'
        if conta in ContaCorrente.contas:
            conta_data = ContaCorrente.contas[conta]
            if conta_data["senha"] == senha:
                conta_valida = conta_data           
                menu_interno(conta_corrente1)
        voltar_ao_menu()
    except:
        print("\nErro: Certifique-se de colocar os dados corretamente")
        voltar_ao_menu()
def escolher_opção():
    try:
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            criar_conta()
        elif escolha == 2:
            entrar()
        elif escolha == 3:
            print("sair")
        else:
            opção_invalida()
    except:
           opção_invalida()
def main():
    listar_opcoes()
if __name__ == '__main__':
    main()