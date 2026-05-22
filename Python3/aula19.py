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
def desafio91():
    jogadores = [
    {"jogador": "jogador1", "dado": 0},
    {"jogador": "jogador2", "dado": 0},
    {"jogador": "jogador3", "dado": 0},
    {"jogador": "jogador4", "dado": 0}
]

    print("Valores sorteados:")

    for d in range(4):
        jogadores[d]["dado"] = randint(1,6)
        print(F"O {jogadores[d]["jogador"]} tirou {jogadores[d]["dado"]}")

    print('Os jogadores com maiores valores tirados foram:')
    
    print(jogadores)
    print(jogadores[1]["dado"])
    
desafio91()