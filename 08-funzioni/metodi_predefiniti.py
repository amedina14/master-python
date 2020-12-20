nome = "Adrian Medina"

#print(type())
print("\n### type() ###")
print(type(nome))

#isinstance(): detetta il il tippato
print("\n### isinstace() ###")
controlla = isinstance(nome, str)
if controlla:
    print("La variabile è di tipo string")
else:
    print("Non è di tipo string")

if not isinstance(nome, float):
    print("Si, il nome non è di tipo float")
else:
    print("Stranamente il nome è di tipo float")

#strip
print("\n### strip() ###")
testo_per_strip = "    Jingle Bells    "
print(testo_per_strip)
print(testo_per_strip.strip())

#del
print("\n### del() o del x ###")
cancellare = 2020
print("Ancora presente: "+str(cancellare))
del cancellare
#print(cancellare)

#len
print("\n### len() ###")
lunghezza = "Merry Christmas!"
if len(lunghezza) <= 0:
    print("Vuoto")
else:
    print("La lunghezza della variabile è:", len(lunghezza))

#find
print("\n### find() ###")
stella = "stella"
find_position_string = "La stella di natale guida all'incontro con il bambino"
print(find_position_string, f"\nRicerca: \"{stella}\"")
print("La posizione della stella cercata è:",find_position_string.find(stella))

#replace
print("\n### replace() ###")
replacing = "Il Natale è bello"
print(replacing)
print(replacing.replace("Natale", "monopattino"))

#lower() y upper()
print("\n### lower e upper ###")
frase = "Frosty the Snowman"
print("Original:",frase)
frase_maiusc = frase.upper()
print("Upper:\t ",frase_maiusc)
frase_minusc = frase.lower()
print("Lower:\t ",frase_minusc)
