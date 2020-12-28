"""
Lista di 8 numeri interi
-scorrere e stamparla
-funzione che scorra la lista e restituisca un string
-ordinarla e stamparla
-mostrare lunghezza
-Cercare elemento richiesto da tastiera
"""

numeri = [11,2,6,7,4,3,17,14]

#1 scorrere e stamparla
for numero in numeri:
    print(numero)

#2 funzione che scorra la lista e restituisca un string
def scorri(lista):
    risultato = ""
    for i in lista: # 'i' prende il valore dell'elemento
        risultato += str(i)
        if lista.index(i)+1 < len(lista): # da 1 a < 8: stampa la ", " alla stringa
            risultato += ", "                        
    return risultato
print("\n"+scorri(numeri))

#3 ordinarla e stamparla
numeri.sort()
print(f"\nLista ordinata: {scorri(numeri)}")

#4 mostrare lunghezza
print(f"\nLunghezza della lista: {len(numeri)}")

#5 Cercare elemento richiesto da tastiera
try:
    cerca = int(input("\nInserisci il numero da cercare: "))
    controlla = isinstance(cerca, int)
    while not controlla or cerca <= 0: 
        cerca = int(input("\nInserisci il numero da cercare: "))
    else:
        print(f"Inserito {cerca}")
    position = numeri.index(cerca)
    print("Il numero \""+ str(cerca) +"\" si trova nel indice: "+str(position))
except:
    print("Il valore non è presente")

