#Esempio 4 parametri opzionali
print("\n##### Esempio 4 #####")

def getImpiegato(nome, dni = False):
    print("Impiegato")
    print(f"Nome: {nome}")
    if dni != False:
        print(f"DNI: {dni}")

getImpiegato("Adrian Medina","758812544")#"758812544"
