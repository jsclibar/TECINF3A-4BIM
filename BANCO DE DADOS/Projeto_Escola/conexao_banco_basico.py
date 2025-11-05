import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola_abc"
)

if conexao.is_connected():
    print("Conexão realizada com sucesso com o banco 'escola_abc'!")

cursor = conexao.cursor()
cursor.execute('SELECT * FROM ALUNO WHERE ativo_sn = 2')
resultados = cursor.fetchall()

if not resultados == True:
    print('DADOS NÃO ENCONTRADOS!!!')

for i in resultados:
    print(i)

conexao.close()
