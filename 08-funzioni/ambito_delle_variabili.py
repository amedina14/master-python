"""
Variabili locali: Si definiscono dentro di una funzione e non si possono
richiamare al di fuori di essa. Sono disponibili solo dentro a meno che
si restituiscano come risultato con un return.

Variabili globali: Sono definite fuori da una funzione e sono
disponibili su tutto il programma.
"""

# Variabili globali
frase = "Né i geni sono così geni, né i medriocri sono così mediocri."

print("fuori: "+frase)

def stampa():
    frase = "Hello world!!"
    print("\ndentro: "+str(frase))

    year = 2021
    print(year)

    global web
    web = "arandom.000webhostapp.com"
    print("Dentro: "+web)

    return "ritorna: "+str(year)

print(stampa())
print("\nVariabile convertita a globale:", web)