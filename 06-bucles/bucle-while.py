print("------------------------")
i=1
stampa = str(0)

while i<=5:
    print(i)
    i+=1

print("------------------------")
i=1
stampa = str(0)

while i<=5:
    stampa = stampa+", "+str(i)
    #print(i)
    i+=1
print(stampa)

print("------------------------")
i=1
colonna = str(0)

while i<=5:
    colonna = colonna+", "+str(i)
    print(colonna)
    i+=1

print("------------------------ Tabella di moltiplicazione while")
numero_utente = int(input("Di che numero vuoi vedere la tabellina?: "))
i=1


while i<11:

    if numero_utente < 1:
        print("Valore invalido")
        break
    """
    elif type(numero_utente) != int:
        break
    """
    
    #ris = numero_utente*i
    print(f"{numero_utente}x{i}: {numero_utente*i}")
    i+=1

