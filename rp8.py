# Receba um número e determine se ele é um palíndromo (lê-se igual de frente para trás).

# 1. Recebendo o número:

num = int(input('Digite um numero: '))

# 2. Determinar se é um palíndromo
# 3. Retornar se é ou não é

minha_sting = str(num)

if minha_sting == minha_sting[::-1]:
    print("É palindromo")
else:
    print("Não é palindromo")

