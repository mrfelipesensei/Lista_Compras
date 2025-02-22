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

def menu():
    while True:
        print("\n1. Adicionar item\n2. Remover item\n3. Exibir lista\n4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_item()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida!Tente novamente.")

#Executar o menu
menu()