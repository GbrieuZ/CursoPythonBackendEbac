# Dada um array de números inteiros, cada elementyo aparece duas vezes, exceto um. Encontre esse um.

array = [2,2,6,6,9,9,12,12,45,45,300,1,1]

dicionario = {}

for i in array:
    if i not in dicionario:
        dicionario[i] = 1
    else:
        dicionario[i] += 1

for chave, valor in dicionario.items():
    if valor == 1:
        print(chave)
