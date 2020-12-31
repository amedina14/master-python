"""
Ereditarieta:
Possibilita di condividere attributi e metodi tra le classi.
E che diversi classi eredino da altri classi.
"""

class Persona:
    """
    nome
    cognome
    altezza
    eta
    """

    def getNome(self):
        return self.nome    
    def setNome(self, nome):
        self.nome = nome
    
    def getCognome(self):
        return self.cognome    
    def setCognome(self, cognome):
        self.cognome = cognome
    
    def getAltezza(self):
        return self.altezza
    def setAltezza(self, altezza):
        self.altezza = altezza
    
    def getEta(self):
        return self.eta
    def setEta(self, eta):
        self.eta = eta

    def parlare(self):
        return "Sto parlando"
    
    def caminare(self):
        return "Sto caminando"
    
    def dormire(self):
        return "Buona notte. Dormendo"

class Informatico(Persona):
    """
    linguaggi
    esperienza
    progetti
    """
    linguaggi = ""

    def __init__(self): # Costruttore che aggiunge automaticamente valori alle proprieta
        self.linguaggi = "Python, Java, C#, JavaScript"
        self.esperienza = 5
    
    def getLinguaggi(self):
        return self.linguaggi
    def setLinguaggi(self, linguaggi):
        self.linguaggi = linguaggi
    
    def imparare(self, linguaggi):
        self.linguaggi += "*"+linguaggi+" "
        return self.linguaggi
    
    def programmare(self):
        return "Sto programmando"
    
    def ripararePc(self):
        return "Ho riparato il tuo pc"

class TecnicoReti(Informatico):

    def __init__(self):
        super().__init__()
        self.auditReti = 'Esperto'
        self.esperienzaReti = 5
        
    def audit(self):
        return "Sto audendo la rete"

    