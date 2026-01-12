def conuter_function():
    yield 1
    yield 2
    yield 

# O yield  pega um espaço na memória e aloca-lo para guarda-lo e executar a tarefa.
# Executanto tarefa uma de cada vez sob comando.

contador = conuter_function()

print(next(contador))
print(next(contador))
print(next(contador))
