import random

#desafio 66 é o mesmo do desafio 64

def desafio67():
    while True: 
        print('=-'*20)
        n = input("Digite o número em que você deseja ver a tabuada: ")
        
        n = int(n)
        
        if n < 0:
            break 
        
        for i in range(1,11):
            print(f'{n} x {i} = {n*i}')
        
    print('Programa Tabuada terminado. Volte sempre!')
       
def desafio68():
    print('=-'*15)
    print('\033[036mPAR OU IMPAR\033[0m')
    print('=-'*15)
    
    contador = 0
    
    while True:
        pcNum = random.randint(1, 10)
        userNum = input('Digite um número: ')
        if not userNum.isnumeric():
            print('Digite um número inteiro!')
            continue

        userNum = int(userNum)
        
        userChoice = input('Par ou Impar?(P/I): ')
        userChoice = userChoice.lower()

        while not userChoice == "p" and not userChoice == "i":
            userChoice = input('Favor escolha apenas "P" ou "I": ')
        
        soma = userNum + pcNum
        
        print('-'*30)
        print(f'Você escolheu {userNum} e o computador {pcNum}. A soma total foi de {soma}')
        
        if userChoice == 'p' and soma % 2 == 0:
            print('VOCÊ VENCEU!')
            contador += 1
            print('Vamos jogar novamente...')
            continue
        elif userChoice == 'i' and soma % 2 != 0:
            print('-'*30)
            print('\033[032mVOCÊ VENCEU!\033[0m')
            contador += 1
            print('Vamos jogar novamente...\n')
            continue
        else:
            print('-'*30)
            print(f'\033[031mGAME OVER!!\033[0m Você venceu {contador} vezes.')
            break

def desafio69():
    maiorDeIdade = 0
    homens = 0
    mulheres = 0
    
    while True:  
        texto = 'CADASTRO DE PESSOAS'
        print('-'*30)
        print(f'\033[033m{texto.center(30)}\033[0m')
        print('-'*30)
        
        idade = input('\nDigite a idade dessa pessoa: ')
        while not idade.isnumeric():
            idade = input('Digite um número inteiro!: ')
        idade = int(idade)
            
        if idade >= 18:
            maiorDeIdade += 1
            
        sexo = input('Digite o sexo dessa pessoa (\033[034mM\033[0m/\033[035mF\033[0m): ').lower()
        while sexo not in ('m', 'f'):
            sexo = input('Digite "\033[034mM\033[0m" para masculino e "\033[035mF\033[0m" para feminino: ').lower()
            
        if sexo == 'm':
            homens += 1
        
        if sexo == 'f' and idade < 20:
            mulheres += 1
                
        repetir = input('\nQuer continuar cadastrando? (\033[032mS\033[0m/\033[031mN\033[033m\033[0m): ')
        repetir = repetir.lower()
        
        while repetir not in('s', 'n'):
            repetir = input('Digite apenas "S" ou "N"').lower()
        
        if repetir == 'n':
            break
        
    print('-'*30)
    print(f'Você cadastrou {maiorDeIdade} pessoas maiores de idade.')
    print(f'Você cadastrou {homens} homens.')
    print(f'Você cadastrou {mulheres} mulheres com menos de 20 anos.\n')
    
    
#A partir do desafio70 eu começei a escrever TUDO em inglês, com o principal objetivo sendo melhorar o meu inglês
def desafio70():
    totalSum = 0
    productsOver1000 = 0
    cheapestPrice = float('inf')
    cheapestProduct = ''
    
    while True:
        tittle = 'PRODUCT REGISTRATION'
        print('-'*30)
        print(f'\033[33m{tittle.center(30)}\033[0m')
        print('-'*30)
        
        productName = input('Enter the product name: ')
        
        while True:
            priceInput = input('Enter a price for this product: ').replace(',', '.')
            if priceInput.replace('.', '', 1).isdigit():
                price = float(priceInput)
                totalSum += price
                break
            else:
                price = input('Please, input a valid number!: ')
        
        if price > 1000:
            productsOver1000 += 1
        
        if price < cheapestPrice:
            cheapestPrice = price
            cheapestProduct = productName
        
        while True:
            continueChoice = input('Do you want to continue? (Y/N): ').lower()
            if continueChoice in ('y', 'n'):
              break
            else:
                print('Please, input "Y" for Yes or "N" for No.')
            
        if continueChoice == 'n':
            break
               
    print(f'Total spent: R${totalSum:.2f}')
    print(f'{productsOver1000} products are more expensive than R$1000.00')
    print(f'{cheapestProduct} is the cheapest product.')

def desafio71():
    tittle = "BIEL'S BANK"
    print('='*30)
    print(f'\033[32m{tittle.center(30)}\033[m')
    print('='*30)
    
    banknote50 = 0
    banknote20 = 0
    banknote10 = 0
    banknote1 = 0
    
    value = start_value = input('Enter a value to cash: ')
    while True:
        if not value.isnumeric():
            value = input('Enter a int value!: ')
        else:
            value = int(value)
            break

    start_value = value
        
    while value >= 50:
        value -= 50 
        banknote50 += 1
        
    while value >= 20:
        value -= 20 
        banknote20 += 1
    
    while value >= 10:
        value -= 10 
        banknote10 += 1
    
    while value >= 1:
        value -= 1
        banknote11 += 1
    
    if banknote50 > 0:
        print(f'{banknote50} banknotes of R$50 were used for {start_value}')
    if banknote20 > 0:
        print(f'{banknote20} banknotes of R$20 were used for {start_value}')
    if banknote10 > 0:
        print(f'{banknote10} banknotes of R$10 were used for {start_value}')
    if banknote1 > 0:
        print(f'{banknote1} banknotes of R$1 were used for ${start_value}')
            
    print('-'*30)
    print('Come back soon!\n')
desafio71()

