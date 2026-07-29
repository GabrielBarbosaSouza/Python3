from rich import print, inspect
from rich.traceback import install

install()

class Diario:
    def __init__(self, senha_padrao: str = "Gabriel"):
        self.__segredos: list[str] = []
        self.__senha_padrao = senha_padrao
        
    def escrever(self, mensasgem) -> None:
        self.__segredos.append(mensasgem)
    
    def ler(self, senha) -> None:
        if senha != self.__senha_padrao:
            print("[red]Você não pode ler o diario.[/]")
        else:
            print("[green]DIÁRIO LIBERADO[/]")
            
            for segredo in self.__segredos:
                print(f"- {segredo}")
    
diario = Diario()
diario.escrever("Segredo 1")

diario.ler("Gabriel")