"""
meu_array =[elemento for elemento in range(1,6)]

print(meu_array)
"""
"""
palavra = ["python", "é", "uma", "linguagem", "de", "programação"]

iniciais = [palavra[0] for palavra in palavra]

print(iniciais)
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Pegar o quadrado de cada número na lista, mas apenas se o número for ímpar

quadrados_impares = [elemento**2 for elemento in numeros if elemento % 2 != 0]

print(quadrados_impares)
