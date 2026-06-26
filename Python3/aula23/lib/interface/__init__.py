def linha(tamanho=40):
    return "-" * tamanho

def cabecalho(titulo):
    print()
    print(linha())
    print(f'\033[34m{titulo.center(40)}\033[m')
    print(linha())
        

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[34m{c}\033[m - {item}")
        c += 1