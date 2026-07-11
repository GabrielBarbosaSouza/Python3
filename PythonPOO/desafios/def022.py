from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class ControleRemoto:
    canal_min = 1
    canal_max = 5

    volume_min = 0
    volume_max = 5

    def __init__(self, canal=1, volume=1):
        self.status = False
        self.canal_atual = canal
        self.volume_atual = volume

    def ligaDesliga_tv(self):
        self.status = not self.status

    def mostrar_tv(self):

        if not self.status:
            print(
                Panel(
                    ":prohibited: [red]A TV está desligada![/]",
                    title="[ TV ]",
                    width=40
                )
            )
            return

        conteudo = "CANAL = "

        for canal in range(self.canal_min, self.canal_max + 1):
            if canal == self.canal_atual:
                conteudo += f"[black on yellow] {canal} [/] "
            else:
                conteudo += f" {canal} "

        conteudo += "\nVOLUME = "

        for volume in range(self.volume_min, self.volume_max):
            if volume <= self.volume_atual-1:
                conteudo += "[black on cyan] [/]"
            else:
                conteudo += "[black on white] [/]"

        print(Panel(conteudo, title="[ TV ]", width=40))

    def aumentar_canal(self):
        if not self.status:
            print("\n" * 5)
            print("[red]Ligue a TV primeiro![/] (Digite @ para ligar)")
            return

        if self.canal_atual == self.canal_max:
            self.canal_atual = self.canal_min
        else:
            self.canal_atual += 1

    def diminuir_canal(self):
        if not self.status:
            print("\n" * 5)
            print("[red]Ligue a TV primeiro![/] (Digite @ para ligar)")
            return

        if self.canal_atual == self.canal_min:
            self.canal_atual = self.canal_max
        else:
            self.canal_atual -= 1

    def aumentar_volume(self):
        if not self.status:
            print("\n" * 5)
            print("[red]Ligue a TV primeiro![/] (Digite @ para ligar)")
            return

        if self.volume_atual < self.volume_max:
            self.volume_atual += 1

    def diminuir_volume(self):
        if not self.status:
            print("\n" * 5)
            print("[red]Ligue a TV primeiro![/] (Digite @ para ligar)")
            return

        if self.volume_atual > self.volume_min:
            self.volume_atual -= 1

    def processar_comando(self, comando):
        match comando:
            case "@":
                self.ligaDesliga_tv()
            case ">":
                self.aumentar_canal()
            case "<":
                self.diminuir_canal()
            case "+":
                self.aumentar_volume()
            case "-":
                self.diminuir_volume()
            case _:
                print("\n" * 5)
                print("[red]Digite uma opção válida![/] (@ para ligar a TV, < para voltar o canal, > para avançar o canal, + para aumentar o volume, - para diminuir o volume e 0 para sair do programa.)")


tv = ControleRemoto()

while True:
    tv.mostrar_tv()
    escolha = input(f"< CH{tv.canal_atual} >     - VOL{tv.volume_atual} +     : ")
    if escolha == "0":
        print("[bold green]Volte sempre![/] 🤖")
        break

    tv.processar_comando(escolha)