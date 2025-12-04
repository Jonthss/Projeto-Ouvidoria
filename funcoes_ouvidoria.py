from operacoesbd import *
import os
import time

# --- Funções Utilitárias ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_enter():
    input("\nPressione Enter para continuar...")

def exibir_menu():
    print("=" * 40)
    print("         Sistema de Ouvidoria")
    print("=" * 40)
    print("\nMenu de Opções:")
    print("1. Listagem das Manifestações")
    print("2. Criar uma nova Manifestação")
    print("3. Exibir quantidade de manifestações")
    print("4. Pesquisar uma manifestação por código")
    print("5. Deletar uma manifestação")
    print("6. Atualizar o status de uma manifestação")
    print("7. Sair do Sistema")
    print("-" * 40)

# --- Funções do Sistema ---

def listar_manifestacoes(conexao):
    limpar_tela()
    print("== Listagem de Manifestações ==\n")

    contar = "SELECT COUNT(*) FROM ouvidoria"
    contarBanco = listarBancoDados(conexao, contar)

    if contarBanco[0][0] == 0:
        print("Nenhuma manifestação registrada.")
    else:
        tudo = "select * from ouvidoria"
        todos_dados = listarBancoDados(conexao, tudo)
        print("Lista de manifestações no banco de dados: ")
        for item in todos_dados:
            print(f"Codigo: {item[0]} | Manifestação: {item[1]} | Status: {item[2]}")
    
    esperar_enter()


def criar_manifestacao(conexao):
    limpar_tela()
    print("== Criar Nova Manifestação ==\n")

    nova_manifestacao = input("Descreva a nova manifestação (ou 0 para sair): ")
    if nova_manifestacao == '0':
        return
    
    inserir = "INSERT INTO ouvidoria (problema) VALUES (%s)"
    dados = (nova_manifestacao,)
    insertNoBancoDados(conexao, inserir, dados)

   
    codigo = listarBancoDados(conexao, "SELECT LAST_INSERT_ID() FROM ouvidoria")[0][0]
    print("\nManifestação registrada com sucesso! O seu código é:", codigo)
    esperar_enter()




def contar_manifestacoes(conexao):
    limpar_tela()
    print("== Quantidade de Manifestações ==\n")
    
    contar = "SELECT COUNT(*) FROM ouvidoria"
    contarBanco = listarBancoDados(conexao, contar)
    
    total = contarBanco[0][0]
    if total == 0:
        print("Até o momento, o sistema não possui manifestações.")
    else:
        print(f"Até o momento, o sistema possui exatas {total} manifestações.")
    esperar_enter()




def pesquisar_manifestacao(conexao):
    contar = "SELECT COUNT(*) FROM ouvidoria"
    total = listarBancoDados(conexao, contar)[0][0]

    if total == 0:
        limpar_tela()
        print("== Pesquisar por Código ==\n")
        print("Nenhuma manifestação registrada para pesquisar.") 
        esperar_enter()
        return 

    while True:   
        try:
            limpar_tela()
            print("== Pesquisar por Código ==\n")
            
            entrada = input("Por favor, informe o código da manifestação (ou 0 para sair): ")
            if entrada == '0': return 

            codigo = int(entrada)
            
            pesquisa = "SELECT * FROM ouvidoria WHERE codigo = %s"
            dadosPesquisa = listarBancoDados(conexao, pesquisa, (codigo,))

            if dadosPesquisa: 
                print(f"\nA manifestação de código {codigo} é: {dadosPesquisa[0][1]}")
                print(f"Status atual: {dadosPesquisa[0][2]}")
                esperar_enter()
                return 
            else:
                print("\nCódigo inválido ou não encontrado. Tente novamente.")
                time.sleep(2)
                
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
            time.sleep(2)




def deletar_manifestacao(conexao):
    contar = "SELECT COUNT(*) FROM ouvidoria"
    total = listarBancoDados(conexao, contar)[0][0]

    if total == 0:
        limpar_tela()
        print("== Deletar uma Manifestação ==\n")
        print("Nenhuma manifestação registrada para deletar.")
        esperar_enter()
        return

    while True:
        try:
            limpar_tela()
            print("== Deletar uma Manifestação ==\n")
            
            entrada = input("Informe o código da manifestação que deseja deletar (ou 0 para sair): ")
            if entrada == '0': return

            codigo = int(entrada)

            pesquisaDeletar = "SELECT * FROM ouvidoria WHERE codigo = %s"
            dadosDeletar = listarBancoDados(conexao, pesquisaDeletar, (codigo,))

            if dadosDeletar:
                while True:
                    limpar_tela()
                    print(f"Você vai deletar: {dadosDeletar[0][1]}")
                    confirmar = input(f"\nTem certeza? (s/n): ").lower()
                    
                    if confirmar == 's':
                        deletar = "DELETE FROM ouvidoria WHERE codigo = %s"
                        excluirBancoDados(conexao, deletar, (codigo,))
                        print("\nManifestação deletada com sucesso.")
                        esperar_enter()
                        return
                    
                    elif confirmar == 'n':
                        print("\nOperação cancelada.")
                        time.sleep(1)
                        return 
                    
                    else:
                        print("\nEntrada inválida. Digite S ou N.")
                        time.sleep(2)
            else:
                print("\nCódigo não encontrado.")
                time.sleep(2)

        except ValueError:
            print("\nEntrada inválida.")
            time.sleep(2)
def atualizar_manifestacao(conexao):
    contar = "SELECT COUNT(*) FROM ouvidoria"
    total = listarBancoDados(conexao, contar)[0][0]

    if total == 0:
        limpar_tela()
        print("== Atualizar uma Manifestação ==\n")
        print("Nenhuma manifestação registrada para atualizar.")
        esperar_enter()
        return

    while True:
        try:
            limpar_tela()
            print("== Atualizar uma Manifestação ==\n")
            
            entrada = input("Informe o código da manifestação (ou 0 para sair): ")
            if entrada == '0': return
            codigo = int(entrada)

            pesquisa = "SELECT * FROM ouvidoria WHERE codigo = %s"
            dados = listarBancoDados(conexao, pesquisa, (codigo,))
            
            if dados:
                while True:
                    limpar_tela()
                    print(f"Manifestação: {dados[0][1]}")
                    print("\nOpções: 1-Fechado | 2-Encerrado | 3-Resolvido | 4-Em andamento | 5-Pendente")
                    
                    try:
                        novo_status_num = int(input(f"Informe o número do novo STATUS: "))
                        status_texto = ""

                        if novo_status_num == 1: status_texto = "fechado"
                        elif novo_status_num == 2: status_texto = "encerrado"
                        elif novo_status_num == 3: status_texto = "resolvido"
                        elif novo_status_num == 4: status_texto = "em andamento"
                        elif novo_status_num == 5: status_texto = "pendente"
                        else:
                            print("Opção inválida.")
                            time.sleep(2)
                            continue 
                        
                        atualizar = "UPDATE ouvidoria SET status = %s WHERE codigo = %s"
                        atualizarBancoDados(conexao, atualizar, (status_texto, codigo))
                        
                        print(f"\nManifestação atualizada para '{status_texto}'!")
                        esperar_enter()
                        return 

                    except ValueError:
                        print("\nDigite apenas o número.")
                        time.sleep(2)
            else:
                print("\nCódigo não encontrado.")
                time.sleep(2)

        except ValueError:
            print("\nCódigo inválido.")
            time.sleep(2)