# Receba uma lista de palavras e ordene-as em ordem alfabéfica

# 1. Criar um array vazio para receber essas palavras

meu_array = []

# 2. Definir uma quantidade de palavras

# Serão 5 palavras

# 3. Criar a lógica para receber essas palavras e adicionar dentro do array

for i in range(1, 6):
    palavra = input('Digite algumas palavra: ')
    print("Palavra sendo adicionada")
    meu_array.append(palavra)

# 4. Ordenar a lista

meu_array.sort()

# 5. Printar na tela list

print(meu_array)