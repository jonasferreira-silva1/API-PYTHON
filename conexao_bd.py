import psycopg2

def getConnectionPostegre():
    return psycopg2.connect(
        host='localhost',
        user='postgres',
        password='jonas1385',
        database='api',
    )

# Obtém a conexão
connection = getConnectionPostegre()

# Fecha a conexão
connection.close()

print("Conexão funcionando")
