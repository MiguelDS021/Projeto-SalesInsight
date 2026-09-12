from produtos import Produtos
from datetime import datetime

Vendas = {}
def Adicionar_Vendas(ID_venda, ID_produto, Nome, Data, Categoria, Quantidade, Preço_unitário, Total):

    Vendas[f"Venda{ID_venda}"] = {
        "ID da venda": ID_venda,
        "ID do produto": ID_produto,
        "Nome do produto": Nome,
        "Data da venda": Data,
        "Categoria": Categoria,
        "Quantidade": Quantidade,
        "Preço unitário": Preço_unitário,
        "Total": Total
    }        

id_venda = 0
def Registrar_Vendas(id_venda):
    try:
        id1 = int(input("Digite o id do produto: "))
    except ValueError:
        print("ERRO: O ID deve ser um número inteiro.")
        return id_venda

    buscado = False
    
    for chave, valor in Produtos.items():
        if valor["ID"] == id1:
            try:
                qtd = int(input("Digite a quantidade desejada: "))
                buscado = True
            except ValueError:
                print("ERRO: Só é permitido números")
                continue

            if qtd <= 0:
                print("ERRO: Não é permitido o valor 0")

            else:    
                if valor["Estoque"] >= qtd:
                    print("Venda registrada com sucesso.")
                    data = datetime.now().date()
                    valor["Estoque"] -= qtd 
                    Total = valor["Preço"] * qtd
                    id_venda += 1
                    Adicionar_Vendas(id_venda, id1, valor["Nome"], data, valor["Categoria"],qtd, valor["Preço"], Total)
                    
                else:
                    print("Quantidade insuficiente em estoque.")

    if buscado == False:
        print("Este produto não existe.") 

    return id_venda        

def Visualizar_Vendas():
    print(f"{'=' * 5} Vendas {'=' * 5}")
    if not Vendas:
        print("Não existem vendas registradas")

    else:
        for chave, valor in Vendas.items():
            print(f"""
{chave}
ID da venda: {valor["ID da venda"]}
ID do produto: {valor["ID do produto"]}
Nome do produto: {valor["Nome do produto"]}
Categoria: {valor["Categoria"]}
Quantidade: {valor["Quantidade"]}
Preço unitário: {valor["Preço unitário"]}
Total: {valor["Total"]} """)

def Buscar_Vendas_Por_ID():
    try:
        id2 = int(input("Digite o id da venda: "))
    except ValueError:
        print("ERRO: O ID deve ser um número inteiro.")
        return

    condição = False
    for chave, valor in Vendas.items():
        if valor["ID da venda"] == id2:
            print(f"""{valor["ID da venda"]}
            {valor["ID do produto"]}
            {valor["Nome do produto"]}
            {valor["Categoria"]}
            {valor["Quantidade"]}
            {valor["Preço unitário"]}
            {valor["Total"]}""")
            condição = True
            
    if condição == False:
        print("Este produto não existe")