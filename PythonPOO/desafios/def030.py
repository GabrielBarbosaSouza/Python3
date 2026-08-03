from hashlib import sha256
from rich import print

class Credencial:
    """
Uma classe que lê e valida se uma senha em hash SHA-256 é igual a outra senha já armazenada.

Como usar:
variavel = Credencial()
variavel.senha = 'sua_senha'
variavel.validar("senha_para_validar")
    """
    
    def __init__(self):
        self.__hash_senha: str | None = None
    
    @property
    def senha(self):
        raise AttributeError("A senha não pode ser lida")
    
    @senha.setter
    def senha(self, nova_senha: str) -> None:
        self.__hash_senha = sha256(nova_senha.encode('utf-8')).hexdigest()
    
    def validar(self, senha) -> bool:
        if sha256(senha.encode('utf-8')).hexdigest() == self.__hash_senha:
            print("[green]Senha válida[/]")
        else:
            print("[red]Senha inválida[/]")
    
    
credencial = Credencial()
credencial.senha = str(input("Digite sua senha: "))
credencial.validar("teste")