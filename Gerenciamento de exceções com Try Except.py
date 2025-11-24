"""
try: # Tentar fazer isso
    print("Oi")

except: # Se der erro, faça isso
    print("Tchau")
"""

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é {resultado}")
except ValueError:
    print("Erro: Você deve digitar um número.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")