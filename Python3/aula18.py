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
kg.sort()

print(kg)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'{kg[0:]} são as pessoas mais pesadas.')
print(f'{} são as pessoas mais leves.')
