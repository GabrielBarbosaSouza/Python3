# Declaração de uma CLASSE
class Pessoa:
    """
Classe que le um nome e idade de uma pessoa e retorna essas informações.

Para ver uma nova pessoa use a estrutura:
variavel = Pessoa(nome, idade)
    """
    # Método Construtor
    def __init__(self, nome='vazio', idade=0):
        # Atributos de Instância
        self.nome = nome
        self.idade = idade
        
    # Métodos de Instância
    def aniverario(self):
        self.idade += 1  
    
    def __str__(self):
        return f"{self.nome} é uma Pessoa e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome:{self.nome} ; idade: {self.idade}"
    
# Declaração de um OBJETO
g1 = Pessoa("Gabriel", 18)

g1.aniverario()
print(g1)

print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
print(Pessoa.__doc__)