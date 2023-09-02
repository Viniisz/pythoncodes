'''
DATA: 02/09/2023 ÁS 17:11
BY VINICIUSM

NECESSÁRIO INSTALAR AS DEPENDÊNCIAS COM O 'PIP'
'''

import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
    host = "localhost",
    database = "pessoas",
    user = "root",
    password = "Vn_2022#"    
)

    if con.is_connected():
        db_info = con.get_server_info()
        print("informações do banco de dados ", db_info)
        
        sqlSelect = "SELECT * FROM pessoa;"
        cursor = con.cursor()
        cursor.execute(sqlSelect)

        records = cursor.fetchall()

        print("\nDados na tabela: \n")
        
        for record in records:
            print(record)
    
    print("\n")
    
except Error as e:
    print("Ocorreu um erro: ", e)

finally:
    con.close()
    cursor.close()
    print("Conexão com banco de dados encerrada!!\n")
