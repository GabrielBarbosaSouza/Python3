import sqlite3
from datetime import date

busca = input("Quem você está procurando? ").strip()
hoje = date.today()
try:
    with sqlite3.connect("exercicios/ex018/meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0
        linha = "-" * 30
        
        print(linha)
        for total, amigo in enumerate(cursor, start=1):
            nome = amigo['nome']
            nascimento = amigo['nascimento']
            
            try:
                data_nascimento = date.fromisoformat(nascimento)
            except (ValueError, TypeError):
                print(f"Data de nascimento do amigo {nome} inválida: {nascimento}")
                continue
            
            if hoje >= data_nascimento:
                ja_passou = (hoje.month, hoje.day) >= (data_nascimento.month, data_nascimento.day)
                idade = hoje.year - data_nascimento.year - (0 if ja_passou else 1)
                
                print(f"{nome} nasceu em {data_nascimento:%d/%m/%Y} e tem {idade} anos")
            else:
                print(f"Data de nascimento do amigo {nome} ({data_nascimento:%d/%m/%Y}) é maior que a data de hoje ({hoje:%d/%m/%Y})")
        print(linha)
        
        if total == 1:    
            print(f"Foram encontrados {total} amigo com a busca '{busca}'.")
        elif total == 0:
            print(f"Não foi encontrado nenhum amigo com a busca '{busca}'.")
        else:    
            print(f"Foram encontrados {total} amigos com a busca '{busca}'.")
            
except sqlite3.Error as erro:
    print(f"\nErro no banco de dados: {erro}")
except Exception as erro:
    print(f"\nAlgo deu errado. ERRO: {erro}")
    