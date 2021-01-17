"""
Creare un programma che abbia:
 (fatto) - Finestra
 (fatto) - Grandezza fissa
 (fatto) - No ridimensionabile
 (fatto) - Un menu: Inizio, Aggiungere, Informazione, Uscire.
 (fatto) - Opzione di uscire
- Diverse schermate
- Form di aggiungere prodotti
- Salvare i dati temporalmente
- Stampa elenco dati nella schermata home

"""

from tkinter import *

# Defining window
finestra = Tk()
finestra.geometry("500x500")
finestra.title("Progetto tkinter python")
finestra.resizable(0,0)

# Creates toolbar
toolbar = Menu(finestra)

# Loads toolbar: Config window to display toolbar
finestra.config(menu=toolbar)

# Defining toolbar
toolbar.add_command(label="Inizio")
toolbar.add_command(label="Aggiunger")
toolbar.add_command(label="Informazione")
toolbar.add_command(label="Uscire", command=finestra.quit)


# Load window
finestra.mainloop()