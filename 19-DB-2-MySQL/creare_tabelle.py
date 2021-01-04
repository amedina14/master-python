import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port="3308",
    database="master_python"
)

cursor = database.cursor()

# Creare tabella
cursor.execute("""
CREATE TABLE IF NOT EXISTS veicoli (
    Id int(10) auto_increment not null,
    Marca varchar(20) not null,
    Modello varchar(30) not null,
    Prezzo float(10,2) not null,
    CONSTRAINT pk_veicolo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

database.close()