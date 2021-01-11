"""
Tkinter
Modulo di python per creare interfacce grafiche di utenti
"""

from tkinter import *

# Creare la finestra principale
window = Tk(screenName="First window with tk")

# Titolo della finestra
window.title("Prima app Python GUI")

# Icono della finestra
window.iconbitmap("./21-tkinter/img/logo-tesseract.ico")

# Cambi nelle dimensioni della finestra
window.geometry("750x450")

# Bloccare il ridimensionamento della finestra: fx(x,y) => 0 bloccato, 1 sbloccato
window.resizable(1,0)

# Eseguire e chiamare la finestra fino alla chiusura, importante che questo metodo sia tra gli ultimi.
window.mainloop()