def desafio05():
    n = input("Fale um número para ver o seu sucessor e antecessor: ")
    if not n.isnumeric():
        print("Por favor, digite um número válido.")
        return desafio05()
    
    n = int(n)
    print(f"O seu sucessor é: {n+1}\nO seu antecessor é: {n-1}")

def desafio06():
    n = input("Digite um número para ver o dobro, triplo e a sua raiz quadrada: ")
    if not n.isnumeric():
        print("Por favor, digite um número válido.")
        return desafio06()
    
    n = int(n)
    print(f"Seu dobro é: {n*2} Seu triplo é: {n*3} Sua raiz quadrada é: {n**(1/2)}")
          
def desafio07():
    print("Para calcular a média das suas notas, informe as suas duas notas a baixo:")
    n1 = input("Primeira nota: ")
    n2 = input("Segunda nota: ")
    if not n1.isnumeric() or not n2.isnumeric():
        print("Por favor, digite uma nota numérica.")
        return desafio07()
    
    n1 = float(n1)
    n2 = float(n2)
    m = (n1 + n2) / 2
    print(f"Sua média entre {n1} e {n2} é {m}")
    
def desafio08():
    m = input("Informe o valor em metros para convertê-lo em centímetros e milímetros: ")
    if not m.isnumeric():
        print("Por favor, informe um valor numérico.")
        return desafio08()
    
    m = float(m)
    cm = m*100
    mm = m*1000
    print(f"O valor em centímetros é: {cm} cm\nO valor em milímetros é: {mm} mm")
    
def desafio09():
    n = input("Digite um número para ver a tabuada: ")
    if not n.isnumeric():
        print("Por favor, digite um número válido.")
        return desafio09()
        
    n = int(n) 
    print(f"Tabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def desafio10():
    r = input("Para saber quandos dolares você pode ter, informe a quantidade de reais você tem em sua carteira para a conversão: ")
    if not r.isnumeric():
        print("Por favor, digite um número válido.")
        return desafio10()
    
    r = float(r)
    d = r * 3.27
    print(f"Com R${r} você pode comprar U$${d} dólares.")
    
def desafio11():
    l = input("Informe a largura da parede: ")
    a = input("Informe a altura da parede: ")
    if not l.isnumeric() or not a.isnumeric():
        print("Por favor, informe valores numéricos válidos.")
        return desafio11()
    
    area = float(l) * float(a)
    area_tinta = area / 2
    
    print(f"\nConsiderando que cada lata de tinta possui 2L\nVocê precisará de {area_tinta} litros de tinta para pintar uma parede de {area} m².")

def desafio12():
    produto = input("Informe o preço do produto: R$")
    
    if not produto.replace(',', '.', 1).replace('.', '', 1).isdigit():
        print("Por favor, informe um valor numérico válido.")
        return desafio12()
    
    produto = float(produto.replace(',', '.', 1))
    produto_final = produto - (produto * 0.05)
    print(f"Com o desconto de 5%, o novo preço do produto é: R${produto_final}")

def desafio13():
    salario = input("Para calcular o seu novo salário com 15% de aumento, informe o seu salário atual: R$")
    if not salario.replace(',', '.', 1).replace('.', '', 1).isdigit():
        print("Por favor, informe um valor numérico válido.")
        return desafio13()
    
    salario = float(salario.replace(',', '.', 1))
    novo_salario = salario * 1.15
    print(f"Com o aumento de 15%, o seu novo salário será: R${novo_salario}")
    
