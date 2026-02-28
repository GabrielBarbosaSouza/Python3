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
    print(f'Você digitou {len(numeros[1])} números pares. São eles: {numeros[1]}')

def desafio86():
    