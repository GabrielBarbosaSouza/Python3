from rich import print, inspect
from rich.traceback import install
from datetime import datetime

install()


class Pessoa:
    def __init__(
        self,
        nome: str,
        nascimento: int
    ):
        self._nome = nome
        self._nascimento = 2000

        self.nascimento = nascimento

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_nascimento: int) -> None:
        if novo_nascimento >= datetime.now().year:
            print(f"[red]Ano {novo_nascimento} inválido.[/]")
            return

        self._nascimento = novo_nascimento

    @property
    def idade(self) -> int:
        return datetime.now().year - self._nascimento

    @idade.setter
    def idade(self, nova_idade: int) -> None:
        print("[red]Você não pode alterar a idade de uma pessoa. Altere o nascimento.[/]")


class Aluno(Pessoa):
    cursos_oficiais: list[str] = ["CC", "ADM", "ADS", "Odonto"]

    def __init__(
        self,
        nome: str,
        nascimento: int,
        curso: str
    ):
        super().__init__(nome, nascimento)

        self._curso = "CC"
        self.curso = curso

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, nome: str) -> None:
        if nome not in self.cursos_oficiais:
            print(f"[red]O curso {nome} não está entre os cursos oficiais.[/] {self.cursos_oficiais}")
            return

        self._curso = nome

    @classmethod
    def add_curso(cls, curso: str) -> None:
        if curso in cls.cursos_oficiais:
            print(f"[red]O curso {curso} já está cadastrado.[/]")
            return

        cls.cursos_oficiais.append(curso)
        print(f"[green]Curso {curso} adicionado.[/]")


g = Aluno("Gabriel", 2008, "CC")

g.curso = "Sei lá"
g.nascimento = 2005

inspect(g, private=True, methods=True)