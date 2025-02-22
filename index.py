import tkinter as tk
from tkinter import messagebox
import json
import os

#Nome do arquivo onde os dados serão salvos
ARQUIVO_JSON = "lista_compras.json"

#Lista de compras (dicionário: item -> [quantidade, preço])
lista_compras = {}

#Função para salvar a lista em JSON
def salvar_lista():
    with open(ARQUIVO_JSON, "w") as file:
        json.dump(lista_compras,file,indent=4)
    print("Lista salva com sucesso!")

#Função para carregar a lista do arquivo JSON
def carregar_lista():
    global lista_compras
    if os.path.exists(ARQUIVO_JSON): #Verifica se o arquivo existe
        with open(ARQUIVO_JSON, "r") as file:
            lista_compras = json.load(file)
    atualizar_lista()


#Função de atualizar a exibição da lista na interface
def atualizar_lista():
    lista_box.delete(0,tk.END) #Limpa a exibição
    for item, (quantidade, preco) in lista_compras.items():
        lista_box.insert(tk.END, f"{quantidade} x {item} - R$ {preco:.2f}")

#Função de adicionar item
def adicionar_item():
    item = entrada_item.get().strip().lower()
    if not item:
        messagebox.showerror("Aviso","Digite o nome do item!")
        return
    
    try:
        quantidade = int(entrada_quantidade.get())
        preco = float(entrada_preco.get())
        if quantidade <= 0 or preco <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro","Quantidade e Preço devem ser números positivos!")
        return


    #Lógica de verificação e adição do item à lista
    if item in lista_compras:
        lista_compras[item][0] += quantidade #Atualiza quantidade
    else:
        lista_compras[item] = [quantidade,preco]

    print(f"{quantidade}x {item} adicionado(s) à lista de compras.")
    salvar_lista() #Salva automaticamente após adicionar um item
    atualizar_lista()
    entrada_item.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_preco.delete(0, tk.END)

def remover_item():
    item = input("Digite o nome do item a ser removido: ").strip().lower()

    if item in lista_compras:
        del lista_compras[item]
        print(f"{item} removido da lista")
        salvar_lista() #Salva automaticamente após remover um item
    else:
        print("Item não encontrado.")

def editar_item():
    item = input("Digite o nome do item para alterá-lo: ").strip().lower()

    if item not in lista_compras:
        print("Item não encontrado na lista.")
        return
    
    print(f"Item atual: {item} | Quantidade: {lista_compras[item][0]} | Preço: {lista_compras[item][1]:.2f}")

    while True:
        try:
            nova_quantidade = int(input("Nova quantidade (ou Enter para manter): ") or lista_compras[item][0])
            if nova_quantidade <= 0:
                print("A quantidade deve ser um número maior que zero!")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número inteiro!")    
    
    while True:
        try:
            novo_preco = float(input("Novo preço unitário (ou Enter para manter): R$ ") or lista_compras[item][1])
            if novo_preco <= 0:
                print("O valor deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número!")

    #Atualiza item na lista de compras
    lista_compras[item] = [nova_quantidade,novo_preco]
    print(f"{item} Atualizado! Nova quantidade: {nova_quantidade} e Novo preço: R$ {novo_preco:.2f}")
    salvar_lista() #Salva automaticamente após editar um item


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
    carregar_lista() #Carregar a lista ao iniciar o programa
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