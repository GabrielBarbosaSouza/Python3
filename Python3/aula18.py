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
            
