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

def desafio80():
    numeros = []
    c = 0
    
    while c != 5:
        numero = input('Digite um número: ')
        if numero.isnumeric():
            numero = int(numero)
            numeros.append(numero)
            c += 1
        else:
            print('Digite um número correto')
    print(f'A lista dos números de forma ordenada foram: {sorted(numeros)}')
desafio80()
