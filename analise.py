import pandas as pd
from vendas import Vendas
from graficos import (Grafico_Faturamento_Produto, Grafico_Quantidade_Produto, Grafico_Faturamento_Categoria, Grafico_Quantidade_Categoria, Grafico_Participacao_Categoria, Grafico_Faturamento_Tempo)

def Analisar_Vendas():

    if not Vendas:
        print("Não existem vendas para analisar.")
        return

    df = pd.DataFrame(Vendas.values())
    while True:
        try:
            opcao = int(input("""
===== ANÁLISE DE VENDAS =====

[1] Resumo das vendas
[2] Faturamento total
[3] Quantidade de produtos vendidos
[4] Produtos mais vendidos
[5] Faturamento por produtos
[6] Ticket médio
[7] Faturamento por categorias
[8] Gráficos
[9] Voltar

Escolha uma opção: """))
        except ValueError:
            print("ERRO: Digite apenas números.")
            continue
        if opcao < 1 or opcao > 9:
            print("ERRO: Insira uma opção válida")

        elif opcao == 1:
            print(df.describe())

        elif opcao == 2:
            print(f"Faturamento total: R$ {df["Total"].sum():.2f}")

        elif opcao == 3:
            print(f"Produtos vendidos: {df["Quantidade"].sum()}")

        elif opcao == 4:
            mais_vendidos = df.groupby("Nome do produto")["Quantidade"].sum()
            mais_vendidos = mais_vendidos.sort_values(ascending=False)

            print(f"""
            ===== PRODUTOS MAIS VENDIDOS =====
            {mais_vendidos}""")

        elif opcao == 5:    
            faturamento = df.groupby("Nome do produto")["Total"].sum()
            faturamento = faturamento.sort_values(ascending=False)

            print(f"""
    ===== FATURAMENTO POR PRODUTOS =====
    {faturamento} """)

        elif opcao == 6:
            ticket_medio = df["Total"].mean()
            print(f"""
    ===== TICKET MÉDIO =====
    R$ {ticket_medio:.2f} """)

        elif opcao == 7: 
            fat_cat = df.groupby("Categoria")["Total"].sum()
            fat_cat = fat_cat.sort_values(ascending=False)

            print(f""" 
            ===== FATURAMENTO POR CATEGORIAS =====
            {fat_cat}
              """)

        elif opcao == 8:  
            faturamento = df.groupby("Nome do produto")["Total"].sum()
            faturamento = faturamento.sort_values(ascending=False)
            Grafico_Faturamento_Produto(faturamento)

            produtos_vendidos = df.groupby("Nome do produto")["Quantidade"].sum()
            produtos_vendidos = produtos_vendidos.sort_values(ascending=False)
            Grafico_Quantidade_Produto(produtos_vendidos)

            cat_fatura = df.groupby("Categoria")["Total"].sum()
            Grafico_Faturamento_Categoria(cat_fatura.sort_values(ascending=False))

            qtd_cat = df.groupby("Categoria")["Quantidade"].sum()
            qtd_cat = qtd_cat.sort_values(ascending=False)
            Grafico_Quantidade_Categoria(qtd_cat)

            Grafico_Participacao_Categoria(cat_fatura.sort_index())

            fat_data = df.groupby("Data da venda")["Total"].sum()
            fat_data = fat_data.sort_index()

            Grafico_Faturamento_Tempo(fat_data)

        elif opcao == 9:         
            break            
