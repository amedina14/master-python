# Importare sqlite DB
import sqlite3

# Connessione
connessione = sqlite3.connect('./19-BD/prove.db')

# Creare indice: Permette eseguire le query
cursor = connessione.cursor()

# Creare tabella
cursor.execute("CREATE TABLE IF NOT EXISTS prodotti("+
    "ID INTEGER(15) PRIMARY KEY AUTOINCREMENT, "+
    "Titolo varchar(20), "+
    "Descrizione text, "+
    "Prezzo int(50)"+
")")

# Salvare cambi
connessione.commit()

# Chiudere la connessione altrimenti non si salvano i cambi
connessione.close()