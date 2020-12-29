class Veicolo:

    # Attributi o Proprietà (Variabili)
    colore = "Rosso"
    marca = "Ferrari"
    modelo = "599 GTO"
    velocita = 350
    cv = 550
    posti = 2

    # Costruttore
    def __init__(self, colore, marca, modelo, velocita, cv, posti):
        self.colore = colore
        self.marca = marca
        self.modelo = modelo
        self.velocita = velocita
        self.cv = cv
        self.posti = posti

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

    def getInfo(self):
        #result = "---------Informazione veicolo---------"
        result = f"Marca: {self.getMarca()}"
        result += f"\nModelo: {self.getModelo()}"
        result += f"\nColore: {self.getColore()}"
        result += f"\nVelocita: {self.getVelocita()}"
        return result