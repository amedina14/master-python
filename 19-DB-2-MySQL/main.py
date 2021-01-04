import mysql.connector

# Connettere a mysql
database = mysql.connector.Connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

# Verificare la connessione con mysql.connector
print(database)

# Crea cursore che permette realizzare query
cursor = database.cursor()

# Crea db
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Mostra la lista dei bd
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
"""
"""

# Chiudere connessione
database.close()
