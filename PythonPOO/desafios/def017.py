from rich import print
from rich.panel import Panel

class Produto:
    """
Uma classe que lê e apresenta um produto.

Para usar use:
variavel = Produto(nome, preco)
    """
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = f"R${preco:.2f}"
        
    def etiqueta(self):
        tabela = Panel(f"{self.nome}\n{self.preco}",
                       title="Produto",
                       width=50)
        
        return tabela
        
        
p1 = Produto("iPhone 15", 3800)
p2 = Produto("MacBook", 1500)

print(p1.etiqueta())
print(p2.etiqueta())