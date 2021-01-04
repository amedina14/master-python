import mysql.connector

def trattini():
    for trattino in range(57):
        print("-",end="")
    print()

connessione = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3308,
    database="master_python"
)

cursor = connessione.cursor()


cursor.execute("SELECT * FROM veicoli")
macchine = cursor.fetchall() # Rende a macchine una tabella con tutti i campi

#connessione.commit()
print("\n#### Tutte le macchine - TUPLE 1D ####")
for macchina in macchine:
    print(macchina)
print()
"""
#### Tutte le macchine - TUPLE 1D ####
(1, 'Fiat', '500x', 20100.0)
(2, 'Mercedes', 'Classe A', 26500.0)
(3, 'Jeep', 'Wrangler', 18000.0)
(4, 'Seat', 'Arona', 17758.2)
(5, 'Ford', 'Puma', 20024.9)

"""

print("#### Tutte le macchine - MATRICE 2D ####")
for macchina in macchine:
    result = ""
    for campo in macchina:
        result += str(campo)+"    "+"\t"
    print(result)
print()

"""
Per che le colonne siano tutte alineate si deve trovare la differenza di spazzi tra la parola più lunga 
e la parola più corta della stessa colonna (o riga) e concatenarle quei spazzi mancati ed infine tabulare
la parola da stampare nel loop 1D o 2D, ecc.

---- Tutte le macchine - MATRICE ----
1       Fiat            500x            20100.0
2       Mercedes        Classe A        26500.0
3       Jeep            Wrangler        18000.0
4       Seat            Arona           17758.2
5       Ford            Puma            20024.9

"""

cursor.execute("SELECT Marca FROM veicoli")
marche = cursor.fetchall() # Rende a marche una tabella con 1 campo
print("#### Marche delle macchine - MATRICE 2D CON UNA SOLA COLONNA (5*1) ####")
for marca in marche:
    for dato in marca:
        print("Marca:",dato)
print()
"""
#### Marche delle macchine - MATRICE 2D CON UNA SOLA COLONNA (5*1) ####
Marca: Fiat
Marca: Mercedes
Marca: Jeep
Marca: Seat
Marca: Ford

"""

cursor.execute("SELECT Modello, Prezzo FROM veicoli")
modelli = cursor.fetchall() # Rende modelli una nuova tabella con 2 campi
print("#### Modelli e Prezzi delle macchine - LISTA 1[D] dimensione parametrica ####")
print("#### Su una dimensione mostra 2 dimensioni in base alle colonne ricevute ####")
for modello in modelli:
    print(f"{modello[0]}    \t{modello[1]}")
print()
"""
#### Modelli e Prezzi delle macchine - LISTA 1[D] dimensione parametrica ####
#### Su una dimensione mostra 2 dimensioni in base alle colonne ricevute ####
500x            20100.0
Classe A        26500.0
Wrangler        18000.0
Arona           17758.2
Puma            20024.9

"""

print("#### Macchine con costo minore di 20K ####")
cursor.execute("SELECT * FROM veicoli WHERE Prezzo < 20000")
macchine_prezzi_minore_20k = cursor.fetchall()
for macchina in macchine_prezzi_minore_20k:
    trattini()
    print("|",end=" ")
    for dato in macchina:
        print(str(dato)+"   \t", end="| ")
    print()
trattini()
print()
"""
#### Macchine con costo minore di 20K ####
---------------------------------------------------------
| 3     | Jeep          | Wrangler      | 18000.0       |
---------------------------------------------------------
| 4     | Seat          | Arona         | 17758.2       |
---------------------------------------------------------

"""


print("#### Macchine JEEP con costo minore di 20K ####")
cursor.execute("SELECT * FROM veicoli WHERE Prezzo < 20000 AND Marca = 'Jeep'")
macchine_jeep_prezzi_minore_20k = cursor.fetchall()
for macchina in macchine_jeep_prezzi_minore_20k:
    trattini()
    print("|",end=" ")
    for dato in macchina:
        print(str(dato)+"   \t", end="| ")
    print()
trattini()
print()
"""
#### Macchine JEEP con costo minore di 20K ####
---------------------------------------------------------
| 3     | Jeep          | Wrangler      | 18000.0       |
---------------------------------------------------------

"""

print("#### Prima macchina della tabella ####")
cursor.execute("SELECT * FROM veicoli")
prima_macchina = cursor.fetchone()
trattini()
print("|",end=" ")
for macchina in prima_macchina:
    print(macchina,"   \t", end="| ")
print()
trattini()
print()
"""
#### Prima macchina della tabella ####
---------------------------------------------------------
| 1     | Fiat          | 500x          | 20100.0       |
---------------------------------------------------------

"""

connessione.close()