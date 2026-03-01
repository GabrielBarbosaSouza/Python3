linha = '=-'*20

def desafio84():
    pessoas = list()

    while True:
        nome = str(input('Digite um nome: '))
        peso = float(input('Digite uma peso: '))
        
        pessoas.append([nome, peso])
        
        continuar = str(input('Deseja continuar? (S/N): ')).strip().lower()
        if continuar == 'n':
            break
        elif continuar != 's':
            continuar = str(input('Digite "S" para sim e "N" para não')).strip().lower()

    kg = [p[1] for p in pessoas]
    pesado = max(kg)
    leve = min(kg)

    print(f'Foram cadastradas {len(pessoas)} pessoas.')

    print(f'A pessoa mais pesada é ', end='')
    for p in pessoas:
        if p[1] == pesado:
            print(p[0])
            
    print(f'A pessoa mais leve é ', end='')
    for p in pessoas:
        if p[1] == leve:
            print(p[0])
            
def desafio85():
    numeros = [[], []]
    
    for _ in range(7):
        num = int(input('Digite um número inteiro: '))
        if num % 2 == 0:
            numeros[0].append(num)
            numeros[0].sort()
        else:
            numeros[1].append(num)
            numeros[1].sort()

    print(linha)
    print(f'Você digitou {len(numeros[0])} números pares. São eles: {numeros[0]}')
    print(f'Você digitou {len(numeros[1])} números impares. São eles: {numeros[1]}')

def desafio86():
    matriz = [
        [[], [], []], 
        [[], [], []],
        [[], [], []],
    ]
    
    for l in range(3):
        for c in range(3):
            matriz[l][c] = input(f'Digite um valor para [{l}, {c}]: ')
     
    print(linha)   
    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()

def desafio87():
    matriz = [
        [[], [], []], 
        [[], [], []],
        [[], [], []],
    ]
    
    par = list()
    # coluna3 = list()
    linha2 = list()
    
    for l in range(3): 
        for c in range(3):
            matriz[l][c] = input(f'Digite um valor para [{l}, {c}]: ')
               
            if int(matriz[l][c]) % 2 == 0:
                par.append(int(matriz[l][c]))
              
        if l == 1:
            for c in range(3):
                linha2.append(int(matriz[l][c]))  
            
    print(linha)   
    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()
          
    print(f'\nA soma de todos os números pares dessa matriz é {sum(par)}')
    
    print(f'O maior valor da segunda linha é {max(linha2)}')
desafio87()
    
    