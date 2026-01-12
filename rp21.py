# Dado um array meu_arrayzinho de tamanho n, retorne o elemento majoritário.
# O elemento majoritário é aquele que aparece mais de [n/2] vezes.
# Você pode assumir que o elemento majoritário sempre existe no array.

array = [3,2,3]
majoritario = len(array) / 2

# print(majoritario)

dict = {}

for i in array:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for chave, valor in dict.items():
    if valor >= majoritario:
        print(chave)


