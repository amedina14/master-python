import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

cursor.execute("UPDATE prodotti SET Prezzo = Prezzo - 1 WHERE Prezzo >= 5 AND Prezzo <= 40")
cursor.execute("SELECT * FROM prodotti WHERE Prezzo >= 5 AND Prezzo <= 40")
conn.commit()
offerte = cursor.fetchall()
print("---- VOLANTINO DELLE OFFERTE ----")
for prodotto in offerte:
    print("-------- --------")
    for dato in prodotto:
        if prodotto.index(dato) == 0:
            print(f"Id: {dato}")
        elif prodotto.index(dato) == 1:
            print(f"Prodotto: {dato}")
        elif prodotto.index(dato) == 2:
            print(f"Descrizione: {dato}")
        elif prodotto.index(dato) == 3:
            print(f"Prezzo: {dato}")
print()

conn.close()