from rich import print
from rich.traceback import install

install()

class Caneta:
    """
Uma classe que te permite a escrever com uma caneta com as principais cores.
Você pode escolher a cor, escrever, pular linhas, destampar e tampar a caneta.

Para usar a classe use:
variavel = Caneta(cor)

Para escrever, lembre-se sempre de destampar a caneta!
variavel.destampar()
    """
    
    
    def __init__(self, cor):
        match cor.lower().strip():
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case "amarelo":
                escolha = "[yellow]"
            case "azul":
                escolha = "[blue]"
            case "roxo":
                escolha = "[magenta]"
            case "ciano":
                escolha = "[cyan]"
            case _:
                escolha = "[white]"
                
        self.cor = escolha
        self.tampada = True
        

    def destampar(self):
        self.tampada = False
        print(f"\n[green]Você destampou a caneta![/]")
        
    
    def tampar(self):
        self.tampada = True
        print(f"\n[red]Você tampou a caneta![/]")
        
        
    def escrever(self, texto) -> str:
        if self.tampada == False:
            print(f"{self.cor}{texto}")
        else:
            print(f":prohibited: [red]Você precisa destampar a sua caneta para escrever![/]")
        
        
    def pular_linha(self, quantidade: int):
        for numero in range(quantidade):
            print()
    
       
caneta1 = Caneta("azul")
caneta1.destampar()
caneta1.escrever("Oi")
caneta1.pular_linha(1)
caneta1.escrever("Tudo bem?")
caneta1.tampar()

caneta2 = Caneta("verde")
caneta2.destampar()
caneta2.escrever("Tudo bem?")
caneta2.tampar()

caneta3 = Caneta("roxo")
caneta2.escrever("Teste")