"""
Definire una classe modello veicolo per più oggetti con caratteristiche simili
"""

class Veicolo:

    # Attributi o Proprietà (Variabili)
    colore = "Rosso"
    marca = "Ferrari"
    modelo = "599 GTO"
    velocita = 350
    cv = 550
    posti = 2

    # Costruttore


    # Metodi (Azioni dell'oggetto)
    def setColore(self, colore):
        self.colore = colore

    def getColore(self):
        return self.colore
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def accelerare(self):
        self.velocita += 1

    def frenare(self):
        self.velocita -= 1

    def getVelocita(self):
        return self.velocita        

    def setVelocita(self, velocita):
        self.velocita = velocita

#Fine classe

# Creare oggetto / istanziare
ferrari = Veicolo() 

sceltaColore = input("Inserisci colore a tua scelta: ")
ferrari.setColore(sceltaColore)
sceltaModelo = input("Inserisci un modelo a tua scelta: ")
ferrari.setModelo(sceltaModelo)

print("\n## Ferrari 1 ##")
print("Marca: "+ferrari.getMarca(), "\nColore: "+ferrari.getColore(), "\nModelo: "+ferrari.getModelo())
print("Km/h:",ferrari.getVelocita())
print("Oggetto del tipo:", type(ferrari).__name__)

print("\n## In moto ##")
for accelerando in range(0,20):
    ferrari.accelerare()
print("Accelerata Km/h:",ferrari.getVelocita())

for frenando in range(0,15):
    ferrari.frenare()
print("Frenata Km/h:",ferrari.getVelocita())

#Creare multipli oggetti
ferrari_default_599 = Veicolo()

print("\n## Ferrari 2 ##\nMarca: "+ferrari_default_599.getMarca(), "\nModelo: "+ferrari_default_599.getModelo(), "\nColore: "+ferrari_default_599.getColore(), "\nVelocita: "+str(ferrari_default_599.getVelocita()))
print("Oggetto del tipo:", type(ferrari_default_599).__name__)