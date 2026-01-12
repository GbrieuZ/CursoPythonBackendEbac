# Dado um array meu_arrayzinho. Definimos uma soma acumulada de um array como runningSum[i] = sum(meu_arrayzinho[0]+meu_arrayzinho[i]).
# Retorne a soma acumulada de meu_arrayzinho.

# Explicação: A soma acumulada é obtida da seguinte forma: [1, 1+2, 1+2+3, 1+2+3+4].

array = [1,2,3,4]
novo = []

contador = 0

for i in array:
    contador += i
    novo.append(contador)

print(novo)