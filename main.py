id = 0
categorias = ["Camisetas", "Calças", "Calçados", "Acessórios"]
camiseta = ["P", "M", "G", "GG"]
calça = [38, 40, 42, 44]
calçados = [38, 39, 40, 42]

def Cadastrar_Produtos(id):
    try:    
        while True:
            nome = input("Digite o nome do produto: ").strip()
            if nome == "": 
                print("Erro: É necessário digitar um nome.")
            else:
                break  

        while True:
            cat_escolha = int(input("Digite a categoria: [1] Camiseta | [2] Calça | [3] Calçados | [4] Acessórios"))
            
        
            if cat_escolha < 1 or cat_escolha > 4:
                print("Erro: Digite uma opção válida.")
        
            else:   
                categoria = categorias[cat_escolha-1]
                break

        while True:
            if categoria == "Camisetas":
                escolha = int(input("""Escolha o tamanho: 
                [1] P
                [2] M
                [3] G
                [4] GG """))

                if escolha < 1 or escolha > 4:
                    print("Erro: Escolha uma opção válida.")

                else:
                    tamanho = camiseta[escolha-1]
                    break

            elif categoria == "Calças":
                escolha2 = int(input("""Escolha o tamanho: 
                [1] 38
                [2] 40
                [3] 42
                [4] 44 """))
                        
                if escolha2 < 1 or escolha2 > 4:
                    print("Erro: Escolha uma opção válida.")
                        
                else:
                    tamanho = calça[escolha2-1]
                    break

            elif categoria == "Calçados":
                escolha3 = int(input("""Escolha o tamanho: 
                [1] 38
                [2] 39
                [3] 40
                [4] 41 """))
        
                if escolha3 < 1 or escolha3 > 4:
                    print("Erro: Escolha uma opção válida")
        
                else:
                    tamanho= calçados[escolha3-1]
                    break

            elif categoria == "Acessórios":
                tamanho = "Único"
                break

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




while True:
    
        opção = int(input("""Escolha uma opção:
        [1] Adicionar produtos
        [2] Mostrar produtos
        [3] Buscar produtos
        [4] Sair """))

        if opção < 1 or opção > 4:
            print("Erro: Escolha uma opção válida.")
        else:
            if opção == 1:
                
                id = Cadastrar_Produtos(id)

            elif opção == 2:
                Visualizar_Produtos() 

            elif opção == 3:
                Buscar_Produtos()

            elif opção == 4:
                break              
            