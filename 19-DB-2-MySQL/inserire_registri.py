import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port="3308",
    database="master_python"
)

cursor = database.cursor()

# Inserire singolo registro
cursor.execute("""
INSERT INTO veicoli VALUES (null, 'Fiat', '500x', 20100)
""")

# Inserire multipli registri
concessionario_macchine = [
    ("Mercedes","Classe A",26500),
    ("Jeep","Wrangler",18000),
    ("Seat","Arona",17758.2),
    ("Ford","Puma",20024.9)
]

cursor.executemany("""
INSERT INTO veicoli VALUES (null,%s,%s,%s)
""",concessionario_macchine)
database.commit()

database.close()

"""
Verificare i dati inseriti sul DB PhpMyAdmin

1
Fiat
500x
20100.00

2
Mercedes
Classe A
26500.00

3
Jeep
Wrangler
18000.00

4
Seat
Arona
17758.20

5
Ford
Puma
20024.90
"""