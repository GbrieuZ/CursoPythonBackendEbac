operadores = {
    1: ("Adição (+)", lambda num1, num2: num1 + num2),
    2: ("Subtração (-)", lambda num1, num2: num1 - num2),
    3: ("Multiplicação (*)", lambda num1, num2: num1 * num2),
    4: ("Divisão (/)", lambda num1, num2: num1 / num2),
    0: ("Sair", None)
}

print("Selecione a operação:")
for chave, (nome, _) in operadores.items():
    print(f"{chave}: {nome}")
while True:
    try:
        escolha = int(input("Digite o número da operação desejada: "))
        if escolha in operadores:
            if escolha == 0:
                print("Saindo da calculadora. Até mais!")
                break
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            operacao = operadores[escolha][1]
            resultado = operacao(num1, num2)
            print(f"O resultado da {operadores[escolha][0]} entre {num1} e {num2} é: {resultado}")
           
        else:
            print("Operação inválida. Tente novamente.")
    except ZeroDivisionError:
        resetar = input("Erro: Divisão por zero não é permitida. Deseja resetar a calculadora? (S/N): ")
        if resetar.lower() == "s":
            continue
        elif resetar.lower() == "n":
            print("Saindo da calculadora. Até mais!")
            break
        else:
            print("Insira uma opção válida (S/N).")
            continue
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.")
