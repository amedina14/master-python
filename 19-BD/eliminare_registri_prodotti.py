import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM prodotti WHERE Titolo = 'Latte'")
conn.commit()

conn.close()