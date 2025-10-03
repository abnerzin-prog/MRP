def obter_dados_item():
    """Coleta informações de um item do usuário."""
    codigo = input("Codigo do produto: ")
    item = input("Descrição do produto: ")
    unidade = input("Unidade (ex: kg, un): ")
    valor = float(input("Valor unitário: "))
    return {"Codigo do produto": codigo, "Item": item, "Unidade": unidade, "Valor Unitário": valor}

def adicionar_ao_estoque(estoque_lista, produto):
    """Adiciona um produto à lista de estoque."""
    estoque_lista.append(produto)
    print(f"'{produto['Item']}' adicionado.")

def exibir_tabela_estoque(estoque_lista):
    """Exibe todos os produtos cadastrados em formato de tabela."""
    print("\n--- Produtos Cadastrados ---")
    print(f"{'Item':20} {'Unidade':10} {'Valor Unitário':>15}")
    print("-" * 50)
    for produto in estoque_lista:
        print(f"{produto['Item']:20} {produto['Unidade']:10} R$ {produto['Valor Unitário']:>10.2f}")

# Programa principal
estoque = []
while True:
    novo_item = obter_dados_item()
    adicionar_ao_estoque(estoque, novo_item)
    continuar = input("Deseja cadastrar outro item? (s/n): ").lower()
    if continuar != "s":
        break
exibir_tabela_estoque(estoque)
