def desafio113():
    def leiaInt(num):
        while True:
            entrada = input(num)
            try:
                return int(entrada)
            except ValueError:
                print('\033[31mERRO! Digite um número inteiro!\033[m')
        
        
    def leiaFloat(num):
        while True:
            entrada = input(num)
            try:
                return float(entrada)
            except ValueError:
                print('\033[31mERRO! Digite um número real!\033[m')


    i = leiaInt('Digite um número inteiro: ')
    f = leiaFloat('Digite um número real: ')

    print(f'Você digitou {i} e {f}')


import urllib.request

def desafio114():
    try:
        site = urllib.request.urlopen('https://ong-eg.github.io/SmartEco/')
    except Exception as e:
        print(f'Não consegui acessar esse site!\nErro: {e}')
    else:
        print('Consegui acessar esse site!')