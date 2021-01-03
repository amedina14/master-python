import mysql.connector

database = mysql.connector.Connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

# Verificare la connessione con mysql.connector
print(database)

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
"""
"""
