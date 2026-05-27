def escreva(texto):
    tamanho = len(texto)
    print("~" * tamanho)
    print(texto.center(tamanho))
    print("~" * tamanho)
    

def desafio96():
    def area(b, a):
        print(f"A área de {b} x {a} é {b*a}")
        
    
    # print("CONTROLE DE TERRENOS")
    # print("=-"*20)
    
    # base = float(input("Largura (m): "))
    # altura = float(input("Comprimento (m): "))
    
    # area(base, altura)

def desafio97():
    def escreva(texto):
        tamanho = len(texto)
        print("~" * tamanho)
        print(texto.center(tamanho))
        print("~" * tamanho)
        
    escreva("Olá, mundo!")

import time

def desafio98():
    def contador(inicio, fim, passo):
        if passo <= 0:
            print("Digite um passo maior que 0!")
            print("Reinicie novamente a função.")
            print()
            
        escreva(f"Contagem de {inicio} até {fim} (de {passo} em {passo})")
        if inicio <= fim:
            cont = inicio
            while cont <= fim:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont += passo
        else:
            cont = inicio
            while cont >= fim:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont -= passo
        print("Fim.")

        print()
        escreva(f"Contagem de {fim} até {inicio} (de dois em dois)")
        if fim <= inicio:
            cont = fim
            while cont <= inicio:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont += 2
        else:
            cont = fim
            while cont >= inicio:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont -= 2
        print("Fim.")

        print("Escolha o seu inicio, fim e passo de forma personalizada:")
        inicio = int(input("Digite seu novo inicio: "))
        fim = int(input("Digite seu novo fim: "))
        passo = int(input("Digite a quantidade de passos a saltar: "))
        
        escreva(f"Contagem de {inicio} até {fim} (de {passo} em {passo})")
        if inicio <= fim:
            cont = inicio
            while cont <= fim:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont += passo
        else:
            cont = inicio
            while cont >= fim:
                time.sleep(0.3)
                print(cont, end=", ", flush=True)
                cont -= passo
        print("Fim.")
    contador(10, 1, 1)

def desafio99():
    def maior(* valor):
        escreva("Analisando os valores passados...")
        print(f"Valores: {valor} | Ao todo foram analisados {len(valor)} valores. ")
        print(f"O maior valor é {max(valor)}")
        
    maior(2, 3)
    maior(1, 2, 5)
    maior(0)

import random
import time
def desafio100():
    def sortear(lista):
        print("Sorteando 5 valores: ", end="")
        for n in range(5):
            n = random.randint(1, 10)
            lista.append(n)
            print(n, end=" ", flush=True)
            time.sleep(0.3)
            
    def somaPar(lista):
        listaPar = list()
        for n in lista:
            if n % 2 == 0:
                listaPar.append(n)
        print(f"\nSomando os números pares entre {lista} obtemos {sum(listaPar)}")
    
    numeros = list()
    sortear(numeros)
    somaPar(numeros)