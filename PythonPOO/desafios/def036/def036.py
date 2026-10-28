from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None    
    
    
    @property
    def valor(self) -> float:
        return self._valor
    
    
    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Digite um valor positivo.")
    
    
    @property
    def fvalor(self) -> float:
        # poderia ser um return f"R${self.valor:,.2f}"
        
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        return locale.currency(self.valor, grouping=True)
    
    
    @abstractmethod
    def pagar(
        self, 
        valor: float
    ):
        pass
    

class Boleto(Pagamento):
    def pagar(
        self, 
        valor: float
    ):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} feito via boleto."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via boleto."

class Pix(Pagamento):
    def pagar(
        self, 
        valor: float
    ):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} feito via pix."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via pix."

class CartaoDeCredito(Pagamento):
    def pagar(
        self, 
        valor: float
    ):
        try:
            self.valor = valor
            return f"Pagamento de {self.fvalor} feito via cartão de crédito."
        except Exception as e:
            return f"Falha no pagamento de {self.fvalor} via cartão de crédito."
            
            
def finalizar_compra(tipo_de_pagamento: Pagamento, valor: float):
    print(tipo_de_pagamento.pagar(valor))
    