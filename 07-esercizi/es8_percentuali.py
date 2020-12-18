"""
Esercizio 8
Inserire un numero da tastiera ed estrarre l'N percento dove N anch'esso è da tastiera.
"""

numero = -1
percentuale = 0
fattibile = False

while numero<0:
    try:
        numero = int(input("Inserire un numero: "))
        """if numero < 0:
            print("Il numero non puo essere negativo")"""
    except:
        print("Errore: Il valore inserito non è valido")

while fattibile == False:
    try:
        percentuale = int(input("Inserire una percentuale da applicare: "))
        fattibile = True
    except:
        fattibile = False
        print("Errore: La percentuale inserita non è valida")


print(f"{numero} unita, percentuale {percentuale}% = {numero*(percentuale/100)} unita")