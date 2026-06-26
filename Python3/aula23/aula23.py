import urllib.request
from lib.interface import *
from lib.opcoes import *

# Importar * significa importar tudo q a pasta tem

def desafio113():
    def leiaInt(num):
        while True:
            entrada = input(num)
            try:
                return int(entrada)
            except ValueError:
                print('\033[31mERRO! Digite um número inteiro!\033[m')
        
        
    def leiaFloat(num):
        while True:
            entrada = input(num)
            try:
                return float(entrada)
            except ValueError:
                print('\033[31mERRO! Digite um número real!\033[m')


    i = leiaInt('Digite um número inteiro: ')
    f = leiaFloat('Digite um número real: ')

    print(f'Você digitou {i} e {f}')

def desafio114():
    try:
        urllib.request.urlopen('https://ong-eg.github.io/SmartEco/')
    except Exception as e:
        print(f'Não consegui acessar esse site!\nErro: {e}')
    else:
        print('Consegui acessar esse site!')
        
def desafio115():
    
    lista = ["Ver pessoas cadastradas", "Cadastrar novas pessoas", "Sair do sistema"]
       
    while True:
        menu(lista)
        print("-"*40)
        
        try:
            opcao = int(input("\033[4:mSua opção:\033[m "))
            
            if opcao == 1:
                pessoascadastradas("aula23/lib/opcoes/pessoascadastradas.txt")
            
            elif opcao == 2:
                cadastrarpessoas("aula23/lib/opcoes/pessoascadastradas.txt")
            
            elif opcao == 3:
                cabecalho(lista[2])
                print("Volte sempre!")
                break
                
            else:
                print("\033[31mOpção inválida! Tente novamente.\033[m")
                
            repetir = input("Deseja voltar ao menu? (S/N): ").lower()
            if repetir == "s":
                print()
                continue
            elif repetir == "n":
                break
            else:
                print("\033[31mEscolha uma opção válida.\033[m")
            
        except Exception as e:
            print(f"\033[31mERRO: {e}.\033[m")
                
desafio115()
