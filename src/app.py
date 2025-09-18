from task_manager import *
from database import create_tables

def main():
    create_tables()
    print("=== Gerenciador de Tarefas ===")

    # Criar usuário inicial(caso não exista)
    if not get_user_by_email("teste@email.com"):
        create_user("Usuário Teste", "teste@email.com", "1234")

    user = get_user_by_email("teste@email.com")
    user_id = user[0]

# ------------------ LOGIN ------------------ #
print("\n🔐 Faça login abaixo: ")
email = input("E-mail: ")
senha = input("Senha: ")
# ------------------ MENU ------------------ #
while True:
        print("\n1. Listar Tarefas\n2. Adicionar Tarefa\n3. Atualizar Status\n4. Excluir Tarefa\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tasks = list_tasks(user_id)
            for t in tasks:
                print(f"[{t[0]}] {t[1]} - {t[2]} (prazo: {t[3]})")

        elif opcao == "2":
            title = input("Título: ")
            desc = input("Descrição: ")
            due = input("Prazo (YYYY-MM-DD): ")
            add_task(title, desc, due, user_id)
            print("✅ Tarefa adicionada!")

        elif opcao == "3":
            task_id = int(input("ID da tarefa: "))
            status = input("Novo status (pendente/concluída/atrasada): ")
            update_task_status(task_id, status)
            print("🔄 Status atualizado!")

        elif opcao == "4":
            task_id = int(input("ID da tarefa: "))
            delete_task(task_id)
            print("🗑️ Tarefa excluída!")

        elif opcao == "5":
            print("👋 Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
