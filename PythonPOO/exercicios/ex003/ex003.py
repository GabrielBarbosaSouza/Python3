from rich import *

class ContaBancaria:
    """
Uma classe que cria uma conta bancária para possíveis saques e/ou depositos.
    """
    
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
    
    def __getstate__(self):
        return f"id: {self.id}, titular: {self.titular}, saldo: {self.saldo}"
      
    def __str__(self):
        return f"A conta de ID {self.id} de {self.titular} tem um saldo de R${self.saldo:.2f} reais."
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} reais \033[32mautorizado\033[m com sucesso.")
    
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} reais \033[31mAUTORIZADO\033[m com sucesso.")
        else: print(f"Saque de R${valor:.2f} reais \033[31mRECUSADO\033[m.\nVocê não pode sacar um valor maior do que o seu saldo atual.")
    
conta1 = ContaBancaria(67, "Gabriel", 2000)
# print(conta1.__doc__)

# conta1.depositar(300) # 2300 reais
# conta1.sacar(1000) # 1300 reais
# print(conta1)

inspect(conta1)