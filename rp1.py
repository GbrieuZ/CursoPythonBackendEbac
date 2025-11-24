# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# 1. Preciso receber esses números separadamente

num1, num2, num3 = map(int, input().split())

# 2. Criar uma lógica para ver quem é o segundo maior

meu_array = []

meu_array.append(num1)
meu_array.append(num2)
meu_array.append(num3)

meu_array.sort()

# 3. Mostrar na tela quem é o vencedor, ou seja, quem é o segundo maior

print(meu_array[1])