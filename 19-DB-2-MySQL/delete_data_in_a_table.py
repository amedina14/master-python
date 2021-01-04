import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

cursor = conn.cursor(buffered=True)

cursor.execute("DELETE FROM veicoli WHERE Marca = 'Ford'")
conn.commit()

righe_eliminate = cursor.rowcount
print(righe_eliminate,"righe eliminate")

conn.close()