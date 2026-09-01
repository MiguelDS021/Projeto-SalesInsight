id = 0
categorias = ["Camisetas", "Calças", "Calçados", "Acessórios"]
tamanhos = {
    "Camisetas": ["P", "M", "G", "GG"],
    "Calças": [38, 40, 42, 44],
    "Calçados": [38, 39, 40, 41],
    "Acessórios": ["Único"]
}

def Cadastrar_Produtos(id):
    try:    
        while True:
            nome = input("Digite o nome do produto: ").strip()
            if nome == "": 
                print("Erro: É necessário digitar um nome.")
            else:
                break  

        for i, cat in enumerate(categorias, start=1):
            print(f"[{i}] {cat}")

        esc_categoria = int(input("Escolha o tamanho: "))
        if esc_categoria < 1 or esc_categoria > len(categorias):
            print("ERRO: Digite uma opção válida")
        else:    
            categoria = categorias[esc_categoria - 1]

        lista = tamanhos[categoria]
        for i, tam in enumerate(lista, start=1):
            print(f"[{i}] {tam}")
            
        esc_tamanho = int(input("Escolha o tamanho: "))
        if esc_tamanho < 1 or esc_tamanho > len(lista):
            print("ERRO: Digite uma opção válida")
        else:    
            tamanho = lista[esc_tamanho- 1]



        while True:                          
            preço = float(input("Digite o preço: R$ "))
            if preço <= 0:
                print("Erro: O preço do produto não pode ser negativo ou igual a 0.")
            else:
                break    

        while True:    
            estoque = int(input("Digite a quantidade: "))
            if estoque < 0:
                print("Erro: O valor do estoque não pode ser negativo.")
            else:
                break    
    
    except ValueError:
        print("Erro: Em preço só é permitido números decimais e em estoque números inteiros.")    
    
    else:  
       
        id += 1
        Adicionar_Produtos(id, nome, categoria, tamanho, preço, estoque) 
        return id
    

Produtos = {}
def Adicionar_Produtos(id, nome, categoria, tamanho, preço, estoque):
    
        Produtos[f"Produto{id}"] = {
            "ID": id,
            "Nome": nome,
            "Categoria": categoria,
            "Tamanho": tamanho,
            "Preço": preço,
            "Estoque": estoque           
}

    
def Visualizar_Produtos():
    if not Produtos:
        print("O dicionário não possui produtos cadastrados")
    else:
        print(f"{'=' * 5} Produtos {'=' * 5}")
        for chave, valor in Produtos.items():
            print(f"""
{chave}
ID: {valor["ID"]}
Nome: {valor["Nome"]}
Categoria: {valor["Categoria"]}
Tamanho: {valor["Tamanho"]}
Preço: {valor["Preço"]}
Estoque: {valor["Estoque"]}

-------------""")

def Buscar_Produtos():
    while True:
        alternativa = int(input("""Escolha uma alternativa:
        [1] Buscar por id
        [2] Buscar por nome
        [3] Voltar"""))

        if alternativa < 1 or alternativa > 3:
            print("Erro: Escolha uma opção válida.")
        else:
            if alternativa == 1:
                Buscar_Por_Id()

            elif alternativa == 2:
                Buscar_Por_Nome()

            elif alternativa == 3:
                break


def Buscar_Por_Id():
    busca = int(input("Digite o ID do produto: "))

    encontrado = False
    for chave, valor in Produtos.items():
        if busca == valor["ID"]:
            print(f"""{valor["ID"]}
        {valor["Nome"]}
        {valor["Categoria"]}
        {valor["Tamanho"]}
        {valor["Preço"]}
        {valor["Estoque"]}""")
            encontrado = True

    if encontrado == False:
        print("Este produto não existe") 

                   
def Buscar_Por_Nome():
    procura = input("Escreva o nome do produto: ")

    nome_encontrado = False
    for chave, valor in Produtos.items():
        if procura in valor["Nome"]:
            print(f"""{valor["ID"]}
        {valor["Nome"]}
        {valor["Categoria"]}
        {valor["Tamanho"]}
        {valor["Preço"]}
        {valor["Estoque"]}""")
            nome_encontrado = True

    if nome_encontrado == False:
        print("Não existe produtos com este nome")


def Alterar_Produtos():
    alteração = int(input("Digite o id do produto: "))

    id_encontrado = False
    for chave, valor in Produtos.items():
        if alteração == valor["ID"]:
            id_encontrado = True
            while True:
                submenu = int(input("""Escolha uma opção:
                [1] Nome
                [2] Categoria
                [3] Tamanho
                [4] Preço
                [5] Estoque
                [6] Voltar """))

                if submenu < 1 or submenu > 6:
                    print("Erro: Escolha uma opção válida.")
                else:

                    if submenu == 1:
                        Alterar_Nome(valor)

                    elif submenu == 2:
                        Alterar_Categoria(valor)     

                    elif submenu == 3:
                         Alterar_Tamanho(valor)

                    elif submenu == 4:
                         Alterar_Preco(valor)

                    elif submenu == 5:       
                        Alterar_Estoque(valor) 

                    elif submenu == 6:
                        break    

        if id_encontrado == False:
            print("O id não existe")


