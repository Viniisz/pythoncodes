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

if conexao.is_connected():
    
    print("\n Conectado ao banco de dados!!")
    sqlUpdate = """ UPDATE pessoa SET data_reg = '2023/09/05' WHERE id = 1; """
    
    cursor = conexao.cursor()
    cursor.execute(sqlUpdate)

    print("\nOs dados foram atualizados!!")

    cursor.close()
    conexao.close()

else:
    print("Ocorreu um erro!!")
