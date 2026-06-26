from lib.interface import *

def pessoascadastradas(arquivo):
    with open(arquivo, "rt") as pessoascadastradas:
                    
        cabecalho("PESSOAS CADASTRADAS")
        
        print(pessoascadastradas.read())
        print(f"{linha()}\n")
        
def cadastrarpessoas(arquivo):
    with open(arquivo, "a") as pessoascadastradas:
                    
        cabecalho("CADASTRO DE PESSOAS")
        nome = str(input("Digite o nome do cadastrado: "))
        idade = str(input("Digite a idade do cadastrado: "))
        
        try:
            pessoascadastradas.writelines(f"\n{nome:<25} {idade:>3} anos")
            print(f"\033[33m{nome} foi adicionado com sucesso.\033[m")
        except Exception as e:
            print(f"\033[31mERRO: {e}.\n\033[m O cadastro não foi feito com com sucesso")
        
        print(f"{linha()}\n")