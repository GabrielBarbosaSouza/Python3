import sqlite3

busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect("exercicios/ex018/meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cursor = banco.cursor()

        cursor.execute(f"SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0
        for total, amigo in enumerate(cursor, start=1):
            print(f"{amigo['nome']} - {amigo['nascimento']}")
            
        # lista = cursor.fetchall()
        # print(lista)
            
except sqlite3.Error as erro:
    print(f"Erro no banco de dados: {erro}")
except Exception as erro:
    print(f"Algo deu errado. ERRO: {erro}")