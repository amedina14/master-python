"""
Esercizio 3
controlla variabili vuota
riempie
maiuscola
"""

variabile = ""
num = None

if len(variabile.strip()) <= 0:
    variabile = "riempito per default".upper()
    #variabile = variabile.upper()
else:
    print("\"Variabile\" ha contenuto")
print(variabile)

#print(num)
if num == None:
    print(f"\"num\" vuota: {num}")