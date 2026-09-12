from produtos import (Cadastrar_Produtos, 
                      Visualizar_Produtos, 
                      Buscar_Produtos, 
                      Alterar_Produtos, 
                      Excluir_Produtos
)

from vendas import (
    Registrar_Vendas,
    Visualizar_Vendas,
    Buscar_Vendas_Por_ID
)

from analise import Analisar_Vendas

id = 0
id_venda = 0
while True:
    
    try:
        opção = int(input("""Escolha uma opção:
        [1] Adicionar produtos
        [2] Mostrar produtos
        [3] Buscar produtos
        [4] Alterar produtos
        [5] Excluir produtos
        [6] Registrar vendas
        [7] Visualizar vendas
        [8] Buscar vendas
        [9] Analisar vendas
        [10] Sair"""))
    except ValueError:
        print("ERRO: Digite apenas números.")
        continue
    if opção < 1 or opção > 10:
        print("Erro: Escolha uma opção válida.")
    
    elif opção == 1:
                
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
        Analisar_Vendas()

    elif opção == 10:
        break              
            