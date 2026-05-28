from utilidadesCeV import moeda
from utilidadesCeV import dado

# O Desafio 107, 108 e 109 foram o mesmo. O 109 foi uma melhoria do 108 e o 108 foi uma melhoria do 107.

def desafio107_8_9():
    p = float(input("Digite um preço: R$"))
    print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p)}")
    print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
    print(f"Aumentando 10%, temos {moeda.aumentar(p, 10, True)}")
    print(f"Diminuindo 13%, temos {moeda.diminuir(p, 13, True)}")


# É o desafio anterior, porém bem mais resumido
def desafio110():
    p = float(input("Digite um preço: R$"))
    moeda.resumo(p, 10, 10)


# O desafio111 e 112 foi colocar dividir as funções (e criar mais algumas) em arquivos dentro de modulos.

def desafio112():
    p = dado.leiaDinheiro("Digite um preço: R$")
    moeda.resumo(p, 10, 10)
    
desafio112()