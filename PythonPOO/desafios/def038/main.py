from def038 import *

def main():
    p1 = Produto("Caderno", 39.99)
    p2 = Produto("Lápis", 2.50)
    p3 = Produto("Estojo", 7.49)
    p4 = Produto("Régua", 11.20)

    c1 = Carrinho()
    c1 = c1 + p1 + p2 + p4
    
    print(c1)

if __name__ == "__main__":
    main()