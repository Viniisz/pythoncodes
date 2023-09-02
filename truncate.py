'''
DATA: 02/09/2023 ÁS 17:11
BY VINICIUSM

NECESSÁRIO INSTALAR AS DEPENDÊNCIAS COM O 'PIP'
'''

import mysql.connector
from mysql.connector import Error

conexao = mysql.connector.connect(
    host = "localhost",
    database = "pessoas",
    user = "root",
    password = "Vn_2022#"
)

print("\n")
if conexao.is_connected():
    
    print("Conectado ao banco de dados!!")
    sqlTruncate = "TRUNCATE pessoa;"
    
    cursor = conexao.cursor()
    cursor.execute(sqlTruncate)

    print("\nOs dados foram apagdos da tabela!!")
    print("\n")

    conexao.close()
    cursor.close()

else:
    print("", Error)    
