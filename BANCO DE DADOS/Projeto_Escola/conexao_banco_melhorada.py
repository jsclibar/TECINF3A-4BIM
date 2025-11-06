import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escola_abc"
    )

    if conexao.is_connected():
        print("Conexão realizada com sucesso com o banco 'escola_abc'!")

except Error as e:
    print(f"Erro ao conectar: {e}")

finally:  # O finally garante que a conexão será fechada mesmo se ocorrer erro
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")
