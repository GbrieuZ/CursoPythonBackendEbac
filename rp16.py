# Dado um array de inteiros, um inteiro sortudo é um inteiro que tem um frequencia no array igual ao seu valor.

array = [1,2,3,3,4,4,5,6,7,1,2]

dicionario = {}

for i in array:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

for chave, valor in dicionario.items():
    if chave == valor:
        print(chave)