"""
#import inserire_dati_prodotti
Aggiungendo l'importazione si eseguono anche gli script di quel file
ed aggiunge un altro profotto alla tabella prodotti 
"""
import sqlite3

# Connettere
#conn = sqlite_main.sqlite3.connect(sqlite_main.db)
db = './19-BD/prove.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS persone ("+
    "ID INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "Nome varchar(20), "+
    "Qualifica text"+
")")
conn.commit()

# Inserire dati
cursor.execute("INSERT INTO persone VALUES (null, 'Adrian Medina', 'CEO')")
conn.commit()

# Elencare prodotti
cursor.execute("SELECT * FROM persone")
persone = cursor.fetchall() # prende tutti i registri della tabella
for persona in persone:
    print("ID persona:",persona[0])
    print("Nome persona:",persona[1])
    print("Qualifica:",persona[2])
    print()

# close conn
conn.close()
