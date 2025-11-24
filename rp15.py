# Dado um array meu_arrayzinho contendo n números distintos no intervalo [0, n],
# retorne o único número no intervalo que está faltando no array.

array = [0,1,2,3,4,5,6,8,9,10]



tamanho_array = len(array)
soma_valores = sum(array)

soma_total = (tamanho_array * (tamanho_array + 1)) // 2

print(soma_total - soma_valores)