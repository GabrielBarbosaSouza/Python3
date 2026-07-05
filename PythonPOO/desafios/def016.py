from rich import print

class Funcionario:
    """
Uma classe que lê funcionários e os apresenta com base no nome, setor e cargo da pessoa.

Para usar use:
variavel = Funcionario(nome, setor, cargo)
    """
    
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def apresentacao(self):
        return f":wave:  Olá!, eu sou [blue]{self.nome}[/], [green]{self.cargo}[/] do setor de [red]{self.setor}[/] da Megadan Broker!"
        
        
pessoa1 = Funcionario("Gabriel", "Executivo", "TI")
pessoa2 = Funcionario("Nicole", "Administrativo", "Financeiro")

print(pessoa1.apresentacao())
print(pessoa2.apresentacao())