def Alterar_Nome(valor):
    novo_nome= input("Digite o novo nome: ")
    valor["Nome"] = novo_nome


def Alterar_Categoria(valor):
    escolhe = int(input("""Escolha uma opção:
    [1] Camiseta
    [2] Calça
    [3] Calçados
    [4] Acessórios"""))

    if escolhe < 1 or escolhe > 4:
        print("Erro: Escolha uma opção válida.")
    else:
        valor["Categoria"] = categorias[escolhe-1]  
        Alterar_Tamanho(valor)


def Alterar_Preco(valor):
    novo_preço= float(input("Digite um novo preço: "))

    if novo_preço <=0:
        print("ERRO: Não é permitido valores iguais ou menores que 0")
    else:
        valor["Preço"] = novo_preço


def Alterar_Estoque(valor):
    novo_estoque = int(input("Digite um novo valor para estoque: "))
    if novo_estoque < 0:
        print("ERRO: Não é permitido valores menores que 0")
    else:
        valor["Estoque"] = novo_estoque    


def Alterar_Tamanho(valor):
    lista = tamanhos[valor["Categoria"]]

    for i, tamanho in enumerate(lista, start=1):
        print(f"[{i}] {tamanho}")


    esc_tamanho = int(input("Escolha o tamanho: "))
    if esc_tamanho < 1 or esc_tamanho > len(lista):
        print("ERRO: Digite uma opção válida")
    else:    
        valor["Tamanho"] = lista[esc_tamanho - 1]

def Excluir_Produtos():
    procura_id = int(input("Digite o id do produto: "))

    busca_id = False

    for chave, valor in Produtos.items():
        if procura_id == valor["ID"]:
            busca_id = True
            break

    if busca_id:
        del Produtos[chave]
        print("Produto excluído com sucesso.")
    else:
        print("O ID não existe.")

Vendas = {}
def Adicionar_Vendas(ID_venda, ID_produto, Nome, Quantidade, Preço_unitário, Total):

    Vendas[f"Venda{ID_venda}"] = {
        "ID da venda": ID_venda,
        "ID do produto": ID_produto,
        "Nome do produto": Nome,
        "Quantidade": Quantidade,
        "Preço unitário": Preço_unitário,
        "Total": Total
    }        

id_venda = 0
def Registrar_Vendas(id_venda):
    id1 = int(input("Digite o id do produto: "))

    buscado = False
    
    for chave, valor in Produtos.items():
        if valor["ID"] == id1:
            qtd = int(input("Digite a quantidade desejada: "))
            buscado = True
            if qtd == 0 or qtd < 0:
                print("ERRO: Não é permitido o valor 0")

            else:    
                if valor["Estoque"] >= qtd:
                    print("Quantidade em estoque")
                    valor["Estoque"] -= qtd
                    Total = valor["Preço"] * qtd
                    id_venda += 1
                    Adicionar_Vendas(id_venda, id1, valor["Nome"], qtd, valor["Preço"], Total)
                    return id_venda

        else:
            print("Quantidade em falta no estoque")

    if buscado == False:
        print("Este produto não existe")     

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
Quantidade: {valor["Quantidade"]}
Preço unitário: {valor["Preço unitário"]}
Total: {valor["Total"]} """)

def Buscar_Vendas_Por_ID():
    id2 = int(input("Digite o id da venda: "))

    condição = False
    for chave, valor in Vendas.items():
        if valor["ID da venda"] == id2:
            print(f"""{valor["ID da venda"]}
            {valor["ID do produto"]}
            {valor["Nome do produto"]}
            {valor["Quantidade"]}
            {valor["Preço unitário"]}
            {valor["Total"]}""")
            condição = True
            
    if condição == False:
        print("Este produto não existe") 

while True:
    
        opção = int(input("""Escolha uma opção:
        [1] Adicionar produtos
        [2] Mostrar produtos
        [3] Buscar produtos
        [4] Alterar produtos 
        [5] Excluir produtos
        [6] Registrar vendas
        [7] Visualizar vendas
        [8] Buscar vendas
        [9] Sair"""))

        if opção < 1 or opção > 9:
            print("Erro: Escolha uma opção válida.")
        else:
            if opção == 1:
                
                id = Cadastrar_Produtos(id)

            elif opção == 2:
                Visualizar_Produtos() 

            elif opção == 3:
                Buscar_Produtos()

            elif opção == 4:
                Alterar_Produtos()

            elif opção == 5:
                Excluir_Produtos()

            elif opção == 6:
               id_venda = Registrar_Vendas(id_venda)


            elif opção == 7:
                Visualizar_Vendas()

            elif opção == 8:    
                Buscar_Vendas_Por_ID()

            elif opção == 9:
                break              
            