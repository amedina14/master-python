import sqlite3
"""
Come ottenere il primo prodotto della tabella prodotti
"""

# Prima si realizza la connessione e si crea il cursore
conn = sqlite3.connect("./19-BD/prove.db")
cursor = conn.cursor()

# Poi si fa la query e si salvano i cambi
cursor.execute("SELECT * FROM prodotti")
conn.commit()

# Si applica il comando per il primo prodotto e si stampa su console
primo_prodotto = cursor.fetchone()
print("----------------\nStampato sotto forma di tupla:", primo_prodotto)

# Stampato dato per dato singolo
print("----------------")
for prodotto in primo_prodotto:
    print(f"{primo_prodotto.index(prodotto)}: {prodotto}")
print()

# Infine si chiude la connesione
conn.close()

"""
Domanda: 
Come ottenere il nome dei campi di una tabella da iterare e stampare in un elenco?
"""