# Recomendado a criação de um ambiente virtual para só depois instalar os pacotes abaixo:

# Via pip, instale os seguintes pacotes:
# pip install mysql-connector-python
# pip install pandas

import mysql.connector  # Biblioteca para conectar ao banco MySQL
from mysql.connector import Error  # Classe usada para tratar erros do MySQL

# Função para atualização de registro


def atualizar_registro(conexao, sql, valores, descricao):
    """
    Executa um comando UPDATE no banco de dados.
    - conexao: conexão ativa com o MySQL
    - sql: comando SQL com placeholders (%s)
    - valores: dados a serem usados na atualização
    - descricao: texto de apoio (ex.: 'professor', 'aluno')
    """
    cursor = conexao.cursor()  # Cria o cursor, que envia comandos SQL ao banco
    # Executa o comando SQL com os valores fornecidos
    cursor.execute(sql, valores)
    conexao.commit()  # Confirma a alteração no banco

    if cursor.rowcount == 0:
        print(
            f"\nNenhum {descricao} encontrado com os critérios informados.\n")
    else:
        print(f"\n{descricao.capitalize()} atualizado com sucesso!\n")

    cursor.close()  # Fecha o cursor após o uso


try:  # O bloco try tenta criar uma conexão com o banco MySQL
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola_abc"
    )

    # Confirma se a conexão foi estabelecida com sucesso antes de continuar
    if conexao.is_connected():
        print("Conexão realizada com sucesso com o banco 'escola_abc'!")

    while True:
        print("\n=== MENU DE ATUALIZAÇÃO ===")
        print("1) Atualizar professor")
        print("2) Atualizar aluno")
        print("0) Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- Atualização de Professor ---")
            nome = input("Nome do professor a ser atualizado: ").strip()

            # Coleta novos dados
            novo_salario = float(input("Novo salário: ").replace(",", "."))
            nova_area = input("Nova área de atuação: ").strip()

            sql_update_prof = """
                    UPDATE professor
                    SET salario = %s, area = %s
                    WHERE nome = %s
                """
            dados_update = (novo_salario, nova_area, nome)
            atualizar_registro(conexao, sql_update_prof,
                               dados_update, "professor")

        elif opcao == "2":
            print("\n--- Atualização de Aluno ---")
            nome = input("Nome do aluno a ser atualizado: ").strip()

            ativo_sn = int(input("Ativo (1=Sim / 0=Não): "))

            sql_update_aluno = """
                    UPDATE aluno
                    SET ativo_sn = %s
                    WHERE nome = %s
                """
            dados_update_aluno = (ativo_sn, nome)
            atualizar_registro(conexao, sql_update_aluno,
                               dados_update_aluno, "aluno")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Chama a função criada anteriormente para realizar a atualização
    atualizar_registro(conexao, sql_update_prof, dados_update, "professor")

# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar ou atualizar dados: {e}")

finally:  # O finally garante que a conexão será fechada mesmo em caso de erro
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")
