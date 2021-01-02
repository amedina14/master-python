import sqlite3
"""
Come i prodotti della tabella prodotti
"""

# Prima si realizza la connessione e si crea il cursore
conn = sqlite3.connect("./19-BD/prove.db")
cursor = conn.cursor()

# Poi si fa la query e si salvano i cambi
cursor.execute("SELECT * FROM prodotti")
conn.commit()

# Si applica il comando per il primo prodotto e si stampa su console
elenco_prodotti = cursor.fetchall()

# Stampato dato per dato singolo
for prodotto in elenco_prodotti:
    print("----------------")
    for dato in prodotto:
        print(f"{prodotto.index(dato)}: {dato}")
print()

# Infine si chiude la connesione
conn.close()

"""
Domanda: 
Come ottenere il nome dei campi di una tabella da iterare e stampare in un elenco?
"""