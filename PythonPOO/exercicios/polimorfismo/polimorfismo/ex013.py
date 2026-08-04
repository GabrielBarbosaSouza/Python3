from abc import ABC, abstractmethod

class Mae(ABC):
    def __init__(self, nome: str = "Mamãe"):
        self.nome = nome
        
    def fazer_pudim(self):
        print(f"{self.nome} faz um pudim igual uma mãe.")
    
    def fritar_coxinha(self):
        print(f"{self.nome} faz uma coxinha igual uma mãe.")
    
    
class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz um pudim igual uma filha.")


class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} faz uma coxinha igual um filho.")


p1 = Mae("Cristiane")
p2 = Filha("Amanda")
p3 = Filho("Gabriel")

p1.fazer_pudim()
p1.fritar_coxinha()
print()

p2.fazer_pudim()
p2.fritar_coxinha()
print()

p3.fazer_pudim()
p3.fritar_coxinha()