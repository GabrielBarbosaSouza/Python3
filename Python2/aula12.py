from datetime import date
from InquirerPy import prompt
import random

def desafio36():
    valor = float(input("Qual o valor da casa que você deseja financiar?: "))
    salario = float(input("Qual o seu salário?: "))
    parcela = float(input("Em quantos anos você vai pagar?: "))
    
    prestacao_mensal = valor / parcela
    
    if prestacao_mensal  > salario * 0.30:
        print("Empréstimo negado.")
    else:
        print("Emprestimo aceito.")

def desafio37():
    n = int(input("Escreva um número inteiro para ver ele convertido: "))
    convercao = int(input("""
Para qual base de conversão você deseja converter?
Digite 1 para binário
Digite 2 para octal
Digite 3 para hexadecimal
Resposta: """))
    
    if convercao == 1:
        print(f"Seu número em binário fica: {bin(n)[2:]}")
    elif convercao == 2:
        print(f"Seu número em octal fica: {oct(n)[2:]}")
    elif convercao == 3:
        print(f"Seu número em hexadecimal fica: {hex(n)[2:]}")
    else:
        print("Opção inválida.")

def desafio38():
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))
    
    if n1 > n2:
        print(f"{n1} é maior que {n2}!")
    elif n2 > n1:
        print(f"{n2} é maior que {n1}!")
    else:
        print("Esses números são iguais!")
        
def desafio39():
    idade = input("Escreva a sua data de nascimento (DD/MM/ANO):")
    
    idade = (idade.replace('/', ' ').split())
    ano = int(idade[2])
    ano_atual = date.today().year
    
    if ano_atual - ano < 18:
        print("Você irá poder se alistar em breve!")
        if 18 - (ano_atual - ano) == 1:
            print(f"Falta {18 - (ano_atual - ano)} ano para você se alistar")
        else:
            print(f"Falta {18 - (ano_atual - ano)} anos para você se alistar")
            
    elif ano_atual - ano == 18:
        print(f"Está na hora de você se alistar!")
        
    else:
        print(f"Você já passou da idade de se alistar!")
        print(f"Já passou {(ano_atual - ano) - 18 } anos desde que você poderia se alistar")
    
def desafio40():
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite a sua segunda nota: "))
    
    media = (n1 + n2) / 2
    
    if media < 5:
        print("Você está REPROVADO!")
    elif media < 7:
        print("Você está de RECUPRERAÇÃO!")
    else:
        print("Você está APROVADO!")

def desafio41():
    idade = input("Escreva a sua data de nascimento (DD/MM/ANO):")
    
    idade = (idade.replace('/', ' ').split())
    ano = int(idade[2])
    ano_atual = int(date.today().year)
    
    if ano_atual - ano < 9:
        print("Mirim")
    elif ano_atual - ano < 14:
        print("Infantil")
    elif ano_atual - ano < 20:
        print("Senior")
    else:
        print("Master")

def desafio42():
    reta1 = float(input("Para saber se é possível formar um triangulo, informe um valor para a primeira reta: "))
    reta2 = float(input("Informe um valor para a segunda reta: "))
    reta3 = float(input("Informe um valor para a terceira reta: "))
    
    if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
        print("Um triângulo PODE ser formado com essas retas.")

        if (reta1 == reta2 == reta3):
            print("Esse triangulo é equilátero")
        elif (reta1 == reta2 ) or (reta1 == reta3) or (reta2 == reta3):
            print("Esse triangulo é isóceles")
        else:
         print("Esse triângulo é escaleno")
         
    else:
        print("Um triângulo NÃO pode ser formado com essas retas.")

def desafio43():
    print("-="*16)
    print("Bem vindo a calculadora de IMC!")
    print("-="*16)
    peso = float(input("Informe o peso que você quer calcular (em kg): "))
    altura = input("Informe a altura que você quer calcular (em metros): ")
    
    altura = float(altura.replace(',', '.'))
    
    def imc(peso, altura):
        return float(peso / (altura ** 2))
    
    resultado = imc(peso, altura)
    
    if resultado < 18.5:
        print("Abaixo do Peso") 
    elif resultado < 25:
        print("Peso Ideal") 
    elif resultado < 30:
        print("Sobrepeso") 
    elif resultado < 40:
        print("Obesidade") 
    elif resultado > 40:
        print("Obesidade Mórbida") 
    else:
        print("""
Informe os valores corretos:
Altura em cm
Peso em kg""")
    
    print(f"Seu IMC é {resultado:.2f}")
    
def desafio44():
    opcoes = [
        "À vista (dinheiro/cheque)",
        "À vista no cartão",
        "Em até 2x no cartão",
        "3x ou mais no cartão"
    ]
    
    forma_pagamento = [
        {
            "type": "list",
            "name": "pagamento",
            "message": "Como você deseja pagar por esse produto?: ",
            "choices": opcoes
        },
    ]
    
    valor = float(input("Qual o valor do produto a ser pago?: "))
    cond_pagamento = prompt(forma_pagamento)
    escolha = cond_pagamento["pagamento"]
    
    if escolha == "À vista (dinheiro/cheque)":
        print("Você escolheu pagar à vista e recebeu 10% de desconto!")
        print(f"Valor final: R${valor - (valor * 0.10):.2f}")
        
    elif escolha == "À vista no cartão":
        print("Você escolheu pagar à vista no cartão e recebeu 5% de desconto!")
        print(f"Valor final: R${valor - (valor * 0.05):.2f}")
        
    elif escolha == "Em até 2x no cartão":
        print(f"O preço final do seu produto continua o mesmo. (R${valor:.2f})")
        
    elif escolha == "3x ou mais no cartão":
        print(f"O preço final do seu produto tem 20% de juros. (R${valor * 1.20:.2f})")
    
def desafio45():
    
    opcoes = [
        "Pedra",
        "Papel",
        "Tesoura"
    ]
    
    escolha = [
        {
            "type": "list",
            "name": "escolha_jogador",
            "message": "O que você deseja selecionar?",
            "choices": opcoes
        }
    ]
    
    escolha_jogador = prompt(escolha)
    userChoice = escolha_jogador["escolha_jogador"]
    pcChoice = random.choice(opcoes)
    
    if userChoice == "Pedra" and pcChoice == "Papel":
        print("Você perdeu!")
        print(f"O computador escolheu {pcChoice}.")
    
    elif userChoice == "Papel" and pcChoice == "Tesoura":
        print("Você perdeu!")
        print(f"O computador escolheu {pcChoice}.")
    
    elif userChoice == "Tesoura" and pcChoice == "Pedra":
        print("Você perdeu!")
        print(f"O computador escolheu {pcChoice}.")
        
    elif userChoice == "Papel" and pcChoice == "Pedra":
        print("Você ganhou!")
        print(f"O computador escolheu {pcChoice}.")
    
    elif userChoice == "Tesoura" and pcChoice == "Papel":
        print("Você ganhou!")
        print(f"O computador escolheu {pcChoice}.")
        
    elif userChoice == "Pedra" and pcChoice == "Tesoura":
        print("Você ganhou!")
        print(f"O computador escolheu {pcChoice}.")
    
    else:
        print(f"Empate! os dois escolheram {pcChoice}")
        
    denovo = input("\nDeseja tentar novamente? (Sim ou Não): ")
    if denovo.lower() == "sim":
        return desafio45()
        
desafio45()