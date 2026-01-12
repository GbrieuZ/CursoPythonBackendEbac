# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte caso é válido:

# Todaas as letras desta palavra são maiúsculas, como EUA.

# Dada uma palavra de strig, retorne verdadeiro se o uso de letras maiúsculas está certo.

palavra = input("Digite uma palavra: ")
contador = 0


for letra in palavra:
    if letra.isupper():
        contador += 1

if contador == len(palavra):
    print("Passou no teste!")
else:
    print("Reprovado!")