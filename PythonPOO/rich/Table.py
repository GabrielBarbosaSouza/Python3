from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")
tabela.add_column("Produto", justify="right", style="red")
tabela.add_column("Preço", justify="center", style="blue")

tabela.add_row("Lápis", "R$1.00")
tabela.add_row("Borracha", "R$0.50")

print(tabela)