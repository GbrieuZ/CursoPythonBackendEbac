# Você recebe um array de números inteiros meu_arrayzinho.
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos únicos de meu_arrayzinho.



meu_arrayzinho = [1,2,3,3,4,4,5,5,6,6,6]

meu_dicionario = {}



for i in meu_arrayzinho:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

soma_das_chaves = 0

for chave, valor in meu_dicionario.items():
    if valor == 1:
        soma_das_chaves += chave

print(soma_das_chaves)
