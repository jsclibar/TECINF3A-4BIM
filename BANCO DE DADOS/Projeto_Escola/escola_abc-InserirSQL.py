# Recomendado a criação de um ambiente virtual para só depois instalar os pacotes abaixo:

# Via pip, instale os seguintes pacotes:
# pip install mysql-connector-python
# pip install pandas

import mysql.connector  # Biblioteca para conectar ao banco MySQL
from mysql.connector import Error  # Classe usada para tratar erros do MySQL

# função para inserção de registro


def inserir_registro(conexao, sql, valores, descricao):

    cursor = conexao.cursor()  # Cria o cursor, que envia comandos SQL ao banco
    # Executa o isert SQL com os respectivos dados
    cursor.execute(sql, valores)
    conexao.commit()  # realizada a gravação no banco
    print(f"\n{descricao.capitalize()} inserido com sucesso!\n")
    cursor.close()  # Fecha o cursor após o uso


try:  # O bloco try tenta criar uma conexão com o banco MySQL usando as credenciais informadas
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola_abc"
    )

    # Confirma se a conexão foi realmente estabelecida antes de continuar.
    if conexao.is_connected():
        print("Conexão realizada com sucesso com o banco 'escola_abc'!")

    # Comando INSERT INTO <tabela> (campos). Usamos o placeholder %s por segurança, evitando ataques de SQL Injection
    sql_prof = """
            INSERT INTO professor (nome, idade, sexo, telefone, endereco, data_admissao, salario, area, ativo_sn)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Dados que serão enviados ao banco junto com o comando SQL INSERT INTO
    dados_prof = (
        "Cláudia Moreira", 38, "F", "98888-1122",
        "Av. Central, 100", "2024-03-20", 5200.00, "Português", 1
    )

    # Chama a função criada anteriormente para realizar a inserção do novo registro
    inserir_registro(conexao, sql_prof, dados_prof, "professor")

# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar ou inserir dados: {e}")

finally:  # O finally garante que a conexão será fechada
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")