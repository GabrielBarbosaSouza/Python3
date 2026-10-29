from datetime import date

hoje = date.today()

teste = (hoje.month, hoje.day) <= (5, 10)

print(teste)