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
