from rich import print, inspect
from rich.traceback import install
from rich.panel import Panel
from abc import ABC, abstractmethod

install()

class Funcionario(ABC):
    """

Classe base para diferentes tipos de funcionários.
Calcula e analisa salários de funcionários horistas e mensalistas.


Para usar ela use:
variavel1 = Horista("nome_da_pessoa", valor_da_hora, quantas_horas_trabalhou)
variavel1.analisar_salario()

variavel2 = Mensalista("nome_da_pessoa", salario_bruto)
variavel2.analisar_salario()
    """
    
    SALARIO_MINIMO: float = 1_612
    INSS: float = 7.5
    
    def __init__(
        self,
        nome: str | None = None
    ):
        
        self.nome = nome
        self.salario_bruto = 0.0
        self.salario = 0.0
    
    @abstractmethod
    def calcular_salario(self) -> float:
        pass
        
    def analisar_salario(self) -> None:
        salario = self.calcular_salario()
        
        base = salario / self.SALARIO_MINIMO
        mensagem = f"O salário de [yellow]{self.nome}[/] [underline white]({self.__class__.__name__})[/] é de [yellow]R${salario:.2f}[/] e corresponde a [yellow]{(base):.1f}[/] salários mínimos"
        print(
            Panel(
                mensagem,
                title="Análise de Salário",
                width=40
            )
        )



class Horista(Funcionario):
    def __init__(
        self,
        nome: str | None = None,
        valor_hora: float = 7.37,
        quantidade_horas: float = 220.0
    ):

        super().__init__(nome)
        self.valor_hora: float = valor_hora
        self.horas_trabalhadas: float = quantidade_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas
    
    def calcular_salario(self) -> float:
        self.salario = self.salario_bruto - (self.salario_bruto * self.INSS / 100)
        return self.salario
    
    
class Mensalista(Funcionario):
    def __init__(
        self,
        nome: str | None = None,
        salario_bruto: float = Funcionario.SALARIO_MINIMO
    ):
        super().__init__(nome)
        self.salario_bruto = salario_bruto
        
    def calcular_salario(self) -> float:
        self.salario = self.salario_bruto - (self.salario_bruto * self.INSS / 100)
        return self.salario
    
    
horista1 = Horista(
        nome="Gabriel",
        valor_hora=12,
        quantidade_horas=190
    )

mensalista1 = Mensalista(
    nome="Nicole",
    salario_bruto=8500
    )

horista1.analisar_salario()
mensalista1.analisar_salario()