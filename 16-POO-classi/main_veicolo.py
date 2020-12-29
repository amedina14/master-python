"""
Definire una classe modello veicolo per più oggetti con caratteristiche simili
"""

class Veicolo:

    # Attributi o Proprietà (Variabili)
    colore = "Rosso"
    marca = "Ferrari"
    modelo = "599 GTO"
    velocidad = 350
    cv = 550
    posti = 2

    # Costruttore


    # Metodi (Azioni dell'oggetto)
    def accelerare(self):
        self.velocidad += 1

    def frenare(self):
        self.velocidad -= 1

    def getVelocita(self):
        return self.velocidad        

#Fine classe

# Creare oggetto / istanziare
ferrari_599_rossa = Veicolo() 

print(ferrari_599_rossa.marca, ferrari_599_rossa.colore)
print("Km/h:",ferrari_599_rossa.velocidad)

for accelerando in range(0,20):
    ferrari_599_rossa.accelerare()
print("Accelerata Km/h:",ferrari_599_rossa.velocidad)

for frenando in range(0,15):
    ferrari_599_rossa.frenare()
print("Frenata Km/h:",ferrari_599_rossa.velocidad)