from rich import inspect
from classes import Aluno, Professor, Funcionario

def main():
    a1 = Aluno("Gabriel", 18, "CC", "H-302")
    # inspect(a1, methods=True)
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor("Cicero", 67, "T.I", "Mestrado e Doutorado")
    # inspect(p1, methods=True)
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario("Fulano", 20, "Comercial", "Administrativo")
    # inspect(f1, methods=True)
    f1.fazer_aniversario()
    f1.bater_ponto()
    
if __name__ == "__main__":
    main()