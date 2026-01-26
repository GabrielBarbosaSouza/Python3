def desafio72():
    numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    )
    
    while True:
        escolha = input('Digite um número entre 0 e 20: ')
        
        if escolha.isnumeric():
            escolha = int(escolha)
            if 0 <= escolha <= 20:
                print(f'Você digitou o número {numeros[escolha]}')
                break
            else:
                print('Número fora do intervalo.')
        else:
            escolha = input('Digite um número entre 0 e 20: ')
    
def desafio73():
    brasileirao = (
    "Flamengo",            # 1º
    "Palmeiras",           # 2º
    "Cruzeiro",            # 3º
    "Mirassol",            # 4º
    "Fluminense",          # 5º
    "Botafogo",            # 6º
    "Bahia",               # 7º
    "São Paulo",           # 8º
    "Grêmio",              # 9º
    "Red Bull Bragantino", # 10º
    "Atlético-MG",         # 11º
    "Santos",              # 12º
    "Corinthians",         # 13º
    "Vasco",               # 14º
    "Vitória-BA",          # 15º
    "Internacional",       # 16º
    "Ceará",               # 17º
    "Fortaleza",           # 18º
    "Juventude",           # 19º
    "Sport"                # 20º
    )
    
    print(f'Os 5 primeiros times do Brasileirão são: {brasileirao[:5]}')
    print(f'Os 4 ultimos times do Brasileirão são: {brasileirao[-4:]}')
    print(f'Os times em ordem alfabética são: {sorted(brasileirao)}')
    print(f'O Mirassol está na posição {brasileirao.index("Mirassol") + 1}° da lista.')

def desafio74():
    
