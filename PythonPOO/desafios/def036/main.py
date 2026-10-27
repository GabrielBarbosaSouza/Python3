from def036 import *


def main():
    finalizar_compra(Pix(), 1_500)
    finalizar_compra(CartaoDeCredito(), 2_234.4)
    finalizar_compra(Boleto(), 493.23)

if __name__ == "__main__":
    main()