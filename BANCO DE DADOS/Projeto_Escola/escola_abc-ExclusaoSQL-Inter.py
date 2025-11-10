# Recomendado a criação de um ambiente virtual para só depois instalar os pacotes abaixo:

# Via pip, instale os seguintes pacotes:
# pip install mysql-connector-python
# pip install pandas

import mysql.connector  # Biblioteca para conectar ao banco MySQL
from mysql.connector import Error  # Classe usada para tratar erros do MySQL

# Função para exclusão de registro


def excluir_registro(conexao, sql, valores, descricao):
    """
    Executa um comando DELETE no banco de dados.
    - conexao: conexão ativa com o MySQL
    - sql: comando SQL com placeholders (%s)
    - valores: dados usados na condição do WHERE
    - descricao: texto para exibição (ex.: 'professor', 'aluno')
    """
    cursor = conexao.cursor()  # Cria o cursor, que envia comandos SQL ao banco
    # Executa o comando DELETE com os valores informados
    cursor.execute(sql, valores)
    conexao.commit()  # Confirma a exclusão no banco

    if cursor.rowcount == 0:
        print(
            f"\nNenhum {descricao} encontrado com os critérios informados.\n")
    else:
        print(f"\n{descricao.capitalize()} excluído com sucesso!\n")

    cursor.close()  # Fecha o cursor após o uso


try:  # O bloco try tenta criar uma conexão com o banco MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola_abc"
    )

    # Confirma se a conexão foi realmente estabelecida antes de continuar
    if conexao.is_connected():
        print("Conexão realizada com sucesso com o banco 'escola_abc'!")

    while True:
        print("\n=== MENU DE EXCLUSÃO ===")
        print("1) Excluir ALUNO por ID")
        print("0) Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                id_para_excluir = int(
                    input("Digite o ID do aluno a ser excluído: ").strip())
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
                continue

            sql_delete_aluno = """
                    DELETE FROM aluno
                    WHERE id_aluno = %s
                """
            dados_delete = (id_para_excluir,)
            excluir_registro(conexao, sql_delete_aluno, dados_delete, "aluno")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar ou excluir dados: {e}")

finally:  # O finally garante que a conexão será fechada mesmo em caso de erro
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")
