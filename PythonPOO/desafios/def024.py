from rich.traceback import install
from abc import ABC, abstractmethod

install()

class BebidaQuente(ABC):
    """
Uma classe que faz 3 etapas de uma bebida quente (café, cha e leite)
A classe prepara a bebida fervendo ela, misturando e servindo.

bebidas = [Cafe(), Cha(), Leite()]

for bebida in bebidas:
    bebida.preparar()
    print()
    """
    
    def ferver_agua(self):
        print("1. Fervendo a água a 100 °C")
        
    @abstractmethod    
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass
    
    
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        
   
class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando a água pressurizada pelo pó de café moído.")
        
    def servir(self):
        print("3. Servindo em xícara pequena.\n--- Bebida Pronta! ---")
        
        
class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê.")
        
    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.\n--- Bebida Pronta! ---")
        
        
class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando vapor pressurizada pelo bico do leite.")
        
    def servir(self):
        print("3. servindo na caneca grande, já com café.\n--- Bebida Pronta! ---")

bebidas = [
    Cafe(),
    Cha(),
    Leite()
]

for bebida in bebidas:
    bebida.preparar()
    print()