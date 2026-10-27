from rich import print
from rich.traceback import install

install()

class Livro:
    """
Uma classe que, com o título e n° de páginas, faz a leitura de um livro, permitindo o usuário a folhear o livro (exceto se ultrapassar a quantidade mínima e máxima de páginas que o livro tem)

Para usar a classe, faça:
variavel = Livro(titulo, n° de páginas)

print(variavel.avancarPaginas(n° de páginas)) -> PARA AVANÇAR
print(variavel.voltarPaginas(n° de páginas)) -> PARA VOLTAR

    """
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagAtual = 1
        
        # return f"Você abriu o livro '{self.titulo}' que possui {self.paginas} páginas. Você está na página 1!"
    
    def avancarPaginas(self, numero):
        for i in range(1, numero + 1):
            self.pagAtual += 1
            
            if i >= self.paginas:
                print("[red]Opa! Esse livro tem apenas 20 páginas.", end=' ')
                break
            else:
                print(f"Pag{self.pagAtual} :right_arrow: ", end=' ')

        return f"[blue]Você avançou {numero} páginas e agora está na [yellow]página {self.pagAtual}![/]"

    def voltarPaginas(self, numero):
        for _ in range(numero + 1, 1, -1):
            self.pagAtual -= 1
            
            if 1 > self.pagAtual:
                print("[red]Opa! Você já está no inicio do livro.", end=' ')
                self.pagAtual += 1
                break
            else:
                print(f"Pag{self.pagAtual} :right_arrow: ", end=' ')

        return f"[blue]Você voltou {numero} páginas e agora está na [yellow]página {self.pagAtual}![/]"
        
        
l1 = Livro("O Pequeno Principe", 20)

print(l1.avancarPaginas(19))
print(l1.voltarPaginas(2))
print(l1.voltarPaginas(18))