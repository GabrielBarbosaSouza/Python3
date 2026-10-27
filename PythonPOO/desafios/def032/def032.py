from hashlib import sha256
from rich import print
from pwinput import pwinput

class ContaBancaria:
    """
Classe que simula uma conta bancária.

A conta possui um ID, um titular, saldo e uma senha protegida por hash.
Para realizar operações de saque é necessário informar a senha correta.
Caso nenhuma senha seja fornecida na criação da conta, o usuário será
solicitado a cadastrar uma.

Exemplos:
    conta = ContaBancaria("001", "Gabriel", 1000, "1234")

    conta.depositar(1000)
    conta.sacar(500)

Alterando a senha:
    conta.senha = "nova_senha"

Atributos:
    _id (str): Identificador da conta.
    _titular (str): Nome do titular.
    __saldo (float): Saldo atual da conta.
    __hash (str): Hash SHA-256 da senha.
    """
    
    def __init__(
        self,
        id: str,
        nome: str,
        saldo: float = 0,
        chave:str = None
    ):
        self._id: str = id
        self._titular: str = nome
        self.__saldo: float = saldo
        
        if chave is None:
            chave = self.pedir_senha()
            
        self.__hash: str = sha256(chave.encode()).hexdigest()
            
        print(f"Conta {self.id} criada com sucesso. SALDO ATUAL: R${self._saldo:.2f}")
        
    def __str__(self) -> str:
        return (
            f"Conta: {self._id}\n"
            f"Titular: {self._titular}\n"
            f"Saldo: R${self.__saldo:.2f}"
        )
    
    @property
    def nome(self) -> str:
        return self._titular
    
    @property
    def senha(self):
        raise AttributeError("A senha não pode ser lida")
    
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    @senha.setter
    def senha(self, nova_senha: str) -> None:
        self.__hash = sha256(nova_senha.encode('utf-8')).hexdigest()
        
    def pedir_senha(self):
        return str(pwinput("Digite a sua senha: "))
    
    def validar_senha(self, senha: str) -> bool:
        
        if sha256(senha.encode('utf-8')).hexdigest() == self.__hash:
            print("[green]Senha válida[/]")
            return True
        else:
            print("[red]Senha inválida[/]")
            return False
    
    def depositar(self, valor: float) -> None:
        
        if valor <= 0:
            print("[red]Valor inválido[/]")
            return
        
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} autorizado na conta ID-{self._id}")
        
    def sacar(self, valor: float) -> None:
        
        if not self.validar_senha(self.pedir_senha()):
            print("[red]Operação cancelada[/]")
            return

        if valor <= 0:
            print(f"[red]Valor inválido[/]")
            return

        if valor > self.__saldo:
            print("[red]Saldo insuficiente[/]")
            return

        self.__saldo -= valor
        print(f"[green]Saque de R${valor:.2f} autorizado na conta ID-{self._id}[/]")

            
cc = ContaBancaria(000, "Marcelo", 1000, "oi")
cc.depositar(1000)
cc.sacar(500)