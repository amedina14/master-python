import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

dipendenti = [
    ("Sofia","commessa"),
    ("Diego","tecnico"),
    ("Lucia","cassiera"),
    ("Luca","Magazziniere"),
    ("Pablo","Capo reparto")
]

cursor.executemany("INSERT INTO persone VALUES (null,?,?)", dipendenti)
conn.commit()

conn.close()