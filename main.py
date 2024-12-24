import os
import random
from Banco import ContaCorrente        
def limpar():
    os.system("cls")
def menu_principal():
    '''
    Função que exibe o menu principal
    output - aciona o menu de escolher opcoes.
    '''
    limpar()
    print("Opções:")
    print("1. Cadastrar novo usuario.")
    print("2. Entar.")
    print("3. Sair")
    escolher_opção_externa()
def voltar_ao_menu():
    '''
    Tem funcao retornar ao menu principal
    output - aciona o menu de voltar ao menu
    '''
    input('Aperte ENTER parar voltar ao menu')
    main()
def opção_invalida():
    '''
    Função que retorna ao usuario que a opcao dele é invalida
    output - aciona o menu de voltar ao menu
    '''
    print("Opção inválida! Tente novamente.")
    voltar_ao_menu()
def criar_conta():
    '''
    Função que cadastra um novo usuario
    input - nome, senha e saldo
    output - retorna um objeto e exibe o numero da conta que foi criada
    '''
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
    '''
    Função que retorna a opcao escolida pelo usuario
    input - escolha do usuario
    output - direciona para o menu escolhido
    '''
    try:
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            limpar()
            valor = float(input("Digite 0 para cancelar\nDigite o valor que deseja sacar: "))
            if valor == 0:
                menu_interno(conta_corrente1)
            else:
                if conta_corrente1.sacar(valor):
                    print(f"Saque realizado com sucesso! Saldo atual: R${conta_corrente1.saldo:.2f}")
                else:
                    print("Não foi possível realizar o saque.")
        elif escolha == 2:
            limpar()
            valor = float(input("Digite o valor que deseja depositar: "))
            conta_corrente1.depositar(valor)
            print(f"Depósito realizado com sucesso! Saldo atual: R${conta_corrente1.saldo:.2f}")
        elif escolha == 3:
            limpar()
            print(ContaCorrente.exibir_saldo(conta_corrente1))
        elif escolha == 4:
            limpar()
            voltar_ao_menu()
        else:
            menu_interno(conta_corrente1)
    except:
        opção_invalida()
def menu_interno(conta_corrente1):
    '''
    Função que exibe o menu interno
    imput - escolha do menu por parte do usuario
    output - aciona o menu de escolher opcoes internas
    '''
    limpar()
    print(f"Olá, {conta_corrente1._nome}!")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Exibir saldo")
    print("4. Sair")
    escolher_opção_interna(conta_corrente1)
def entrar():
    '''
    Função que permite o usuario entrar na conta
    input - numero da conta e senha
    output - aciona o menu interno se o usuario entrar na conta
    '''
    ################################################################
    # conta teste : 123 senha 123
    conta_corrente1 = ContaCorrente('Weslley','123',1000,123) 
    conta = 123
    senha = '123'
    try:
        # conta = int(input("Digite o numero da conta: "))
        # senha = str(input("Digite a senha: "))
        if conta in ContaCorrente.contas:
            conta_data = ContaCorrente.contas[conta]
            if conta_data["senha"] == senha:         
                menu_interno(conta_corrente1)
                cont = 1
                while cont > 0:
                    enter = input("Digite qualquer tecla e aperte enter para sair...")
                    menu_interno(conta_corrente1)
        voltar_ao_menu()
    except:
        print("\nErro: Certifique-se de colocar os dados corretamente")
        voltar_ao_menu()
def escolher_opção_externa():
    '''
    Função que retorna a opcao escolida pelo usuario
    input - escolha do usuario
    output - direciona para o menu escolhido
    '''
    try:
        escolha = int(input("Digite a opção desejada:"))
        if escolha == 1:
            criar_conta()
        elif escolha == 2:
            entrar()
        elif escolha == 3:
            limpar()
            print('Sessão finalizada')
            pass
        else:
            opção_invalida()
    except:
           opção_invalida()
def main():
    menu_principal()
if __name__ == '__main__':
    main()