class Retangulo:
    """
Uma classe que calcula a area de um retângulo, de acordo com a altura e base.
A classe não permite que a área seja alterada fora do código.

Como usar:
variavel = Retangulo()
variavel.altura = valor_altura
variavel.base = valor_base
print(variavel.medidas)
    """
    
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base_nova):
        if base_nova <= 0:
            raise ValueError("Base deve ser maior que zero.")
        self._base = base_nova

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura_nova):
        if altura_nova <= 0:
            raise ValueError("Altura deve ser maior que zero.")
        self._altura = altura_nova

    @property
    def area(self):
        return self.base * self.altura

    @property
    def medidas(self):
        return (
            f"BASE = {self.base}\n"
            f"ALTURA = {self.altura}\n"
            f"AREA = {self.area}"
        )
        
r = Retangulo()
r.altura = 4
r.base = 2
print(r.medidas)