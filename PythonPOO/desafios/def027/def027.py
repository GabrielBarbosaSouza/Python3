from random import randint, choice
from rich import print
from rich.traceback import install
from abc import  ABC, abstractmethod

install()

class Personagem(ABC):
    """

Classe que simula um personagem para RPG. Tem atributos de classe para armas de curta distância e longa, sendo usadas de acordo com a Classe do personagem que você quer.
Ex: Sayajin usa armas de perto, já um Mago usa armas de longe.

Como usar:
variavel = Sayajin("nome", vida)
variavel.atacar(alvo)
variavel.curar()

O dano do ataque e a quantidade de vida curada são aleatórias, variando de 1 até a quantidade da vida máxima da vida que foi atribuida a um personagem.

    """
    
    ARMAS_PERTO = [
        "[red]um Machado Duplo[/]",
        "[red]uma Foice[/]",
        "[red]um Soco Estelar[/]",
        "[red]uma Faca Mortal[/]"
    ]
    
    ARMAS_LONGE = [
        "[yellow]um Feitiço de Sombras[/]",
        "[yellow]um Tiro de Luz[/]",
        "[yellow]um Sopro Mágico[/]",
        "[yellow]um Chicote Galático[/]"
    ]
    
    def __init__(
        self,
        nome: str,
        vida: int = 1000,
    ):
        self.nome: str = nome
        self.vida: int = vida
        self.vida_maxima: int = vida        
    
    def receber_dano(self, dano: int):
        self.vida -= dano
        
        if self.vida > 0:
            print(f"[red]-{dano}[/] de vida. [underline]VIDA ATUAL: {self.vida}[/]\n")
        else:
            self.vida = 0
            print(f"[red]-{dano}[/] de vida. [bold red]Você está morto.[/]")
            
    def atacar(self, alvo: "Personagem", forca: int = 100):
        arma = choice(self.ARMAS_PERTO) if isinstance(self, Sayajin) else choice(self.ARMAS_LONGE)
        
        print(f"Jogador {self.nome} ({self.vida} de HP) atacou {alvo.nome} ({alvo.vida} de HP) com {arma} de força {forca}...")
        alvo.receber_dano(randint(1, forca))
            
        if alvo.vida == 0:
            print(f"[bold green]Jogador {self.nome} ({self.vida} de HP) derrotou Jogador {alvo.nome} ({alvo.vida} de HP)![/]")
    
    @abstractmethod
    def curar(self):
        pass
    

class Sayajin(Personagem):
    def curar(self):
        cura = randint(1, 100)
        self.vida = min(self.vida + cura, self.vida_maxima)
        
        print(f"{self.nome} - {self.__class__.__name__} concentrou sua dor em um poder gigantesco...")
                    
        if self.vida >= self.vida_maxima:
            print(f"[green]+{cura}[/] de vida. [underline]VIDA CURADA AO MÁXIMO!: {self.vida}[/]\n")
        else:
            print(f"[green]+{cura}[/] de vida. [underline]VIDA ATUAL: {self.vida}[/]\n")

   
class Mago(Personagem):
    def curar(self):
        cura = randint(1, 100)
        self.vida = min(self.vida + cura, self.vida_maxima)
        
        print(f"{self.nome} envolveu o seu corpo com uma aura curadora. O {self.__class__.__name__} curou [green]{cura}[/] de sua vida!...")
        
        if self.vida >= self.vida_maxima:
            print(f"[green]+{cura}[/] de vida. [underline]VIDA CURADA AO MÁXIMO!: {self.vida}[/]\n")
        else:
            print(f"[green]+{cura}[/] de vida. [underline]VIDA ATUAL: {self.vida}[/]\n")
    
    
p1 = Sayajin("Marco", 5000)
p2 = Mago("Biel")

p1.atacar(p2)
p2.curar()