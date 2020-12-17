"""
#For
for variable in elemento_iterable
    instruzioni
"""

c = 0
somma = 0
for i in range(0,10):
    #i+=1
    print("iterazione: "+str(i)+"\tsomma ("+str(somma)+") + i:"+str(somma+i))
    #somma=c+i
    somma+=i
print("somma totale",somma)

# Esempio tabella moltiplicazone
print("\n############# Esempio: tabella moltiplicazone #############")

numero_utente = int(input("Di quale tabella vuoi il numero? "))

if numero_utente < 1:
    print("numero minore di 1")
    numero_utente = 1


print(f"### tabella del {numero_utente} ###")
for i in range(1,10):

    if numero_utente == 10:
        print("numero non permesso")
        break

    print(f"{numero_utente}x{i}: "+str(numero_utente*i))
else:
    print("Tabella finita")
