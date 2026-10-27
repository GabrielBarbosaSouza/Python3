from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} e está emitindo um som.")

class Pato(Animal):
    def emitir_som(self):
        print(f'{self.nome} disse "Quack Quack!"')
    
    
class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} disse "Au Au!"')


class Spitz(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} disse "au au au au au au au au!"')


class PitBull(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} disse "HUFF HUFF!"')


class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} disse "Miau!"')
    
    
class Galinha(Animal):
    def emitir_som(self):
        print(f'{self.nome} disse "Po Po!"')

dog = Cachorro("Tchuco")
dog_fofo = Spitz("Fofinho")
dog_bravo = PitBull("Pandora")

duck = Pato("Donald")
chicken = Galinha("Cocoricó")

dog.emitir_som()
dog_fofo.emitir_som()
dog_bravo.emitir_som()

duck.emitir_som()
chicken.emitir_som()