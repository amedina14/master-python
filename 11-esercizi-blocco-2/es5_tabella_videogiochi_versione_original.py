"""
Esercizio 5 (Versione Victor)
Creare una lista con il seguente contenuto di questa tabella:
AZIONE              AVVENTURA           SPORT
Fallen Order        Skyrim              Fifa 21
Monster Hunter      Minecraft           Rocket League
Battlefront         Bloodborne          Gran Turismo

Stampare questa informazione ordinata
"""

lista_videogiochi = [
    {
        "categoria": "azione",
        "nome": ["GTA", "COD", "Bloodborne"],
    },
    {
        "categoria": "avventura",
        "nome": ["Uncharted", "No Man's Sky", "RDR2"],
    },
    {
        "categoria": "sport",
        "nome": ["PES 21", "Need for Speed", "NBA"],
    }
]

header = ""
for giochi in lista_videogiochi:
    header = f"| {giochi['categoria']} |".upper()
    print(f"---------{header}---------")
    for gioco in giochi['nome']:
        print(gioco)
    
print()