"""
Esercizio 3
controlla variabili vuota
riempie
maiuscola
"""

variabile = ""

if len(variabile.strip()) <= 0:
    variabile = "riempito per default".upper()
    #variabile = variabile.upper()
else:
    print("\"Variabile\" ha contenuto")
print(variabile)