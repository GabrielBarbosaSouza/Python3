def leiaDinheiro(texto):
    while True:
        n = input(texto)
        if n.isnumeric():
            n = float
            
            return n
        else:
            return f"\033[31mERRO: {texto} não é um preço válido!\033[m"

        