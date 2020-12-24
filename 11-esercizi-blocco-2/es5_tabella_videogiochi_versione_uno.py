"""
Esercizio 5 (Versione Adrian)
Creare una lista con il seguente contenuto di questa tabella:
AZIONE              AVVENTURA           SPORT
Fallen Order        Skyrim              Fifa 21
Monster Hunter      Minecraft           Rocket League
Battlefront         Bloodborne          Gran Turismo

Stampare questa informazione ordinata
"""

videogiochi = [
    {
        "nome": "Fallen Order",
        "categoria": "azione"
    },
    {
        "nome": "Monster Hunter",
        "categoria": "azione"
    },
    {
        "nome": "Battlefront",
        "categoria": "azione"
    },
    {
        "nome": "Skyrim",
        "categoria": "avventura"
    },
    {
        "nome": "Minecraft",
        "categoria": "avventura"
    },
    {
        "nome": "Tomb Raider",
        "categoria": "avventura"
    },
    {
        "nome": "Fifa 21",
        "categoria": "sport"
    },
    {
        "nome": "Rocket League",
        "categoria": "sport"
    },
    {
        "nome": "Gran Turismo",
        "categoria": "sport"
    }
]

print(f"\n##### Gruppi di giochi #####")
for gioco in videogiochi:
    print(f"Gioco: {gioco}")
    for dato in gioco:
        print(f"{dato} : {gioco[dato]}") #Chiave valore
    print()
"""
"""

print(f"\n##### Gruppi di nomi #####")
lista_azione = []
lista_avventura = []
lista_sport = []
for gioco in videogiochi:

    if gioco["categoria"] == "azione":
        lista_azione.append(gioco["nome"])
        #print(gioco["nome"])
    elif gioco["categoria"] == "sport":
        lista_sport.append(gioco["nome"])
        #print(gioco["nome"])
    elif gioco["categoria"] == "avventura":
        lista_avventura.append(gioco["nome"])
        #print(gioco["nome"])

def stampa_liste(p_lista):
    result = ""
    for i in p_lista:
        result += f"{i}\n"
    return result

print("## Giochi d'azione ##")
print(stampa_liste(lista_azione))

print("## Giochi d'sport ##")
print(stampa_liste(lista_sport))

print("## Giochi d'avventura ##")
print(stampa_liste(lista_avventura))

