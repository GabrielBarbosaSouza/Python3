from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(
        self,
        nome: str = None,
        salario: float = 1621
    ):
        self.nome = nome
        self.__salario = salario
     
     
    @abstractmethod  
    def calcular_bonus() -> float:
        pass
       
       
    @property
    def salario(self) -> float:
        return self.__salario
    
    
    @salario.setter
    def salario(
        self,
        valor: float = None
    ):
        if valor is None:
            raise ValueError("Impossível reajustar o salário do funcionário.")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Você não pode mudar o salário de um funcionário!")
        
    
    def __str__(self):
        return f"{self.nome} recebe R${self.salario:,.2f}. Por isso tem R${self.calcular_bonus()} de bônus"
    
       
class Gerente(Funcionario):
    def calcular_bonus(self):
        # Gerente: 15% de bônus
        return self.salario * 0.15
    
    
class Designer(Funcionario):
    def calcular_bonus(self):
        # Designer: 10 de bônus
        return self.salario * 0.1
    
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        # Desenvolvedor: 8% de bônus
        return self.salario * 0.08
    