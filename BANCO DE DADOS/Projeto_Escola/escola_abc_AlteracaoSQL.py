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

    # Comando UPDATE com placeholders (%s) para segurança
    sql_update_prof = """
        UPDATE professor
        SET salario = %s, area = %s
        WHERE nome = %s
    """

    # Novos dados que serão aplicados no registro (salário, área e nome do professor)
    dados_update = (5500.00, "Literatura", "Cláudia Moreira")

    # Chama a função criada anteriormente para realizar a atualização
    atualizar_registro(conexao, sql_update_prof, dados_update, "professor")

# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar ou atualizar dados: {e}")

finally:  # O finally garante que a conexão será fechada mesmo em caso de erro
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")
