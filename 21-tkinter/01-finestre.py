"""
Tkinter
Modulo di python per creare interfacce grafiche di utenti
"""
import os.path # as pathlib
from tkinter import *

# Creare la finestra principale
window = Tk(screenName="First window with tk")

# Titolo della finestra
window.title("Prima app Python GUI")

# Verificare l'esistena di un file
indirizzo_icono = os.path.abspath("./img/logo-tesseract.ico")

if not os.path.isfile(indirizzo_icono): # Se non trova l'indireizzo dell'immagine
    indirizzo_icono = os.path.abspath("./21-tkinter/img/logo-tesseract.ico")    

# Icono della finestra
window.iconbitmap(indirizzo_icono)

# Mostrare testo in una label
label_testo = Label(window, text=indirizzo_icono)
label_testo.pack()

# Cambi nelle dimensioni della finestra
window.geometry("750x450")

# Bloccare il ridimensionamento della finestra: fx(x,y) => 0 bloccato, 1 sbloccato
window.resizable(1,0)

# Eseguire e chiamare la finestra fino alla chiusura, importante che questo metodo sia tra gli ultimi.
window.mainloop()