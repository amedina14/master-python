import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

forniture = [
    ("Acqua","S.Pellegrino leggermente frizzante",3),
    ("Limone","Battaglio siciliani",4),
    ("Liquore","Italiano Disaronno",40),
    ("Succo Santal","Cocco e Ananas",2),
    ("Carne","Fettine scelte di bovino adulto",9),
    ("Maiale","lonza/arista di suino a tranci |-32% 140",5),
    ("Salsicce","salsiccia di suino -23% 1,20",6)
]

cursor.executemany("INSERT INTO prodotti VALUES (null,?,?,?)", forniture)
conn.commit()

conn.close()