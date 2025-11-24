# - Tabuada: Receba um número e exiba a tabuada de 1 a 10 para ele.

# 1. Receber o número

num = float(input('Digite um numero para ver a sua tabuáda: '))

# 2. Criar a lógica para mostrar a tabuáda

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
