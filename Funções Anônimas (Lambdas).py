"""
def soma(a, b):
    return a + b

print(soma(3, 5))  # Saída: 8
"""

""""
# Função anônima (lambda) para somar dois números

soma= lambda a, b: a + b
print(soma(3, 5))  # Saída: 8
"""

"""
Use def (Normal): Para qualquer função que precise de múltiplas linhas de código, 
lógica complexa, documentação, ou que você planeja reutilizar em várias partes do seu código.

Use lambda (Anônima): Quando você precisa de uma função simples de uma linha para ser usada 
como argumento imediato para uma função de ordem superior, como uma chave de ordenação (key) ou um filtro.
"""

array = [1, 2, 3, 4, 5]

duplicados = map(lambda numero: numero * 2, array)

print(list(duplicados))  # Saída: [2, 4, 6, 8, 10]