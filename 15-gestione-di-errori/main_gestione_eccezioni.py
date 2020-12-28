"""
Gestione di errori:
Catturare eccezioni e gestire errori nel codice, suscettibili a falle/errori.
"""

try:
    nome = input("Inserisci nome: ")
    if len(nome) > 1:
        messaggio = "Il nome è "+nome
    
    print(messaggio)

except:
    print("Errore: Valore del nome invalido")
else:
    print("Operazione eseguita con successo")
finally:
    print("Fine del blocco 'try'!")