'''
DATA: 02/09/2023 ÁS 17:09 
BY VINICIUSM

NECESSÁRIO INSTALAR AS DEPENDÊNCIAS COM O 'PIP'
'''

import mysql.connector #Biblioteca mysql para realizar a conexão
from mysql.connector import Error #Classe de erro

# Váriavel CONEXAO armeza os dados necessários para conectar ao banco.
conexao = mysql.connector.connect(
    host = "localhost", 
    database = "pessoas",
    user = "root",
    password = "Vn_2022#"
)

try: #Executa a conexao com o banco de dados de acordo com a variável conexao.
    
    if conexao.is_connected: #Se, a conexao estiver funcionando, ou seja, conectada ao banco de dados.
    
        print("\nConexão é segura: " , conexao.is_secure) #Mostra se a conexao é segura kkkkkkkk
        print("Host da conexão: " , conexao._host) #Pega host fornecido no ínicio do código

except Error as e:  #Se hoiver algum erro, except é excutado, e mostra qual erro ocorreu.
    print("Ocorreu um erro: ", e)

finally: #Executado de qualquer forma, faz a desconexao com o banco de dados.
    conexao.disconnect()
    print("Conexão encerrada com o banco de dados!!\n")


    