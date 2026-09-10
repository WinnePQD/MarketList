# ==============================================
# PROJETO: Lista de Mercado
# Linguagem: Python
# ==============================================

# Primeiro, vamos criar uma LISTA para guardar os itens
lista_mercado = []

# Função para adicionar um item
def adicionar_item():
    item = input("Digite o nome do produto: ")
    lista_mercado.append(item)
    print(f"✅ '{item}' foi adicionado à lista!")

# Função para mostrar a lista completa
def mostrar_lista():
    print("\n📋 MINHA LISTA DE MERCADO:")
    if len(lista_mercado) == 0:
        print("A lista está vazia!")
    else:
        for indice, produto in enumerate(lista_mercado, start=1):
            print(f"{indice}. {produto}")
    print("-" * 30)

# Menu principal do programa
while True:
    print("\n===== LISTA DE MERCADO =====")
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        mostrar_lista()
    elif opcao == "3":
        print("👋 Programa encerrado! Até logo.")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")