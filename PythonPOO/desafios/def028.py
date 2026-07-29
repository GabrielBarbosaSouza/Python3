from rich import print, inspect
from rich.traceback import install

install()


class Termostato():
    """
Uma classe que cria um termostato, que tem a temperatura mínima de 16 e máxima de 30.
As temperaturas aceitaveis vão de 0.5 em 0.5. Ou seja, 16, 16.5, 17 ... 29.5 e 30

Como usar:
VARIAVEL = Termostato()
VARIAVEL.temperatura = TEMPERATURA
print(f"A temperatura é {VARIAVEL.ftemperatura}")
    """
    
    def __init__(self,temperatura: float = 24.0):
        
        self.__temperatura: float = temperatura
        
    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temp: float):
        if not 16 <= temp <= 30 or temp % 1 not in (0, 0.5):
            raise ValueError("Temperatura inválida. Deve estar entre 16 e 30 e terminar em .0 ou .5")

        self.__temperatura = temp
    
    @property
    def ftemperatura(self) -> str:
        return f"{self.__temperatura:.1f} °C"
    
        
t = Termostato()
t.temperatura = 29
print(f"A temperatura é {t.ftemperatura}")
# inspect(t, methods=True, private=True)