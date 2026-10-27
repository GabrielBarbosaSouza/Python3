from rich.traceback import install
from abc import ABC, abstractmethod

install()

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        pass
    
class Moto(Transporte):
    fator = 0.5
    
    def calc_frete(self):
        self.distancia * self.fator
    
    
class Caminhao(Transporte):
    fator = 1.2
    
    def calc_frete(self):
        self.distancia * self.fator
    
    
class Drone(Transporte):
    fator = 9.5
    
    def calc_frete(self):
        self.distancia * self.fator