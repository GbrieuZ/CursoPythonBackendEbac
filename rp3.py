
# - Aprovado, reprovado ou recuperação:
# Receba a média de um aluno e diga se ele foi aprovado (média >= 7),
# em recuperação (5 <= média < 7) ou
# reprovado (média < 5).

# 1. Receber a nota do aluno
nota = float(input())

# 2. Fazer a operação e já mostrar o resultado para o aluno.

if nota >= 7.0:
    print("Aluno APROVADO!")
elif 5.0 <= nota < 7.0:
    print("Aluno em RECUPERAÇÃO!")
else:
    print("Aluno REPROVADO!")
