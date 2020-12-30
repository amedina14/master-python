class Veicolo:

    # Attributi o Proprietà (Variabili)
    __colore = "Rosso"
    __marca = "Ferrari"
    __modelo = "599 GTO"
    __velocita = 350
    cv = 550
    posti = 2

    # Costruttore
    def __init__(self, colore, marca, modelo, velocita, cv, posti):
        self.__colore = colore
        self.__marca = marca
        self.__modelo = modelo
        self.__velocita = velocita
        self.cv = cv
        self.posti = posti

    # Metodi (Azioni dell'oggetto)
    def setColore(self, colore):
        self.__colore = colore

    def getColore(self):
        return self.__colore
    
    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def accelerare(self):
        self.__velocita += 1

    def frenare(self):
        self.__velocita -= 1

    def getVelocita(self):
        return self.__velocita        

    def setVelocita(self, velocita):
        self.__velocita = velocita

    def getInfo(self):
        #result = "---------Informazione veicolo---------"
        result = f"Marca: {self.getMarca()}"
        result += f"\nModelo: {self.getModelo()}"
        result += f"\nColore: {self.getColore()}"
        result += f"\nVelocita: {self.getVelocita()}"
        return result