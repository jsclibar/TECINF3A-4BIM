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
    
    while True:
            print("\n=== MENU ===")
            print("1) Inserir novo professor")
            print("2) Inserir novo aluno")
            print("0) Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                print("\n--- Cadastro de Professor ---")
                nome = input("Nome: ").strip()
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F): ").strip().upper()
                telefone = input("Telefone: ").strip()
                endereco = input("Endereço: ").strip()
                data_admissao = input("Data de admissão (AAAA-MM-DD): ").strip()
                salario = float(input("Salário: ").replace(",", "."))
                area = input("Área de atuação: ").strip()
                ativo_sn = int(input("Ativo (1=Sim / 0=Não): "))

                sql_prof = """
                    INSERT INTO professor (nome, idade, sexo, telefone, endereco, data_admissao, salario, area, ativo_sn)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                dados_prof = (nome, idade, sexo, telefone, endereco, data_admissao, salario, area, ativo_sn)
                inserir_registro(conexao, sql_prof, dados_prof, "professor")

            elif opcao == "2":
                print("\n--- Cadastro de Aluno ---")
                nome = input("Nome: ").strip()
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F): ").strip().upper()
                telefone = input("Telefone: ").strip()
                endereco = input("Endereço: ").strip()
                curso = input("Curso: ").strip()
                data_matricula = input("Data de matrícula (AAAA-MM-DD): ").strip()
                ativo_sn = int(input("Ativo (1=Sim / 0=Não): "))

                sql_aluno = """
                    INSERT INTO aluno (nome, idade, sexo, telefone, endereco, curso, data_matricula, ativo_sn)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                dados_aluno = (nome, idade, sexo, telefone, endereco, curso, data_matricula, ativo_sn)
                inserir_registro(conexao, sql_aluno, dados_aluno, "aluno")

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")


# Caso ocorra algum problema (senha errada, banco inexistente, etc.), o erro é exibido
except Error as e:
    print(f"Erro ao conectar ou inserir dados: {e}")

finally:  # O finally garante que a conexão será fechada
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada com o banco de dados.")