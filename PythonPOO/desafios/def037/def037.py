from rich import print
from rich.panel import Panel


class Mensagem:
    def __init__(self, mensagem: str):
        self._mensagem = mensagem
        self._icone = ":speech_balloon:"
        self._tipo = {
            "border_style": "white",
            "style": "on black",
            "color-text": "white",
            "text": "AVISO"
        }
        
    
    @property
    def mensagem(self) -> str:
        return self._mensagem
    
    
    @property
    def icone(self) -> str:
        return self._icone
    
    
    @property
    def tipo(self) -> dict:
        return self._tipo
    
    
    @mensagem.setter
    def mensagem(self, nova_mensagem):
        if len(nova_mensagem) > 0:
            self._mensagem = nova_mensagem
        else:
            raise ValueError("Digite uma mensagem válida!")
        
       
    def mostrar(self):
        caixa = Panel(
                                f"[{self.tipo['color-text']}]{self.mensagem}[/]",
            title =             f"{self.icone} {self.tipo['text']} {self.icone}",
            border_style =      self.tipo['border_style'],
            style =             self.tipo['style'],
            width =             50
        )
        print(caixa)



class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._icone = ":warning:"
        self._tipo = {
            "border_style": "black",
            "style": "on yellow",
            "color-text": "black",
            "text": "ALERTA"
        }
        

class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._icone = ":x:"
        self._tipo = {
            "border_style": "dark_orange",
            "style": "on red",
            "color-text": "dark_orange",
            "text": "ERRO"
        }