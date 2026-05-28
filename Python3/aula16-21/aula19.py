# Dict

def desafio90():
    print()
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
    print()
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
    
def desafio92():
    print()
    from datetime import datetime
    dados = dict()
    
    dados["Nome"] = str(input("Nome: "))
    idade = int(input("Ano de Nascimento: "))
    dados["Idade"] = datetime.now().year - idade
    
    dados["Número da Carteira de trabalho"] = int(input("Carteira de Trabalho (0 não tem): "))
    if dados["Número da Carteira de trabalho"] != 0:
        dados["Ano de Contratação"] = int(input("Ano de Contratação: "))
        salario = float(input("Salário: R$"))
        dados["Salario"] = f"{salario:.2f}"
        dados["Aposentadoria"] = dados["Ano de Contratação"] + 35
    else:
        del dados["Número da Carteira de trabalho"]

    print("=-"*20)
    for k, v in dados.items():
        print(f"- {k}: {v}")
    
def escreva(texto):
    tamanho = len(texto)
    print("-" * tamanho)
    print(texto.center(tamanho))
    print("-" * tamanho)
    

def desafio93():
    print()

    dados = dict()

    dados["Nome"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {dados["Nome"]} Jogou? "))

    if partidas != 0:
        dados["Total de Gols"] = 0
        gols_total = list()
        for i in range(partidas):
            gols = int(input(f"Quantos gols na partida {i+1}? "))
            gols_total.append(gols)
            dados["Total de Gols"] += gols
    else:
        print("Erro! Digite um jogador com mais de 0 partidas!.")

    dados["Gols"] = gols_total

    print("=-"*20)
    print(dados)
    print("=-"*20)


    print("=-"*20)
    for k, v in dados.items():
        print(f"{k}: {v}")
    print("=-"*20)

    print("=-"*20)
    print(f"O jogador {dados["Nome"]} jogou {partidas} partidas:")
    for i in range(partidas):
        print(f"     - Na partida {i+1} o jogador fez {dados["Gols"][i]} gols")
    
    print(f"Foi um total de {dados["Total de Gols"]} gols!")

def desafio94():
    pessoa = dict()
    pessoas = list()
    
    while True:
        print()
        pessoa.clear()
        pessoa["Nome"] = input("Nome: ")

        pessoa["Genero"] = input("Gênero (M/F): ").upper()
        if pessoa["Genero"] != "M" and pessoa["Genero"] != "F":
            print("Digite apenas M ou F.")
            pessoa["Genero"] = input("Gênero (M/F): ").upper()

        pessoa["Idade"] = int(input("Idade: "))

        pessoas.append(pessoa.copy())

        continuar = input("Quer continuar? (S/N): ").lower()
        if continuar != "s" and continuar != "n":
            print("Digite apenas S ou N.")
            continuar = input("Quer continuar? (S/N): ").lower()
        elif continuar == "s":
            continue
        else:
            break

    print("=-"*20)
    print(pessoas)
    print("=-"*20)
    
    print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas")
    
    media = list()
    for p in range(len(pessoas)):
        media.append(pessoas[p]["Idade"])
    media = sum(media) / len(media)
    print(f"B) A média de idade é de {media} anos")

    mulheres = list()
    for p in range(len(pessoas)):
        if pessoas[p]["Genero"] == "F":
            mulheres.append(pessoas[p]["Genero"])
        else:
            continue
    print(f"C) As mulheres cadastradas foram {len(mulheres)}")

    acima_idade = list()
    for p in range(len(pessoas)):
        if pessoas[p]["Idade"] > media:
            acima_idade.append(pessoas[p]["Nome"])
    print(f"D) Lista de pessoas que estão acima da média de idade:")
    print(acima_idade)

def desafio95():
    jogador = dict()
    jogadores = list()

    while True:
        print()
        jogador.clear()
        jogador["Nome"] = input("Nome do jogador: ")
        partidas = int(input(f"Quantas partidas {jogador["Nome"]} Jogou? "))

        if partidas != 0:
            jogador["Total de Gols"] = 0
            gols_total = list()
            
            for i in range(partidas):
                gols = int(input(f" Quantos gols na partida {i+1}? "))
                gols_total.append(gols)
                jogador["Total de Gols"] += gols
                       
        else:
            print("Erro! Digite um jogador com mais de 0 partidas!.")
            partidas = int(input(f"Quantas partidas {jogador["Nome"]} Jogou? "))
    
        jogador["Gols"] = gols_total
        jogadores.append(jogador.copy())
                
        continuar = input("Quer continuar? (S/N): ").lower()
        if continuar != "s" and continuar != "n":
            print("Digite apenas S ou N.")
            continuar = input("Quer continuar? (S/N): ").lower()
            
        elif continuar == "s":
            continue
        
        else:
            break
        
    print("=-"*20)
    print(jogadores)