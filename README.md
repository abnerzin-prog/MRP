# --- Funções do Módulo de Estoque ---

def obter_dados_item():
    """Coleta informações de um novo produto do usuário."""
    print("\n--- Cadastro de Produto ---")
    
    # Gerar um ID simples (simulando um código SKU/ID)
    import random
    codigo = str(random.randint(1000, 9999))
    
    nome = input("Nome do Produto: ")
    categoria = input("Categoria (Ex: Eletrônico, Alimento, Limpeza): ")
    
    # Tratamento de erro para valores numéricos
    while True:
        try:
            preco = float(input("Preço Unitário (R$): ").replace(',', '.'))
            quantidade = int(input("Quantidade Inicial em Estoque: "))
            break
        except ValueError:
            print("🚨 Erro: Preço e Quantidade devem ser números válidos.")

    # Retorna o produto como um Dicionário
    return {
        "Codigo": codigo,
        "Nome": nome,
        "Categoria": categoria,
        "Preco": preco,
        "Quantidade": quantidade
    }

def adicionar_ao_estoque(estoque_lista, produto):
    """Adiciona um produto (dicionário) à lista principal de estoque."""
    estoque_lista.append(produto)
    print(f"\n✅ Produto '{produto['Nome']}' cadastrado com sucesso (ID: {produto['Codigo']}).")

def excluir_produto(estoque_lista):
    """Permite remover um produto pelo seu nome ou código."""
    if not estoque_lista:
        print("\n⚠️ O estoque está vazio. Nada para excluir.")
        return

    termo = input("\nDigite o NOME ou o CÓDIGO do produto que deseja EXCLUIR: ").strip()
    
    # Busca o produto na lista
    produtos_para_remover = [
        p for p in estoque_lista 
        if p['Nome'].lower() == termo.lower() or p['Codigo'] == termo
    ]

    if not produtos_para_remover:
        print(f"\n❌ Produto com nome/código '{termo}' não encontrado.")
        return

    # Confirmação de exclusão
    produto_removido = produtos_para_remover[0]
    confirmar = input(f"Tem certeza que deseja excluir '{produto_removido['Nome']}' (ID: {produto_removido['Codigo']})? (S/N): ").lower()

    if confirmar == 's':
        estoque_lista.remove(produto_removido)
        print(f"\n🗑️ Produto '{produto_removido['Nome']}' removido com sucesso!")
    else:
        print("\n⛔ Exclusão cancelada.")

def exibir_relatorio_estoque(estoque_lista, LIMITE_BAIXO=5):
    """Exibe todos os produtos cadastrados em formato de tabela, destacando estoque baixo."""
    print("\n" + "="*80)
    print("📋 RELATÓRIO DE PRODUTOS CADASTRADOS")
    print("="*80)

    if not estoque_lista:
        print("O estoque está vazio. Cadastre um produto primeiro.")
        print("="*80)
        return

    # Cabeçalho da Tabela
    print(f"{'CÓDIGO':<8} {'NOME DO PRODUTO':<30} {'CATEGORIA':<15} {'PREÇO (R$)':<15} {'QTD.':<8}")
    print("-" * 80)

    # Linhas de Dados
    for produto in estoque_lista:
        # Formatação para destacar estoque baixo (Requisito)
        linha = ""
        if produto['Quantidade'] < LIMITE_BAIXO:
            # Destaca com estrelas e texto (Simulação de Alerta)
            linha += "🚨 "
            alerta = True
        else:
            linha += "   "
            alerta = False

        linha += f"{produto['Codigo']:<8} "
        linha += f"{produto['Nome']:<30} "
        linha += f"{produto['Categoria']:<15} "
        # Formata o preço para duas casas decimais
        linha += f"R$ {produto['Preco']:.2f}".ljust(15)
        linha += f"{produto['Quantidade']:<8}"
        
        print(linha)

    print("-" * 80)
    print(f"\n🚨 {len([p for p in estoque_lista if p['Quantidade'] < LIMITE_BAIXO])} produto(s) com estoque abaixo do limite ({LIMITE_BAIXO}).")
    print("="*80)

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- MÓDULO DE ESTOQUE - QUADRA AMIGA ERP ---")
    print("1 - Cadastrar novo produto")
    print("2 - Excluir produto")
    print("3 - Mostrar relatório de produtos (Listar)")
    print("4 - Sair do programa")
    print("-" * 40)
    
# --- Programa Principal ---

def main():
    # Inicializa a lista de estoque vazia
    estoque = []

    while True:
        exibir_menu()
        
        # Tratamento de erro para a opção do menu
        try:
            opcao = input("Escolha uma opção (1-4): ")
        except EOFError:
            # Caso o input falhe
            opcao = '4' 

        if opcao == '1':
            # Cadastrar produto
            novo_item = obter_dados_item()
            adicionar_ao_estoque(estoque, novo_item)
        
        elif opcao == '2':
            # Excluir produto
            excluir_produto(estoque)

        elif opcao == '3':
            # Mostrar relatório
            exibir_relatorio_estoque(estoque)

        elif opcao == '4':
            # Sair
            print("\n👋 Encerrando o programa. Até mais!")
            break
        
        else:
            print("\n❌ Opção inválida. Por favor, digite um número de 1 a 4.")

if __name__ == "__main__":
    main()
