# If Else Elif

def teste():
    n = input("Digite um número inteiro de 0 a 9999: ")
    n = int(n)

def desafio22():
    nome = input("Digite o seu nome completo: ") 
    if not nome.replace(" ", "").isalpha():
        print("Informe um nome válido.")
        return desafio22()
    
    print(f"Seu nome com todas as letras em maiusculo é: {nome.upper()}")
    
    print(f"Seu nome com todas as letras em minusculo é: {nome.lower()}")
    
    print(f"Ao todo, o seu nome possui {len(nome.replace(' ', ''))} letras")
    
    print(f"Seu primeiro nome tem {len(nome.split()[0])} letras")
    
    #GABRIEL BARBOSA SOUZA -> 19 (7 + 7 + 5) letras

def desafio23():
    n = input("Digite um número inteiro de 0 a 9999: ")
    
    if not n.isdigit():
        print("Digite apenas números.")
        return desafio23()
    
    n = int(n)
    
    if n > 9999 or n < 0:
        print("Por favor, digita o número conforme os critérios.")
        return desafio23()
        
    n = f"{n:04d}"
    print(f"""
Sua unidade é : {n[3]}
Sua dezena é: {n[2]}
Sua centena é: {n[1]}
Seu milhar é: {n[0]}""")
    
def desafio24():
    cidade = input("Digite o nome de uma cidade: ").strip()
    
    if cidade.lower().startswith("santo"):
        print("Essa cidade começa com Santo!")
    else:
        print("Essa cidade não começa com Santo. 🙁")

def desafio25():
    nome = input("Digite um nome: ").strip()
    
    if "silva" in nome.lower():
        print("Esse nome tem Silva!")
    else: 
        print("Esse nome não tem Silva. 🙁")
        
def desafio26():
    frase = input("Digite uma frase: ")
    
    if not frase.replace(' ', '').isalpha():
        print("Por favor, digite um frase apenas com palavras.")
        return desafio26()

    qntd = frase.replace(' ', '').lower().count("a")
    posicao1 = frase.lower().find("a") + 1
    posicao2 = frase.lower().rfind("a") + 1
    
    
    print(f"Na frase:\n{frase}\nA letra A aparece {qntd} vezes.")
    print(f"A letra A aparece pela primeira vez na posição {posicao1}")
    print(f"A letra A aparece pela ultima vez na posição {posicao2}")

def desafio27():
    nome = input("Digite um nome completo: ")
    
    if not nome.replace(' ', '').isalpha():
        print("Por favor, digite um nome.")
        
    nome_separado = nome.split()
    
    primeiro_nome = nome_separado[0]
    ultimo_nome = nome_separado[-1] 
    
    print(f"O primeiro nome de {nome} é {primeiro_nome}")
    print(f"O primeiro nome de {nome} é {ultimo_nome}")