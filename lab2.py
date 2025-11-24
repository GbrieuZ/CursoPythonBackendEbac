# O dicionário global para armazenar as tarefas.
# Essa variável é usada e modificada por todas as funções.
tarefas = {}

def adicionar_tarefa(nome_tarefa):
    """Adiciona uma tarefa ao dicionário. Retorna uma mensagem."""
    global tarefas
    if nome_tarefa in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome_tarefa] = False  # False para pendente
        return f"Tarefa '{nome_tarefa}' adicionada com sucesso!!"


def listar_tarefas(tarefas):
    """Lista todas as tarefas em ordem alfabética e retorna uma string formatada."""
    if not tarefas:
        return "Nenhuma tarefa cadastrada."

    lista_formatada = []
    for nome, status in sorted(tarefas.items()):
        emoji = "✅" if status else "❌"
        status_texto = "Concluída" if status else "Não concluída"
        lista_formatada.append(f"{emoji} {nome} - {status_texto}")

    return "\n".join(lista_formatada)


def remover_tarefa(nome_tarefa):
    """Remove uma tarefa existente. Retorna uma mensagem."""
    if nome_tarefa in tarefas:
        del tarefas[nome_tarefa]
        return f"Tarefa '{nome_tarefa}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."


def marcar_concluida(nome_tarefa):
    """Atualiza o status de uma tarefa para 'concluída'. Retorna uma mensagem."""
    if nome_tarefa in tarefas:
        tarefas[nome_tarefa] = True  # Define o status como True
        return f"Tarefa '{nome_tarefa}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."


def exibir_menu():
    """Retorna a string do menu para ser impressa."""
    return """
Menu:
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Marcar tarefa como concluída
5 - Sair
"""


def main():
    """Função principal que interage com o usuário e chama as funções."""
    while True:
        print(exibir_menu())
        opcao = input("Digite uma opção: ").strip()

        if opcao == '1':
            nome = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(nome))
        elif opcao == '2':
            print(listar_tarefas())
        elif opcao == '3':
            nome = input("Digite o nome da tarefa que deseja remover: ")
            print(remover_tarefa(nome))
        elif opcao == '4':
            nome = input("Digite o nome da tarefa que deseja marcar como concluída: ")
            print(marcar_concluida(nome))
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()