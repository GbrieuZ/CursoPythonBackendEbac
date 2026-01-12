# Dado um array, retorne verdadeiro se algum valor aparece pelo menos 2 vezes no array
# E retorne False se cada elemento for distinto.

array = [1,1,1,3,3,4,3,4,2]

dict = {}


for i in array:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1

for chave, valor in dict.items():
    if valor >= 2:
        print(True)
    else:
        print(False)