#Lista de compras (dicionário: item -> [quantidade, preço])
lista_compras = {}

#Função de adicionar item
def adicionar_item():
    item = input("Digite o nome do item: ").strip().lower()
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço unitário: "))

    #Lógica de verificação e adição do item à lista
    if item in lista_compras:
        lista_compras[item][0] += quantidade #Atualiza quantidade
    else:
        lista_compras[item] = [quantidade,preco]

    print(f"{quantidade}x {item} adicionado(s) à lista de compras.")

def remover_item():
    item = input("Digite o nome do item a ser removido: ")

    if item in lista_compras:
        del lista_compras[item]
        print(f"{item} removido da lista")
    else:
        print("Item não encontrado.")

def exibir_lista():
    if not lista_compras:
        print("A lista de compras está vazia.")
        return
    
    print("\nLista de compras: ")
    total = 0
    for item, (quantidade,preco) in lista_compras.items(): #Mostra os itens da lista
        subtotal = quantidade * preco #Calcula o preço pela quantidade
        total += subtotal #Soma o valor do item ao valor total
        print(f" - {item}: {quantidade} unidade(s) | R$ {preco:.2f} cada | Subtotal R$ {subtotal:.2f}")

    print(f"\nValor Total da compra: R$ {total:.2f}") #Exibe o valor da compra ao final

def menu():
    while True:
        print("\n1. Adicionar item\n2. Remover item\n3. Exibir lista\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            exibir_lista()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida!Tente novamente.")

#Executar o menu
menu()