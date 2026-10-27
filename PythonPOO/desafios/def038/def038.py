class Produto:
    def __init__(
        self,
        nome: str,
        preco: float = 0
    ):
        self.nome = nome
        self.preco = preco
    
     
    def __str__(self) -> str:
        return f"{self.nome} ({preco_formatado(self.preco)})"
    
    
class Carrinho:
    def __init__(
        self,
        produtos: list = None
    ):
        self.produtos = produtos if produtos else []
        
        
    @property
    def total(self):
        soma = sum(produto.preco for produto in self.produtos)
        return preco_formatado(soma)
        
      
    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        if isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválido. Adicione apenas produtos ou carrinhos.")
        
        
    def __str__(self) -> str:
        linha = '-' * 35
        items_carrinho = "\n".join(str(produto) for produto in self.produtos)
        return f"{linha}\n{items_carrinho}\n{linha}\nTotal: {self.total}"
      
       
def preco_formatado(preco: float = 0) -> str:
    import locale
    try:
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    except locale.Error:
        locale.setlocale(locale.LC_ALL, "")
    return locale.currency(preco, grouping=True)
        