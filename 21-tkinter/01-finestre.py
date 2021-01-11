"""
Tkinter
Modulo di python per creare interfacce grafiche di utenti
"""
import os.path # as pathlib
from tkinter import *

class Programma:

    def __init__(self):
        self.titolo = "Prima app Python GUI"
        self.percorso = "./img/logo-tesseract.ico"
        self.percorso_alt = "./21-tkinter/img/logo-tesseract.ico"
        self.dimensione = "750x450"
        self.resizable = False

    def carica(self):
        # Creare la finestra principale
        window = Tk(screenName="First window with tk")
        self.window = window

        # Titolo della finestra
        window.title(self.titolo)

        # Verificare l'esistena di un file
        indirizzo_icono = os.path.abspath(self.percorso)

        if not os.path.isfile(indirizzo_icono): # Se non trova l'indireizzo dell'immagine
            indirizzo_icono = os.path.abspath(self.percorso_alt)

        # Icono della finestra
        window.iconbitmap(indirizzo_icono)

        # Mostrare testo in una label
        label_testo = Label(window, text=indirizzo_icono)
        label_testo.pack()

        # Cambi nelle dimensioni della finestra
        window.geometry(self.dimensione)

        # Bloccare il ridimensionamento della finestra: fx(x,y) => 0 bloccato, 1 sbloccato
        if self.resizable:
            window.resizable(1,0)
        else:
            window.resizable(0,0)

    def add_text(self, dato):
        testo = Label(self.window, text=dato)
        testo.pack()

    def stampa(self):
        # Eseguire e chiamare la finestra fino alla chiusura, importante che questo metodo sia tra gli ultimi.
        self.window.mainloop()

# Instanziare programa
programma = Programma()
programma.carica()
programma.add_text("Hello World 2021!")
programma.add_text("I want to travel to warm places")
programma.add_text("""Atene, 
Mykonos, 
Fira, 
Salonicco, 
Santorini, 
La Canea, 
Rodi, 
Corfù, 
Heraklio""")
programma.stampa()