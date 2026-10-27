from def034 import *

def main():
    funcionarios = [
        Gerente("Vicente", 8000),
        Designer("Cristiane", 8000),
        Desenvolvedor("Gabriel", 8000)
    ]
    
    for funcionario in funcionarios:
        print(funcionario)
    

if __name__ == "__main__":
    main()