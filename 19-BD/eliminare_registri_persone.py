import sqlite3

conn = sqlite3.connect("19-BD/prove.db")
cursor = conn.cursor()

#cursor.execute("DELETE FROM persone WHERE ID > 1 AND ID < 5")
#cursor.execute("DELETE FROM persone WHERE Nome='Adrian Medina'")
cursor.execute("DELETE FROM persone")
conn.commit()

conn.close()