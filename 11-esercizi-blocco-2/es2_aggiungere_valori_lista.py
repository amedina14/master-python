import random

"""
Esercizion 2
Scrivere un programma che aggiunga valori alla lista, 
mentre i suoi elementi siano minori a 120 e dopo 
stampare la lista. 
Realizarlo con while e for.
"""

print("\n###### For ######")
lista_for = []

def aggiungere_elemento(lis):
    for i in range(0,120):
        lista_for.append(f"elemento-{i}")
        print(f"mostrando {i}: {lis[i]}")
        #numRand = random.randint(0,100)
        #lista_for.append(numRand)

"""
def stampa_lista_for(paramList):
    for elemento in paramList:
        print(f"Indice {lista_for.index(elemento)}: {elemento}", end="\n")
        #print(f"Mostrando: {lista_for[elemento]}")
"""

aggiungere_elemento(lista_for)
#stampa_lista_for(lista_for)
print("Lunghezza lista_for",len(lista_for))

####### While #######
print("\n###### While ######")
lista_while = []
j=0
while j < 120:
    lista_while.append(f"elemento-{j}")
    print(f"{j+1}. {lista_while[j]}")
    #print("index "+str(j)+": " + lista_while[j])
    j+=1
