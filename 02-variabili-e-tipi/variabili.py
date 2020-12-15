"""
Una variabile è un contenitore d'informazione
che dentro salva un dato, si possono creare molte
variabili e ciascuna che abbia un dato distinto.
"""

print("------------------------------------")

#Creare variabili e assegnare un valore
variabile = 1
titolo = "Master in Python"
istituzione = "Udemy"
qualificazione = 45
durataOre = 6.7

#Mostrare valori
print(f"titolo {titolo}")
print(f"istituzione {istituzione}")
print(f"qualificazione {qualificazione}")
print(f"durataOre {durataOre}")

print("------------------------------------")

#Sostituire il valore di alcune variabili / riassegnando valori
qualificazione = 77
durataOre = 8.9
print(f"qualificazione {qualificazione}")
print(f"durataOre {durataOre}")

print("------------------------------------")
nome = "Adrian"
cognome = "Medina"
web = "arandom.000webhostapp.com"

print(nome +" "+ cognome +" "+ web)
print(f"{nome} {cognome} - {web}") #f formatta contenuto/testo ed interpola variabili.
print("Ciao, mi chiamo {} {} e la mia web è {}".format(nome,cognome,web))
print(nome, cognome, web)
print("------------------------------------")
