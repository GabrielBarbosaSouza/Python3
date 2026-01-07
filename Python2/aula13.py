import time
from datetime import date

def desafio46():
    print("Contagem regressiva para os fogos de artifícios estourarem em...")
    for i in range(10, 0, -1):
       print(i)
       time.sleep(1)
        
def desafio47():
    for i in range(2,52, 2):
        print(i)
        
def desafio48():
    soma = 0
    for i in range(3, 501,6):
        soma = soma + i
    print(soma)
    
 #nao sei

def desafio49():
    n = int(input("Digite um número para ver a sua tabuada?: "))
    t = int(input("Até que número você deseja ver a tabuada?: "))
    
    for i in range(1,t+1):
        print(f"{i} x {n} = {n * i}")
        
def desafio50():
    soma = 0
    cont = 0

    for _ in range(1, 7):
        num = int(input("Digite um número inteiro: "))

        if num % 2 == 0:
            soma = soma + num
            cont = cont + 1

    print(f"Dentre esses números, você digitou {cont} números pares.")
    print(f"Somando apenas os pares o resultado fica: {soma}")
    
def desafio51():
    pT = int(input("Digite o primeiro termo de uma PA: "))
    r = int(input("Digite a razão dessa PA: "))
    
    contador = 1
    
    for i in range(contador, 11):
        print(pT, end= " -> ")
        contador += 1
        pT += r
    
    print("Fim!!")
desafio51()

def desafio52():
    n = int(input("Digite um número para conferir se ele é um número primo: "))
    
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            print("\033[31m", end = " ")
            total += 1
        else:
            print("\033[0m", end = " ")
        print(i, end = " ")
        
    print(f"\n\033[0mO número \033[34m{n}\033[0m é dívisível \033[32m{total}\033[0m vezes!")
    
    if total > 2:
        print(f"Portanto, o número {n}\033[31m NÃO é primo!\033[0m")
    else:
        print(f"Portanto, o número {n}\033[32m É primo!\033[0m")

def desafio53():
    frase = input("Escreva uma frase: ").lower().replace(' ', '')
    frase_inversa = ''
    
    for i in range(len(frase)-1, -1, -1):
        frase_inversa += frase[i]
        
    if frase == frase_inversa:
        print("Essa frase é um palíndromo")
    else:
        print("Essa frase não é um palíndromo")
    
def desafio54():
    
    tot_maior = 0
    tot_menor = 0
    
    for i in range(1,8):
        nasc = input("Digite uma data de nascimento (DD/MM/NNNN): ")
        ano_atual = int(date.today().year)
        ano_nascimento = int(nasc.replace('/', ' ').split()[2])
        idade = ano_atual - ano_nascimento
    
        if idade <= 17:
            print("Essa pessoa é de \033[31mmenor\033[0m.\n")
            tot_menor += 1
        else:
            print("Essa pessoa é de \033[32mmaior\033[0m.\n")
            tot_maior += 1
    print(f"Ao todo, teve-se {tot_menor} pessoas de menor e {tot_maior} pessoas de maior")
    
def desafio55():
    pesos = []
    
    for p in range(1, 6):
        peso = float(input(f"Informe o peso da {p}° pessoa: "))
        pesos.append(peso)
    
    maior = max(pesos)
    menor = min(pesos)
    
    print(f"O maior peso dentre os que você citou é {maior}")
    print(f"O menor peso dentre os que você citou é {menor}")
    
def desafio56():
    maiorIdadeM = 0
    maiorIdadeM_nome = ""
    
    soma_idades = 0
    
    qntd_mulheres_menosDe20 = 0
    
    n = 0
    for i in range(1,5):
        n += 1
        print(f"\n--------{n}° PESSOA--------")
        nome = input("Digite o seu nome: ").capitalize()
        idade = int(input("Digite a sua idade: "))
        genero = input("Digite o seu gênero (M/F): ").lower()
        if idade > maiorIdadeM and genero == "m":
            maiorIdadeM = idade
            maiorIdadeM_nome = nome
        if idade < 20 and genero == "f":
            qntd_mulheres_menosDe20 += 1
        soma_idades += idade
    
    media = soma_idades / n
    
    print(f"A média de todas as idades é de {media}")
    print(f"\nO homem mais velho é o {maiorIdadeM_nome}, ele tem {maiorIdadeM} anos.")
    print(f"Ao todo, tem {qntd_mulheres_menosDe20} pessoas com menos de 20 anos.")