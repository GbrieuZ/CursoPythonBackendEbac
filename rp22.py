# Retorne a média de todos os salárioos, com exceção do menor e maior

salario = [1000, 6000, 13000, 9000, 7000, 1350, 5000, 4500]

salario_juntos = sorted(salario)
# print(salario_juntos)

salario_juntos.remove(salario_juntos[0])
salario_juntos.remove(salario_juntos[-1])

# print(salario_juntos)

media = 0

for salario in salario_juntos:
    media += salario



print(media // len(salario_juntos))