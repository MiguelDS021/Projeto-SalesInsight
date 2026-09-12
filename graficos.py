import matplotlib.pyplot as plt
import mplcursors 

def Grafico_Faturamento_Produto(dado):
      
            plt.figure(figsize=(8,5))
            barra = plt.bar(dado.index, dado.values)
            plt.title("Faturamento por produtos", fontsize=14)
            plt.xlabel("Produtos", fontsize=12)
            plt.ylabel("Valor", fontsize=12)
            cursor = mplcursors.cursor(barra, hover=True)
            @cursor.connect("add")
            def _(sel):
                sel.annotation.set_text(f"Faturamento: R${sel.target[1]:.2f}")
            plt.show()

def Grafico_Quantidade_Produto(dados):
            
            barra = plt.bar(dados.index, dados.values)

            plt.title("Quantidade vendida por produtos", fontsize=14)
            plt.xlabel("Produtos", fontsize=12)
            plt.ylabel("Quantidade", fontsize=12)
            cursor2 = mplcursors.cursor(barra, hover=True)
            @cursor2.connect("add")
            def _(sel):
                sel.annotation.set_text(f"Quantidade: {sel.target[1]:.0f}")
            plt.show()    

def Grafico_Faturamento_Categoria(dados):
            
            barra = plt.bar(dados.index, dados.values)

            plt.title("Faturamento por categorias", fontsize=14)
            plt.xlabel("Categorias", fontsize=12)
            plt.ylabel("Valor", fontsize=12)

            cursor3 = mplcursors.cursor(barra, hover=True)
            @cursor3.connect("add")
            def _(sel):
                sel.annotation.set_text(f"Valor: {sel.target[1]:.2f}")
            plt.show()    

def Grafico_Quantidade_Categoria(dados):
                   
            barra = plt.bar(dados.index, dados.values)

            plt.title("Quantidade vendida por categorias", fontsize=14)
            plt.xlabel("Categorias", fontsize=12)
            plt.ylabel("Quantidade", fontsize=12)

            cursor4 = mplcursors.cursor(barra, hover=True)
            @cursor4.connect("add")
            def _(sel):
                sel.annotation.set_text(f"Quantidade: {sel.target[1]:.0f}")
            plt.show()

def Grafico_Participacao_Categoria(dados):
            
            plt.pie(dados.values, labels=dados.index, autopct="%1.f%%")
            plt.title("Participação no faturamento por categoria", fontsize=12)
            plt.show()

def Grafico_Faturamento_Tempo(dados):
           
        plt.plot(dados.index, dados.values)
        plt.title("Faturamento ao longo do tempo", fontsize=12)
        plt.xlabel("Data", fontsize=12)
        plt.ylabel("Faturamento", fontsize=12)
        plt.show()