# Importare sqlite DB
import sqlite3

# Connessione
db = './19-BD/prove.db'
connessione = sqlite3.connect(db)

# Creare indice: Permette eseguire le query
cursor = connessione.cursor()

# Creare tabella
cursor.execute("CREATE TABLE IF NOT EXISTS prodotti("+
    "ID INTEGER PRIMARY KEY AUTOINCREMENT, "+
    "Titolo varchar(20), "+
    "Descrizione text, "+
    "Prezzo int(50)"+
")")

# Inserire dati
cursor.execute("INSERT INTO prodotti VALUES (null, 'Latte', 'Granarolo parzialmente scremato', 2)")
connessione.commit()

# Elencare dati
cursor.execute("SELECT * FROM prodotti")
prodotti = cursor.fetchall()

for prodotto in prodotti:
    print("Id:", prodotto[0])
    print("Tipo:", prodotto[1])
    print("Descrizione:", prodotto[2])
    print("Prezzo:", prodotto[3])
    print()

# Salvare cambi
connessione.commit()

# Chiudere la connessione altrimenti non si salvano i cambi
connessione.close()