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
color = "rojo"
if color == "rojo":
    print("Trovato")
    print(f"color {color}")
else:
    print("Not red")

# Esempio 2
print("\n######### ESEMPIO 2 #########")
year = 2020
year = int(input("In che anno siamo? 5"))
if year >= 2021:
    print("Anno maggiore uguale al 2021 in avanti")
else:
    print("Siamo nel periodo che va fino all'anno 2020")