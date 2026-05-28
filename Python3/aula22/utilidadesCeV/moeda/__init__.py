def aumentar(num, percent, format=False):
    n = num + (num * (percent / 100))

    if format == False:
        return n
    else:
         return moeda(n)


def diminuir(num, percent, format=False):
    n = num - (num * (percent / 100))

    if format == False:
        return n
    else:
         return moeda(n)


def dobro(num, format=False):
    n = num * 2

    if format == False:    
        return n
    else:
         return moeda(n)


def metade(num, format=False):
    n = num / 2

    if format == False:
        return n
    else:
         return moeda(n)
     

def moeda(num):
    return f"R${num:.2f}".replace('.', ',')

def resumo(num, taxaA=10, taxaD=10):
    print("-" * 35)
    print("RESUMO DO VALOR".center(35))
    print("-" * 35)
    
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do preço: \t{dobro(num, format=True)}")
    print(f"Metade do preço: \t{metade(num, format=True)}")
    print(f"{taxaA}% de aumento: \t{aumentar(num, taxaA, format=True)}")
    print(f"{taxaD}% de redução: \t{diminuir(num, taxaA, format=True)}")
    
    print("-" * 35)