import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM prodotti WHERE Prezzo < 5")
conn.commit()

prodotti_economici = cursor.fetchall()
print("---- VOLANTINO DELLA CONVENIENZA (prezzi sotto ai 5 €) ----")
for prodotto in prodotti_economici:
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