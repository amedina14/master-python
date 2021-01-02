import sqlite3

conn = sqlite3.connect("./19-BD/prove.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM persone")
conn.commit()

persone = cursor.fetchall()

for persona in persone:
    print("-----------")
    for dato in persona:
        if persona.index(dato) == 0:
            print(f"ID: {dato}")
        elif persona.index(dato) == 1:
            print(f"Nome: {dato}")
        elif persona.index(dato) == 2:
            print(f"Qualifica: {dato}")
print()

conn.close()
