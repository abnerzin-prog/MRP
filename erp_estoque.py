import sqlite3

# -----------------------------------------------------
# Função para conectar ao banco e criar tabela (caso não exista)
# -----------------------------------------------------
def inicializar_banco():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# -----------------------------------------------------
# Cadastro de produto
# -----------------------------------------------------
def cadastrar_produto():
    print("\n--- CADASTRO DE PRODUTO ---")

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")

    # validações de número
    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            quantidade = int(input("Quantidade inicial: "))
            break
        except:
            print("❌ Digite valores válidos para preço e quantidade.")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade))

    conexao.commit()
    conexao.close()

    print(f"\n✅ Produto '{nome}' cadastrado com sucesso!")


# -----------------------------------------------------
# Exclusão de produto
# -----------------------------------------------------
def excluir_produto():
    print("\n--- EXCLUSÃO DE PRODUTO ---")

    termo = input("Digite o ID ou Nome do produto: ")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    # verifica se é ID ou nome
    if termo.isdigit():
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (termo,))
    else:
        cursor.execute("SELECT * FROM produtos WHERE nome = ?", (termo,))

    produto = cursor.fetchone()

    if not produto:
        print("❌ Produto não encontrado.")
        conexao.close()
        return

    print(f"\nEncontrado: ID {produto[0]} | Nome: {produto[1]} | Quantidade: {produto[4]}")
    confirmar = input("Confirmar exclusão? (S/N): ").lower()

    if confirmar == "s":
        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto[0],))
        conexao.commit()
        print("🗑️ Produto excluído com sucesso!")
    else:
        print("⛔ Exclusão cancelada.")

    conexao.close()


# -----------------------------------------------------
# Relatório de produtos
# -----------------------------------------------------
def listar_produtos():
    print("\n==========================")
    print(" 📋 RELATÓRIO DO ESTOQUE ")
    print("==========================")

    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("\n⚠️ Nenhum produto cadastrado.")
        conexao.close()
        return

    print(f"{'ID':<5} {'NOME':<25} {'CATEGORIA':<15} {'PREÇO(R$)':<12} {'QTD':<5}")
    print("-" * 65)

    baixo = 0

    for p in produtos:
        alerta = "🚨" if p[4] < 5 else " "
        print(f"{alerta} {p[0]:<5} {p[1]:<25} {p[2]:<15} R$ {p[3]:<10.2f} {p[4]:<5}")
        if p[4] < 5:
            baixo += 1

    print("-" * 65)
    print(f"\n⚠️ {baixo} produto(s) com estoque baixo (menos que 5).")

    conexao.close()


# -----------------------------------------------------
# Menu
# -----------------------------------------------------
def menu():
    print("\n--- MÓDULO DE ESTOQUE - MINI ERP ---")
    print("1 - Cadastrar produto")
    print("2 - Excluir produto")
    print("3 - Mostrar relatório")
    print("4 - Sair")
    print("-----------------------------------")


# -----------------------------------------------------
# Programa Principal
# -----------------------------------------------------
def main():
    inicializar_banco()

    while True:
        menu()
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            excluir_produto()

        elif opcao == "3":
            listar_produtos()

        elif opcao == "4":
            print("\n👋 Encerrando o sistema...")
            break

        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
