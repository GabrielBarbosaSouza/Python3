from def040 import *

def main():
    usuarios = [
        Usuario("Gabriel", "gabriel@gmail.com"),
        Usuario("Cristiane", "cristiane@gmail.com"),
        Usuario("Vicente", "vicente@gmail.com")
    ]

    alunos = [
        Aluno("Gabriel", "Ciências da Computação", "2 período"),
        Aluno("Nicole", "Odontologia", "2 período")
    ]
    
    exportar_dados(XML(), alunos)
    exportar_dados(JSON(), alunos)
    
    exportar_dados(XML(), usuarios)
    exportar_dados(JSON(), usuarios)

if __name__ == "__main__":
    main()