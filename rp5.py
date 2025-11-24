# - Soma de 1 a N: Receba um número N e exiba a soma de todos os números de 1 até N.

# 1. Recebendo número N:

n = int(input("Digite um número: "))

# 2. Entender a lógica da soma

# 3. Exibir a soma de todos os números de 1 até esse número

soma = 0

for i in range(1, n + 1):
    soma += i  # soma = soma + 1

print(soma)
