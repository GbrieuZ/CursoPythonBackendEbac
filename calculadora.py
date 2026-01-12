# Função das operações

def calculo():
    if operacao > 4 or operacao < 1:
        print("Escolha uma operação exitente na lista")
    elif operacao == 1:
        print("Escolheu 'Soma', o resultado é: ", n1 + n2)
    elif operacao == 2:
        print("Escolheu 'Subtração', o resultado é: ", n1 - n2)
    elif operacao == 3:
        print("Escolheu 'Multiplicação', o resultado é: ", n1 * n2)
    elif operacao == 4:
        print("Escolheu 'Divisão', o resultado é: ", n1 / n2)

#Apresentação das opções

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#Entrada de dados

operacao = int(input("Digite o número correspondente a operação desejada: "))

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calculo()

# Repetição com loop

while True:
    repetir = input("Deseja realizar outra operação? (sim/não): ")
    if repetir.lower() == "sim":
        operacao = int(input("Digite o número correspondente a operação desejada: "))
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        calculo()
    elif repetir.lower() == "não":
        print("Fim do programa, adeus")
        break
    else:
        print("Digite 'sim' ou 'não'.")

