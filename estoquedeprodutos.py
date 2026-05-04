def adicionar_produto(estoque):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))  
    preco = float(input("Preco: "))

    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print(f"{nome} adicionado com sucesso!")

def listar_produtos(estoque):
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[0])
    print("\n--- Lista de estoque ---")
    for nome, dados in produtos_ordenados:
        print(f"{nome}: {dados['quantidade']} disponível - R${dados['preco']:.2f}")

def remover_produto(estoque):
    nome = input("Nome do produto a remover: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto removido.")
    else:
        print("Erro: Produto não encontrado.")

def atualizar_quantidade(estoque):
    nome = input("Nome do produto: ")
    if nome in estoque:
        nova_qtd = int(input("Nova quantidade: "))
        estoque[nome]["quantidade"] = nova_qtd
        print("Quantidade atualizada.")
    else:
        print("Erro: Produto não encontrado.")

def exibir_menu():
    return (
        "\n1 - Adicionar produto"
        "\n2 - Listar produtos"
        "\n3 - Remover produto"
        "\n4 - Atualizar quantidade"
        "\n5 - Sair"
    )

def main():
    estoque = {}

    while True:
        print(exibir_menu())
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            atualizar_quantidade(estoque)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()