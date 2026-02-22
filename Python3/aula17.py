linha = '=-'*20

def desafio78():    
    numeros = []

    for posicao in range(5):
        numero = int(input(f'Digite um número inteiro para a posição {posicao}: '))
        numeros.append(numero)
    
    maior= max(numeros)
    menor = min(numeros)
    print(f'O maior número digitado foi {maior} e ele esta na posição {numeros.index(maior)}')
    print(f'O menor número digitado foi {menor} e ele esta na posição {numeros.index(menor)}')

def desafio79():
    continuar = ''
    numeros = []

    while continuar != 'n':
        while True:
            numero = input('Digite um número inteiro: ')
            if numero.isnumeric():
                numero = int(numero)
                if numero in numeros:
                    print('\nEsse número já foi cadastrado!')
                    break
                else:
                    numeros.append(numero)
                    print('\nNúmero adicionado!')
                    break
            else:
                print('\nNúmero inválido')
                
        continuar = input('Deseja continuar? (S/N): ').lower()      
        if continuar == 'n':
            print('=-'*15)
            print(f'Você digitou os números {sorted(numeros)}')

# def desafio80():

def desafio81():
    continuar = ''
    numeros = []

    while continuar != 'n':
        while True:
            numero = input('Digite um número inteiro: ')
            if numero.isnumeric():
                numero = int(numero)
                numeros.append(numero)
                print('\nNúmero adicionado!')
            else:
                print('\nNúmero inválido')
                
            continuar = input('Deseja continuar? (S/N): ').lower()      
            if continuar == 'n':
                print('=-'*15)
                print(f'Você digitou {len(numeros)} números')
                print(f'Você digitou os números {sorted(numeros, reverse=True)}')
                if 5 in numeros:
                    print('Você digitou o número 5')
                else:
                    print('Você não digitou o número 5')
            elif continuar == 's':
                continue
            else:
                print('Digite apenas S ou N')
                continuar = input('Deseja continuar? (S/N): ').lower()
                
def desafio82():
    numeros = []
    impares = []
    pares = []
    
    while True:
        numero = input('Digite um número: ')
        if numero.isnumeric():
            numero = int(numero)
            numeros.append(numero)
            if numero % 2 == 1:
                impares.append(numero)
            else:
                pares.append(numero)
        else:
            print('Digite um número inteiro!')
            
        continuar = input('Deseja continuar? (S/N): ')
        if continuar.lower() == 's':
            continue
        elif continuar.lower() == 'n':
            break
        else:
            print('Digite "S" para sim e "N" para não')
            
    print(linha)
    print(f'A lista de números digitados foi: {numeros}')
    print(f'Dentro dos números digitados, os números impares são: {impares}')
    print(f'Dentro dos números digitados, os números pares são: {pares}')

def desafio83():
    