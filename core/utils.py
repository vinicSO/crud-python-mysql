import MySQLdb

def conectar():
    """
    Função para conectar ao servidor
    :return: conn
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='vinic',
            password='vinic'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')