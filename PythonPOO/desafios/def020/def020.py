from rich import print
from rich.panel import Panel
from rich.traceback import install

install()

class Gamer:
    """
Uma classe que permite o usuário a cadastrar um gamer, adicionar jogos de um gamer e listar uma ficha completa do gamer.

Para usar a classe use:
variavel = Gamer(nome, nickname)

variavel.add_jogos("jogo") -> PARA ADICIONAR UM JOGO
variavel.mostrar_ficha() -> PARA MOSTRAR A FICHA COMPLETA DO JOGADOR
    """
    
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nickname = nickname
        self.jogos_favoritos = []

    def add_jogos(self, jogo):
        self.jogos_favoritos.append(jogo)
        print(f"O jogo [blue]{jogo}[/] foi adicionado com sucesso!")

    def mostrar_jogos(self):
        jogos = ""
        for jogo in self.jogos_favoritos:
            jogos += f"\n:video_game: [blue]{jogo}[/]"
        return jogos

    def mostrar_ficha(self):
        print(
            Panel(
                f"Nome real: {self.nome}\nJogos favoritos:{self.mostrar_jogos()}",
                title=f"Jogador - {self.nickname}",
                width=50,
                border_style="cyan",
            )
        )


jogador1 = Gamer("Gabriel", "oBiel")

jogador1.add_jogos("Spiderman 2")
jogador1.add_jogos("Roblox")
jogador1.add_jogos("Minecraft")

jogador1.mostrar_ficha()

jogador2 = Gamer("Nicole", "hanna_hana20")

jogador2.add_jogos("Candy Crush")
jogador2.add_jogos("Roblox")
jogador2.add_jogos("Clash Royale")

jogador2.mostrar_ficha()