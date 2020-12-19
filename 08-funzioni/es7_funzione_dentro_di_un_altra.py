# Esempio 7: Funzione dentro di un'altra
print("##### Esempio 7 #####")

def stampa_nome(n):
    nome = f"Il nome è: {n}"
    return nome
def stampa_cognome(c):
    cognome = f"Il cognome è: {c}"
    return cognome
def stampa_tutto(n,c):
    return f"{stampa_nome(n)} \n{stampa_cognome(c)}"

nome = "Adrian"
cognome = "Medina"
print(stampa_tutto(nome, cognome))
