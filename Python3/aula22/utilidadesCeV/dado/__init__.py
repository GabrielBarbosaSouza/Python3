def leiaDinheiro(texto):
    while True:
        entrada = str(input(texto)).replace(',', '.').strip()
        
        if entrada.isalpha() or entrada == '':
            print(f"\033[31mERRO: {entrada} não é um preço válido!\033[m")
        else:
            return float(entrada)