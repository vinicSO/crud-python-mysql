import MySQLdb

def conectar():
    """
    Função para conectar ao servidor
    :return connection:
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

def desconectar(conn):
    """
    Função para desconectar do servidor
    :param conn:
    :return:
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    :return:
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produto;')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print('Listando produtos..')
        print('-------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'NOME: {produto[1]}')
            print(f'PREÇO: {produto[2]}')
            print(f'ESTOQUE: {produto[3]}')
            print('-------------------')
    else:
        print('Não possui registros')
    desconectar(conn)