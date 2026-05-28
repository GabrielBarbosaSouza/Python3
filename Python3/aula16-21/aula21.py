import datetime

def escreva(texto):
    tamanho = len(texto)
    print("~" * tamanho)
    print(texto.center(tamanho))
    print("~" * tamanho)

def desafio101():
    def voto():
        ano = int(input("Em que ano você nasceu?: "))
        
        idade = datetime.date.today().year - ano
        
        if 60 > idade >= 18:
            print(f"\nVocê DEVE votar.\nVocê tem {idade} anos!")
        elif idade >= 60:
            print(f"\nVocê ESCOLHE votar.\nVocê tem {idade} anos!")
        else:
            print(f"\nVocê NÃO pode votar.\nVocê tem {idade} anos!")
        
    voto()
    
def desafio102():
    def fatorial(n, show=False):
        """Calcula o fatorial d eum número\n
        :param n: O número a ser calculádo\n
        :param show: Mostrar a conta (opcional)\n
        :return: O valor do fatorial de n"""
        
        escreva("Calculador de Fatorial")
        f = 1
        for cont in range(n, 0, -1):
            f*=cont
            
        if show == False: 
            print(f)
            print()
        else:
            cont = 0
            while cont != 5:
                if cont == 4:
                    print(n-cont, end=" = ")
                    print(f)
                    print()
                else:
                    print(n-cont, end=" x ")
                cont += 1
     
    fatorial(5)           
    fatorial(5, True)

def desafio103():
    def ficha(nome="<desconhecido>", gols=0):
        print(f"O jogador {nome} marcou {gols} gols")
    
    n = input("Digite o nome do jogador: ")
    g = input("Digite a quantidade de gols: ")
    if g.isnumeric():
        g = int(g)
    else:
        g = 0

    if n.strip() == "":
        ficha(gols=g)
    else:
        ficha(n, g)
    
desafio103()

def desafio104():
    def leiaint(texto):
        global n
        while True:
            input(texto)
            if texto != int:
                print("ERRO! Digite um número inteiro.")
            else:
                break
        
    
    n = leiaint("Digite um número: ")
    print(f"Você digitou o número {n}")
# desafio104()