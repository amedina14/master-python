import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

cursor = conn.cursor(buffered=True) # permette di usare lo stesso cursor più volte

# Aggiorna prezzo del modello Arona
cursor.execute("UPDATE veicoli SET Prezzo=17500.2 WHERE Modello='Arona'")
conn.commit()

record_aggiornati = cursor.rowcount
print(f"{record_aggiornati} record aggiornati")

conn.close()