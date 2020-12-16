"""
# Condizione if

if true:
    instruc.
else false:
    instruc.

#operatori di comparazione
==
!=
<
>
<=
>=

"""

# Esempio 1
print("######### ESEMPIO 1 #########")
color = "rosso"
if color == "rosso":
    print("Trovato")
    print(f"colore {color}")
else:
    print("Not red")

# Esempio 2
print("\n######### ESEMPIO 2 #########")
year = 2020
#year = int(input("In che anno siamo? "))
if year >= 2021:
    print("Anno maggiore uguale al 2021 in avanti")
else:
    print("Siamo nel periodo che va fino all'anno 2020")

# Esempio 3
print("\n######### ESEMPIO 3: Maggiore di eta #########")

nome = "Adrian Medina"
citta = "Guayaquil"
continente = "Europa"
eta = 24
maggiorenne = 18
if eta >= maggiorenne:
    print(f"Utente {nome} è maggiorenne")

    if continente != "Europa":
        print(f"Utente non europeo, è di {continente}")
    else:
        print(f"Utente europeo, è di {citta}")
else:    
    print(f"Utente {nome} è minorenne")