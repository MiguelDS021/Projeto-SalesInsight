Produtos = {}
def Adicionar_Produto(id, nome, categoria, preço, estoque, tamanho):
    
        Produtos[f"Produto{id}"] = {
            "ID": id,
            "Nome": nome,
            "Categoria": categoria,
            "Preço": preço,
            "Estoque": estoque,
            "Tamanho": tamanho
}


id = 0
while True:
   
        opção = int(input("""Escolha uma opção:
        [1] Adicionar produto
        [2] Sair """))

        if opção == 1:
        
            try: 
                while True:
                    nome = input("Digite o nome do produto: ").strip()
                    if nome == "": 
                        print("Erro: É necessário digitar um nome.")
                    else:
                        break  

                while True:
                    categoria_escolhida = int(input("Digite a categoria: [1] Camiseta | [2] Calça | [3] Calçados | [4] Acessórios")).strip()

                    if categoria_escolhida != 1 and categoria_escolhida != 2 and categoria_escolhida != 3 and categoria_escolhida != 4:
                
                        print("Erro: Digite uma opção válida.")

                    else:
                        break    

                for i in categoria_escolhida:

                    if i == 1:
                        categoria = "Camiseta"

                    elif categoria_escolhida == 2:
                        categoria = "Calça"

                    elif categoria_escolhida == 3:
                        categoria = "Calçados"

                    elif categoria_escolhida == 4:
                        categoria = "Acessórios"        
                
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
                
                tamanho = input("Digite o tamanho: ")

            

            except ValueError:
                print("Erro: Em preço só é permitido números decimais e em estoque números inteiros.")    

              
            else:  
                id += 1
                Adicionar_Produto(id, nome, categoria, preço, estoque, tamanho)

        elif opção == 2:
            break        