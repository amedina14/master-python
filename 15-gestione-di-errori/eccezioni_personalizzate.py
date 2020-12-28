"""
Custom errors
"""

try:
    nome = input("Inserisci nome: ")
    eta = int(input("Inserisci eta: "))
    if len(nome) <=1:
        raise ValueError("Nome incompleto")
    elif eta < 5 and eta > 110:
        raise ValueError("Età non ammessa")
    else:
        print(f"Benvenuto al master in python {nome}")
except ValueError:
    print("Inserisci i dati correttamente")
except Exception as e:
    print("Errore: ", e)