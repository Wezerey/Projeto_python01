import os
import random
from Banco import ContaCorrente        
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
    print(f"Conta criada com sucesso!\nNumero da conta: {conta_corrente._conta}\nSaldo da conta: {conta_corrente._saldo}")
    voltar_ao_menu()
    
    
    
def escolher_opção():
    try:
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            criar_conta()
        elif escolha == 2:
            print("entrar")
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