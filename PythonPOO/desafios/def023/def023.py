from rich.traceback import install
from abc import ABC, abstractmethod
from math import pi

install()

class Poligono(ABC):
    """
Uma classe mãe que mostra informações de um polígono.
Para usar a classe informe se deseja ver um quadrado ou um circulo.

variavel = Quadrado(tamanho do lado)
print(variavel.perimetro())
print(variavel.area())
    """
    
    qtd_lados: int = 0

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado
        self.qtd_lados = 4

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio ** 2


q = Quadrado(20)
c = Circulo(10)

print(f"Perímetro do quadrado: {q.perimetro():.2f}")
print(f"Área do quadrado: {q.area():.2f}")

print()

print(f"Perímetro do círculo: {c.perimetro():.2f}")
print(f"Área do círculo: {c.area():.2f}")