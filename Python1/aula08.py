import math
import random

def desafio16():
    n = input("Digite um número: ")
    if not n.replace('.', ',', 1).replace(',', '', 1).isdigit():
        print("Por favor, digite um número válido.")
        return desafio16()
    
    int_n = math.floor(float(n))
    print(f"O número {n} tem a parte inteira {int_n}.")

def desafio17():
    c1 = input("Digite o comprimento do cateto oposto: ")
    if not c1.replace('.', ',', 1).replace(',', '', 1).isdigit():
        print("Por favor, digite um número válido.")
        return desafio16()
    c2 = input("Digite o comprimento do cateto adjacente: ")
    if not c2.replace('.', ',', 1).replace(',', '', 1).isdigit():
        print("Por favor, digite um número válido.")
        return desafio17()
    
    c1 = float(c1)
    c2 = float(c2)
    
    h = pow(c1, 2) + pow(c2, 2)
    print(f"A hipotenusa vai medir {h}")
    
def desafio18():
    angulo = input("Digite um ângulo em graus: ")
    if not angulo.replace(',', '.', 1).replace('.', '', 1).isdigit():
        print("Por favor, digite um número válido.")
        return desafio18()
    
    angulo = float(angulo.replace(',', '.', 1))
    rad = math.radians(angulo)
    
    seno = math.sin(rad)
    cosseno = math.cos(rad)
    tangente = math.tan(rad)
    
    print(f"\nO ângulo de {angulo} tem:\nO seno de {seno: .2f}")
    print(f"Cosseno de {cosseno: .2f}")
    print(f"E a tangente de {tangente: .2f}.")
    
def desafio19():
    print("Um professor quer sortear um dos seus quatro alunos para apagar o quadro.")
    
    a1 = input("Digite o nome do primeiro aluno: ")
    if not a1.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio19()
    
    a2 = input("Digite o nome do segundo aluno: ")
    if not a2.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio19()
    
    a3 = input("Digite o nome do terceiro aluno: ")
    if not a3.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio19()
    
    a4 = input("Digite o nome do quarto aluno: ")
    if not a4.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio19()

    alunos = [a1, a2, a3, a4]
    sorteado = random.choice(alunos)
    print(f"O aluno sorteado foi {sorteado}.")

def desafio20():
    print("Um professor quer sortear a ordem de apresentação de entre 4 alunos.")
    
    a1 = input("Digite o nome do primeiro aluno: ")
    if not a1.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio20()
    
    a2 = input("Digite o nome do segundo aluno: ")
    if not a2.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio20()
    
    a3 = input("Digite o nome do terceiro aluno: ")
    if not a3.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio20()
    
    a4 = input("Digite o nome do quarto aluno: ")
    if not a4.isalpha():
        print("Por favor, digite um nome válido.")
        return desafio20()

    alunos = [a1, a2, a3, a4]
    random.shuffle(alunos)
    print(f"A ordem de apresentarção será nessa ordem:\n{alunos}.")

desafio20()