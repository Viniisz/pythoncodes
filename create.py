'''
DATA: 02/09/2023 ÁS 17:11
BY VINICIUSM

NECESSÁRIO INSTALAR AS DEPENDÊNCIAS COM O 'PIP'
'''

import mysql.connector # Biblioteca mysql para realizar a conexão
from mysql.connector import Error # Classe de erro

# Váriavel CONEXAO armeza os dados necessários para conectar ao banco.
conexao = mysql.connector.connect(
    host = "localhost",
    database =  "pessoas",
    user = "root",
    password = "Vn_2022#"
)
# Executa a conexao com o banco de dados de acordo com a variável conexao.
if conexao.is_connected():
    
    print("\nConectado ao banco de dados!")
    sqlCreate = """INSERT INTO pessoa (nome, snome, pais) 
    VALUES('renan', 'gabriel', 'brasil');"""

    cursor = conexao.cursor()
    cursor.execute(sqlCreate)

    print("\nDados inseridos na tabela\n")

    cursor.close()
    conexao.close()

else:
    print("Ocorreu um erro: ", Error)

