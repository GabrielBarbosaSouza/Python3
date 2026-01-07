import random

def desafio28():

    palpite = int(input("""
Tente acertar o número que eu pensei!
obs: é um número de 1 a 5: """))

    numeros = [1, 2, 3, 4, 5]
    aleatorio = int(random.choice(numeros))

    if palpite == aleatorio:
        print("Parabens! Você acertou o número")
    else:
        print(f"Errouu! O número era {aleatorio} hahaha")
        
        denovo = input("Quer tentar denovo? (Responda com Sim ou Não): ")
        if denovo.lower() == "sim":
            return desafio28()
            
def desafio29():
    velocidade = float(input("Digite a velocidade de um carro(apenas números): "))
    
    if velocidade > 80:
        multa = (velocidade - 80) * 7
        print(f"Por conta dessa alta velocidade, você recebera uma multa de {multa}")
    else:
        print("Velocidade dentro do limite permitido.")

def desafio30():
    n = int(input("Digite um número para consultar se ele é impar ou par: "))
    
    if n % 2 == 1:
        print("Ele é um número impar!")
    else:
        print("Ele é um número par!")
        
def desafio31():
    km = float(input("Informe a distância da sua viagem (Use apenas números): "))
    
    if km <= 200:
        passagem = km + (km * 0.50)
        print(f"O valor da sua passagem é R${passagem:.2f}")
    else:
        passagem = km + (km * 0.45)
        print(f"O valor da sua passagem é R${passagem:.2f}")
    
def desafio32():
    ano = int(input("Digite um ano para conferir se ele é bissexto: "))
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é bissexto!")
    else:
        print(f"{ano} não é bissexto.")

def desafio33():
    n1 = int(input("Escreva um número: "))
    n2 = int(input("Escreva um segundo número: "))
    n3 = int(input("Escreva um terceiro e último número: "))
    
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    
    print(f"O maior número é {maior} e o menor número é {menor}")


def desafio34():
    salario = float(input("Informe um salário: "))
    
    if salario > 1250.0:
        salario = salario * 1.10
        print(f"Com um aumento de 10% o seu salário fica R${salario:.2f}")
    else:
        salario = salario * 1.15
        print(f"Com um aumento de 15% o seu salário fica R${salario:.2f}")

def desafio35():
    reta1 = float(input("Para saber se é possível formar um triangulo, informe um valor para a primeira reta: "))
    reta2 = float(input("Informe um valor para a segunda reta: "))
    reta3 = float(input("Informe um valor para a terceira reta: "))
    
    if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
        print("Um triângulo PODE ser formado com essas retas.")
    else:
        print("Um triângulo NÃO pode ser formado com essas retas.")