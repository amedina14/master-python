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
finestra.geometry("600x500")
finestra.title("Progetto tkinter python")
finestra.resizable(0,0)

# Defining more pages
def home():
    lbl_home.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=20,
        pady=20
    )
    lbl_home.grid(row=0,column=0)

    lbl_product.grid_remove()
    lbl_info.grid_remove()
    data_info.grid_remove()

    return True

def addProduct():
    lbl_product.config(
        fg="white",
        bg="green",
        font=("Consolas", 30),
        padx=20,
        pady=20,
    )
    lbl_product.grid(row=0,column=0)

    lbl_home.grid_remove()
    lbl_info.grid_remove()
    data_info.grid_remove()

    return True

def Information():
    lbl_info.config(
        fg="white",
        bg="blue",
        font=("Times new romans", 30),
        padx=20,
        pady=20,
    )
    lbl_info.grid(row=0,column=0)

    data_info.config(
        fg="white",
        bg="grey",
        font=("Arial", 10),
        padx=20,
        pady=20
    )
    data_info.grid(row=1,column=0)

    lbl_home.grid_remove()
    lbl_product.grid_remove()

    return True


# Defining fields (Home)
lbl_home = Label(finestra, text="Home")

# Defining fields (addProduct)
lbl_product = Label(finestra, text="Product")

# Defining fields (Information)
lbl_info = Label(finestra, text="Information")
data_info = Label(finestra, text="Created by Adrian Medina, 2021")

# Creates toolbar
toolbar = Menu(finestra)

# Defining toolbar
toolbar.add_command(label="Inizio",command=home)
toolbar.add_command(label="Aggiungere",command=addProduct)
toolbar.add_command(label="Informazione",command=Information)
toolbar.add_command(label="Uscire", command=finestra.quit)

# Loads toolbar: Config window to display toolbar
finestra.config(menu=toolbar)

# Load window
finestra.mainloop()