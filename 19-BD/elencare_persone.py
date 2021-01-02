import sqlite3

conn = sqlite3.connect("./19-BD/prove.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM persone")
conn.commit()

persone = cursor.fetchall()

for persona in persone:
    print("-----------")
    for dato in persona:
        print(f"{dato}")
print()

conn.close()
