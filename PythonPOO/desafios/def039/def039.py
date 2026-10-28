from abc import ABC
from rich import print
import re

class Validador(ABC):
    padrao: str
    
    def validar_dado(self, valor: str) -> None:
        """
        Regras que a função de usuário valida:
            - deve ter 5 a 20 caracteres
            - apenas letras minúsculas
            - aceita números
            - aceita simbolo de sublinado
        
        Regras que a função de senha valida:
            - pelo menos 8 caracteres
            - pelo menos uma letra maiúscula
            - pelo menos um simbolo
          
        Regras que a função de e-mail valida:
            - apenas um '@'
            - pode conter letras, números e alguns simbolos
            - os domínios contém pontos
            - o TLD encerra com ponto e pelo menos 2 letras   
        """
        
        nome_classe = type(self).__name__
        valido = bool(re.fullmatch(self.padrao, valor))
        
        if valido:
            print(f"{nome_classe} {valor} é [green]válido[/].")
        else:    
            print(f"{nome_classe} {valor} é [red]inválido[/].")
    
    
class Usuario(Validador):
    padrao = r"[a-z0-9_]{5,20}"
                   
    
class Senha(Validador):
    padrao = r"(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{8,}"
    
    
class Email(Validador):
    padrao = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
            
            
def validar_dado(objeto: Validador, valor: str) -> None:
    objeto.validar_dado(valor)