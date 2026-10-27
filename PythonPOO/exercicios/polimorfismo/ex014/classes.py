from functools import singledispatchmethod

class Analisador():
    
    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possível analisar o valor {valor}")
    
    @analisar.register
    def _(self, valor: int):
            print(f"valor é um número inteiro")
            
    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é uma número real")
    
    @analisar.register
    def _(self, valor: str):
            print(f"valor é uma cadeia de caracteres")
        
    @analisar.register
    def _(self, valor: tuple | list | dict):
            print(f"valor é uma coleção de dados")
            
        