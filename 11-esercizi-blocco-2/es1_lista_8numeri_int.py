"""
Lista di 8 numeri interi
-scorrere e stamparla
-ordinarla e stamparla
-mostrare lunghezza
-Cercare elemento richiesto da tastiera
"""

numeri = [11,2,6,7,4,3,17,14]

#1
for numero in numeri:
    print(numero)

#2
numeri.sort()
print(f"\nLista ordinata: {numeri}")

#3
print(f"\nLunghezza della lista: {len(numeri)}")

#4
cerca = int(input("\nInserisci il numero da cercare: "))
position = numeri.index(cerca)
print("Il numero \""+ str(cerca) +"\" si trova nel indice: "+str(position))