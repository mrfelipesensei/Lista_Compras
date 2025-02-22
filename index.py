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
    selecionado = lista_box.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso","Selecione um item para remover!")
        return
    
    item_texto = lista_box.get(selecionado[0])
    item_nome = item_texto.split("x ")[1].split(" - ")[0]

    if item_nome in lista_compras:
        del lista_compras[item_nome]
        salvar_lista()
        atualizar_lista()

'''
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

'''
#Criar a janela principal
janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("400x450")

#Widgets de entrada
tk.Label(janela, text="Item: ").pack()
entrada_item = tk.Entry(janela)
entrada_item.pack()

tk.Label(janela, text="Quantidade: ").pack()
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack()

tk.Label(janela, text="Preço unitário (R$):").pack()
entrada_preco = tk.Entry(janela)
entrada_preco.pack()

#Botões de ação
btn_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_item)
btn_adicionar.pack()

btn_remover = tk.Button(janela, text="Remover",command=remover_item)
btn_remover.pack()

#Lista de Compras
lista_box = tk.Listbox(janela, width=50)
lista_box.pack()

#Carregar dados e atualizar lista ao iniciar
carregar_lista()

#Executar a interface gráfica
janela.mainloop()