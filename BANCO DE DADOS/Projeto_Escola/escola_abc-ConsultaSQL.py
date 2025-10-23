import mysql.connector  # Biblioteca para conectar ao banco MySQL
from mysql.connector import Error  # Classe usada para tratar erros do MySQL
import pandas as pd  # Biblioteca para manipular e exibir dados em formato de tabela


def consultar_tabela(conexao, sql, titulo):

    cursor = conexao.cursor()  # Cria o cursor, que envia comandos SQL ao banco
    cursor.execute(sql)  # Executa a consulta recebida como parâmetro
    resultados = cursor.fetchall()  # Busca todos os registros retornados pela consulta

    if not resultados:
        print(f"Nenhum registro encontrado em {titulo}.\n")
    else:
        # Traz os nomes e tipos das colunas retornadas
        descricao_colunas = cursor.description
        colunas = []  # Cria uma lista vazia para guardar os nomes

        for desc in descricao_colunas:  # Percorre cada coluna descrita
            # O primeiro item da tupla é o nome da coluna
            nome_coluna = desc[0]
            colunas.append(nome_coluna)  # Adiciona o nome à lista de colunas

        # Cria uma tabela do pandas
        df = pd.DataFrame(resultados, columns=colunas)
        print(f"\n{titulo}:\n")  # Mostra o título da consulta
        # Exibe o DataFrame como texto, sem o índice
        print(df.to_string(index=False))

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

        # Chama a função criada anteriormente
        consultar_tabela(conexao, "SELECT * FROM aluno", "Alunos cadastrados")
        consultar_tabela(
            conexao, "SELECT * FROM professor where nome like 'A%'", "Professores cadastrados")

# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar: {e}")

finally:  # O finally garante que a conexão será fechada mesmo se ocorrer erro
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")
