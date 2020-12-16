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

#Operatori logici
and (e)
or (o)
not (No)
! (negazione)

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

print("\n######### ESEMPIO 4: Weekend #########")
#day = int(input("Insert day: "))
day = 5

"""
if day == 1:
    print("Monday")
else:
    if day == 2:
        print("Tuesday")
    else:
        if day == 3:
            print("Tuesday")
        else:
            if day == 4:
                print("Tuesday")
"""
if day == 1:
    print("Lunedi")
elif day == 2:
    print("Martedi")
elif day == 3:
    print("Mercoledi")
elif day == 4:
    print("Giovedi")
elif day == 5:
    print("Venerdi")
elif day > 5:
    print("Weekend")

print("\n######### ESEMPIO 5: Weekend #########")
eta_minima = 18
eta_massima = 65
eta_ufficiale = 17

if eta_ufficiale >= 18 and eta_ufficiale <= 65:
    print("Può lavorare")
else:
    print(f"Non può lavorare, età ufficiale {eta_ufficiale}")