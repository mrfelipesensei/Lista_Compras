#Lista de compras (dicionário: item -> [quantidade, preço])
lista_compras = {}

#Função de adicionar item
def adicionar_item():
    item = input("Digite o nome do item: ").strip().lower()
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser um número inteiro maior que zero!")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro!")
    
    
    while True:
        try:
            preco = float(input("Digite o preço unitário: "))
            if preco <= 0:
                print("O valor deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("Valor inválido!")

    #Lógica de verificação e adição do item à lista
    if item in lista_compras:
        lista_compras[item][0] += quantidade #Atualiza quantidade
    else:
        lista_compras[item] = [quantidade,preco]

    print(f"{quantidade}x {item} adicionado(s) à lista de compras.")

def remover_item():
    item = input("Digite o nome do item a ser removido: ").strip().lower()

    if item in lista_compras:
        del lista_compras[item]
        print(f"{item} removido da lista")
    else:
        print("Item não encontrado.")

def editar_item():
    item = input("Digite o nome do item para alterá-lo: ").strip().lower()

    if item not in lista_compras:
        print("Item não encontrado na lista.")
        return
    
    print(f"Item atual: {item} | Quantidade: {lista_compras[item][0]} | Preço: {lista_compras[item][1]:.2f}")

    nova_quantidade = int(input("Nova quantidade (ou Enter para manter: )" or lista_compras[item][0]))
    novo_preco = float(input("Novo preço unitário (ou Enter para manter): R$ "or lista_compras[item][1]))

    #Atualiza item na lista de compras
    lista_compras[item] = [nova_quantidade,novo_preco]
    print(f"{item} Atualizado! Nova quantidade: {nova_quantidade} e Novo preço: R$ {novo_preco:.2f}")

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
        print("\n1. Adicionar item\n2. Remover item\n3. Editar item\n4. Exibir lista\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item()
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            editar_item()
        elif opcao == "4":
            exibir_lista()
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida!Tente novamente.")

#Executar o menu
menu()