from abc import ABC, abstractmethod

BYTES_PARA_MB = 1_048_576

class Arquivo(ABC):
    def __init__(
        self,
        nome: str,
        extensao: str,
        tamanho: int
    ):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho
    
    
    @abstractmethod
    def abrir(self):
        pass
    
    
    @property
    def extensao(self):
        return self._extensao
    
    
    @extensao.setter
    def extensao(self, nova_extensao):
        formatos = [
            'pdf',
            'doc'
        ]
        
        if nova_extensao.lower().strip() not in formatos:
            raise AttributeError("O arquivo está em um formato não suportado (apenas .pdf e .doc.)") 
    
    
    def nome_completo(self):
        return f"{self.nome}.{self.extensao} ({self.tamanho / BYTES_PARA_MB:.2f}MB)"
        
        
    def __str__(self):
        return f"Arquivo: {self.nome_completo()}"
    
    
class PDF(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo()}'...")


class DOC(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, "doc", tamanho)
        
    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo()}'...")
