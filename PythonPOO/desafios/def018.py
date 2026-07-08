from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Churrasco:
    """
Uma classe que calcula tudo o que você precisa para um churrasco com qualquer quantidade de pessoas.
Essa classe calcula a carne total, o custo total e o custo por pessoa.

Consumo Padrão: 400g/pessoa
Preço da carne: R$82,40/kg

Para usar essa classe use:
variavel = Churrasco('Nome do Churrasco', quantidade de pessoas)
varivel.analisar()
    """

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        
    def analisar(self):
        carnePorPessoa = 0.4
        carneTotal = carnePorPessoa * self.quantidade
        custoTotal = carneTotal * 40
        custoPorPessoa = custoTotal / self.quantidade
        
        texto =f"""Analisando [yellow]{self.titulo}[/]  com [red]{self.quantidade} convidados[/]:
Cada participante vai comer {carnePorPessoa:.3f}kg e cada kg custa R$82.40

Recomendo comprar [bold]{carneTotal}[/]kg de carne
O custo total será de [bold]R${custoTotal:.2f}[/]
Cada pessoa pagará [bold]R${custoPorPessoa:.2f}[/] para participar do churras"""
        
        print(Panel(texto, title = self.titulo))
        
        
c1 = Churrasco("Churrasco dos irmão", 11)
c1.analisar()

c2 = Churrasco("Churrasco dos Cria", 100)
c2.analisar()