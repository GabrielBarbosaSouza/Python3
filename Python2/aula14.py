import random
from InquirerPy import prompt
import math

def desafio57():
    sexo = input("Digite o sexo de uma pessoa. (M/F): ").upper()
    while sexo != "M" and sexo != "F":
        print("Digite um valor válido. (M/F)\n")
        sexo = input("Digite o sexo de uma pessoa. (M/F): ").upper()
    print("Obrigado!")
            
def desafio58():
    palpite = int(input("""
Tente acertar o número que eu pensei!
obs: é um número de 1 a 10: """))

    palpites = 0
    numero = random.randint(1, 10)
    
    while palpite != numero:
        palpite = int(input("Tente novamente!: "))
        palpites += 1
        
    print("Parabens, você acertou!")
    print(f"Você precisou de {palpites} palpites para acertar.")
    
def desafio59():
    opcoes = [
        "Somar",
        "Multiplicar",
        "Maior",
        "Novos Números",
        "Sair do programa"
    ]
    
    menu = [
        {
            "type": "list",
            "name": "menu",
            "message": "Deseja o que você deseja fazer com esses números: \n",
            "choices": opcoes
        }
    ]
    maior_numero = 0
    
    print("\n\033[036mBem vindo!\033[0m")
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite o outro número inteiro: "))
    if n1 > n2:
        maior_numero = n1
    else:
        maior_numero = n2
    
    while True:
        aparecer_menu = prompt(menu)
        userChoice = aparecer_menu["menu"]
    
        if userChoice == "Somar":
            print(f"\nO resultado da soma entre {n1} e {n2} é {n1+n2}!")
            input("\nPressione ENTER para voltar ao menu...")
        elif userChoice == "Multiplicar":
            print(f"\nO resultado da multiplicação entre {n1} e {n2} é {n1*n2}!")
            input("\nPressione ENTER para voltar ao menu...")
        elif userChoice == "Maior":
            print(f"\nO maior número entre {n1} e {n2} é {maior_numero}!")
            input("\nPressione ENTER para voltar ao menu...")
            if n1 == n2:
                print("\nOs valores são os mesmos! Você escolheu números iguais.")
                input("\nPressione ENTER para voltar ao menu...")
        elif userChoice == "Novos Números":
            n1 = int(input("Digite um número inteiro: "))
            n2 = int(input("Digite o outro número inteiro: "))
            if n1 > n2:
                maior_numero = n1
            else:
                maior_numero = n2
        elif userChoice == "Sair do programa":
            print("Saindo do programa...")
            break
            
def desafio60():
    n = n_inicial = int(input("Digite um número para ver o seu fatorial: "))
    if n == 0:
        print("0 x 0 = 1")
        return
        
    if n == 1:
        print("1 x 1 = 1")
        return
    
    while n > 1:
        print(f"{n}", end= " x ")
        n -= 1
        if n == 1:
           print(f"{n}", end= " = ")
    print(math.factorial(n_inicial))

def desafio61():
    pT = int(input("Digite o primeiro termo de uma PA: "))
    r = int(input("Digite a razão dessa PA: "))
    
    contador = 0
    
    while contador < 10:
        print(pT, end= " -> ")
        pT += r
        contador += 1
    print("Fim!!")
    
def desafio62():
    pT = int(input("Digite o primeiro termo de uma PA: "))
    r = int(input("Digite a razão dessa PA: "))
    
    contador = 0
    total = 10
    mais = 10
    
    while mais != 0:
        while contador < total:
            print(pT, end= " -> ")
            pT += r
            contador += 1
        print("Fim!!")
        mais = int(input('\nGostaria de adicionar mais quantos termos? (Digite "0" para cancelar): '))
        if mais == 0:
            break
        total += mais
    print("Encerrando programa...")

def desafio63():
    print("\033[36m=-"*13)
    print("\033[0mSequência de Fibonacci")
    print("\033[36m=-\033[0m"*13)
    
    while True:
        termoTotal = input(f"\nDigite quantos termos você quer ver da \033[36mSequência de Fibonacci\033[0m: ")
        if termoTotal.isnumeric():
            termoTotal = int(termoTotal)
            break
        else:
            print("Digita um número inteiro!")
    
    contador = 0
    anteriorN = 0
    atualN = 1
    
    fibonacci = []
    
    while contador < termoTotal:
        fibonacci.append(anteriorN)
        proximoN = anteriorN + atualN
        anteriorN = atualN
        atualN = proximoN
        contador += 1
            
    print(fibonacci)

def desafio64():
    nTotal = []
    
    while True:
        n = input('Escreva um número inteiro (para terminar o programa digite "999"): ')
        if n.isnumeric():
            n = int(n)
            nTotal.append(n)
        else:
            print("\nDigita um número inteiro!")
            
        if n == 999:
            break
        soma = sum(nTotal)
        digitados = len(nTotal)
    print('-='*15)
    print(f"Foram digitados \033[32m{digitados}\033[0m números")
    print(f"A soma de todos esses números foi de: \033[32m{soma}\033[0m")
    print('-='*15)

def desafio65():
    numeros = []
    while True:
        
        n = input('Escreva um número inteiro (para terminar o programa digite "999"): ')
        if n.isnumeric():
            n = int(n)
            numeros.append(n)
        else:
            print("Escreva um número inteiro!")
            
        continuar = input("Deseja continuar digitando números? (S/N): ")
        if continuar.lower() == "s":
            continue
        else:
            media = sum(numeros) / len(numeros)
            maior = max(numeros)
            menor = min(numeros)
            print(f'A média de todos os números digitados foi de: \033[32m{media}\033[0m')
            print(f'Dentre todos esses números, o maior foi \033[32m{maior} e o menor foi \033[32m{menor}.\033[0m')
            
