
def Cadastrar_Produto(valor):
    try:    
        while True:
            nome = input("Digite o nome do produto: ").strip()
            if nome == "": 
                print("Erro: É necessário digitar um nome.")
            else:
                break  

        while True:
            categoria_escolhida = int(input("Digite a categoria: [1] Camiseta | [2] Calça | [3] Calçados | [4] Acessórios"))
            categoria = ""
        
            if categoria_escolhida != 1 and categoria_escolhida != 2 and categoria_escolhida != 3 and categoria_escolhida != 4:
                print("Erro: Digite uma opção válida.")
        
            else:   
        
                if categoria_escolhida == 1:
                    categoria = "Camiseta"
                    break

                elif categoria_escolhida == 2:
                    categoria = "Calça"
                    break

                elif categoria_escolhida == 3:
                    categoria = "Calçados"
                    break

                elif categoria_escolhida == 4:
                    categoria = "Acessórios"
                    break

        while True:
            if categoria == "Camiseta":
                tamanho_escolhido = int(input("""Escolha o tamanho: 
                [1] P
                [2] M
                [3] G
                [4] GG """))

                if tamanho_escolhido != 1 and tamanho_escolhido != 2 and tamanho_escolhido != 3 and tamanho_escolhido != 4:
                    print("Erro: Escolha uma opção válida.")

                else:
                        if tamanho_escolhido == 1:
                            tamanho = "P"
                            break

                        elif tamanho_escolhido == 2:
                            tamanho = "M"
                            break

                        elif tamanho_escolhido == 3:
                            tamanho = "G"  
                            break

                        elif tamanho_escolhido == 4:
                            tamanho = "GG"
                            break

            elif categoria == "Calça":
                tamanho_escolhido = int(input("""Escolha o tamanho: 
                [1] 38
                [2] 40
                [3] 42
                [4] 44 """))
                        
                if tamanho_escolhido != 1 and tamanho_escolhido != 2 and tamanho_escolhido != 3 and tamanho_escolhido != 4:
                        print("Erro: Escolha uma opção válida.")
                        
                else:
                        if tamanho_escolhido == 1:
                            tamanho = 38
                            break

                        elif tamanho_escolhido == 2:
                            tamanho = 40
                            break

                        elif tamanho_escolhido == 3:
                            tamanho = 42 
                            break

                        elif tamanho_escolhido == 4:
                            tamanho = 44     
                            break

            elif categoria == "Calçados":
                tamanho_escolhido = int(input("""Escolha o tamanho: 
                [1] 38
                [2] 39
                [3] 40
                [4] 41 """))
        
                if tamanho_escolhido != 1 and tamanho_escolhido != 2 and tamanho_escolhido != 3 and tamanho_escolhido != 4:
                    print("Erro: Escolha uma opção válida")
        
                else:
                    if tamanho_escolhido == 1:
                        tamanho = "38"
                        break
        
                    elif tamanho_escolhido == 2:
                        tamanho = "39"
                        break       
        
                    elif tamanho_escolhido == 3:
                        tamanho = "40"  
                        break
        
                    elif tamanho_escolhido == 4:
                        tamanho = "41"        
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
        id = 0
        id += valor
        Adicionar_Produto(id, nome, categoria, tamanho, preço, estoque)    
    




Produtos = {}
def Adicionar_Produto(id, nome, categoria, tamanho, preço, estoque):
    
        Produtos[f"Produto{id}"] = {
            "ID": id,
            "Nome": nome,
            "Categoria": categoria,
            "Tamanho": tamanho,
            "Preço": preço,
            "Estoque": estoque
            
}


while True:
    while True:
        opção = int(input("""Escolha uma opção:
        [1] Adicionar produto
        [2] Mostrar produto
        [3] Sair """))

        if opção != 1 and opção != 2  and opção != 3:
            print("Erro: Escolha uma opção válida.")
        else:
            if opção == 1:
                valor = 1
                Cadastrar_Produto(valor)

            elif opção == 2:
                print(Produtos)  

    if opção == 3:
        break          