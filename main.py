# JONATHAS BARBOSA DE OLIVEIRA - Projeto Ouvidoria - Etapa 2

from operacoesbd import criarConexao
from ouvidoria import * 

conexao = criarConexao('localhost','root','88558514', 'locadora_guylherme')

while True:
    limpar_tela()
    exibir_menu()
    
    escolha = input("Escolha uma opção (1-7): ")

    if escolha == '1':
        listar_manifestacoes(conexao)

    elif escolha == '2':
        criar_manifestacao(conexao)

    elif escolha == '3':
        contar_manifestacoes(conexao)

    elif escolha == '4':
        pesquisar_manifestacao(conexao)

    elif escolha == '5':
        deletar_manifestacao(conexao)
    
    elif escolha == '6':
        atualizar_manifestacao(conexao)

    elif escolha == '7':
        limpar_tela()
        print("="*40)
        print("      Saindo do sistema. Até logo!")
        print("="*40)
        conexao.close() 
        break
    
    else:
        print("\nOpção inválida.")
        time.sleep(1.5)