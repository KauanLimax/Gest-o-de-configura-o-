"""To-Do GCS - lista de tarefas em linha de comando."""

tarefas = []


def mensagem_boas_vindas():
    return "Bem-vindo ao To-Do"


def adicionar(descricao):
    """Adiciona uma tarefa pendente e retorna seu índice."""
    if not descricao or not descricao.strip():
        raise ValueError("Descrição não pode ser vazia")
    tarefas.append({"descricao": descricao.strip(), "concluida": False})
    return len(tarefas) - 1


def listar():
    """Retorna a lista de tarefas."""
    return list(tarefas)


def concluir(indice):
    """Marca a tarefa como concluída."""
    tarefas[indice]["concluida"] = True


def remover(indice):
    """Remove a tarefa e a retorna."""
    return tarefas.pop(indice)


def exibir():
    if not tarefas:
        print("Nenhuma tarefa.")
    for i, t in enumerate(tarefas):
        marca = "x" if t["concluida"] else " "
        print(f"{i}. [{marca}] {t['descricao']}")


def menu():
    print(mensagem_boas_vindas())
    while True:
        print("\n1) Adicionar  2) Listar  3) Concluir  4) Remover  0) Sair")
        op = input("Opção: ").strip()
        try:
            if op == "1":
                adicionar(input("Descrição: "))
            elif op == "2":
                exibir()
            elif op == "3":
                concluir(int(input("Índice: ")))
            elif op == "4":
                remover(int(input("Índice: ")))
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except (ValueError, IndexError) as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    menu()
