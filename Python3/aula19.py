# Dict

def desafio90():
    aluno = dict()

    aluno["nome"] = str(input("Digite o nome do aluno: "))
    aluno["media"] = float(input("Digite a média do aluno: "))
    
    print("=-=-"*10)

    if aluno["media"] >= 7:
        print(f"{aluno["nome"]} foi aprovado com uma média de {aluno["media"]}!")
    else:
        print(f"{aluno["nome"]} foi reprovado com uma média de {aluno["media"]}!")

from random import randint
from operator import itemgetter
from time import sleep
def desafio91():
    jogadores = {
        "Jogador 01": randint(1,6),
        "Jogador 02": randint(1,6),
        "Jogador 03": randint(1,6),
        "Jogador 04": randint(1,6)
}

    print("Valores sorteados:")
    for k, v in jogadores.items():
        print(f"O {k} tirou o número {v}!")
        
    print()
    
    print('Os jogadores com maiores valores tirados foram:')
    cont = 1
    for k, v in sorted(jogadores.items(), key=itemgetter(1)):
        sleep(1)
        print(f"{cont}° Lugar: {k} com o dado valendo {v}")
        cont += 1
    
desafio91()