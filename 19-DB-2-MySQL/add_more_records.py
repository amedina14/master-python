import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

cursor = conn.cursor(buffered=True)

cursor.execute("INSERT INTO veicoli VALUES (null,'Ford','Puma',20024.9)")
conn.commit()

conn.close()