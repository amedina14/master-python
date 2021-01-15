from tkinter import *

class Numeri:

    """    
        __numero1 = StringVar()
        __numero2 = StringVar()
        risultato = StringVar()
    """

    def __init__(self, alerte):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.risultato = StringVar() 
        self.alerte = alerte

    def converteFloat(self,numero):
        try:
            result = float(numero)
        except:
            result = 0
            self.alerte.showerror("Error","Inseriscei i dat  i correttamente")
        return result
    def somma(self):
        #ris_somma = self.converteFloat(self.numero1.get()) + self.converteFloat(self.numero2.get())
        self.risultato.set(self.converteFloat(self.numero1.get()) + self.converteFloat(self.numero2.get()))
        #self.mostraRisultato(ris_somma)
        self.mostraRisultato()
        #return ris_somma

    def resta(self):
        #ris_resta = self.converteFloat(self.numero1.get()) - self.converteFloat(self.numero2.get())
        self.risultato.set(self.converteFloat(self.numero1.get()) - self.converteFloat(self.numero2.get()))
        #self.mostraRisultato(ris_resta)
        self.mostraRisultato()
        #return result

    def molt(self):
        #ris_molt = self.converteFloat(self.numero1.get()) * self.converteFloat(self.numero2.get())
        self.risultato.set(self.converteFloat(self.numero1.get()) * self.converteFloat(self.numero2.get()))
        #self.mostraRisultato(ris_molt)
        self.mostraRisultato()
        #return result

    def div(self):
        #ris_div = self.converteFloat(self.numero1.get()) / self.converteFloat(self.numero2.get())
        self.risultato.set(self.converteFloat(self.numero1.get()) / self.converteFloat(self.numero2.get()))
        #self.mostraRisultato(ris_div)
        self.mostraRisultato()
        #return result

    def mostraRisultato(self):
        self.alerte.showinfo("Risultato", f"Risultato: {self.risultato.get()}")
        # Svuota i textbox
        self.numero1.set("")
        self.numero2.set("")

    def setNumero1(self, valore1):
        self.numero1 = valore1
    
    def getNumero1(self):
        return self.numero1

    def setNumero2(self, valore2):
        self.numero2 = valore2
    
    def getNumero2(self):
        return self.numero2
