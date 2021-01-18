"""
Creare un programma che abbia:
 (fatto) - Finestra
 (fatto) - Grandezza fissa
 (fatto) - No ridimensionabile
 (fatto) - Un menu: Inizio, Aggiungere, Informazione, Uscire.
 (fatto) - Opzione di uscire
 (fatto) - Diverse schermate
 (fatto) - Form di aggiungere prodotti
 (fatto) - Salvare i dati temporalmente
- Stampa elenco dati nella schermata home

"""

from tkinter import *

# Defining window
finestra = Tk()
finestra.geometry("500x500")
finestra.title("Progetto tkinter python")
finestra.resizable(0,0)

# Defining more pages
def home():
    lbl_home.config(
        fg="white",
        bg="black",
        font=("Arial",30),
        padx=195,
        pady=20
    )
    lbl_home.grid(row=0,column=0)

    lbl_product.grid_remove()
    lbl_info.grid_remove()
    data_info.grid_remove()
    add_product_frame.grid_remove()

    return True

def addProduct():
    lbl_product.config(
        fg="white",
        bg="#2F4F4F",
        font=("Consolas", 30),
        padx=171,
        pady=20,
    )
    lbl_product.grid(row=0,column=0,columnspan=10) # Columnspan: Stabilisce di quante colonne è composta la griglia
    
    # Campi del form
    add_product_frame.grid(row=1) # Mostra frame
    lbl_add_name_product.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    entry_name_product.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    lbl_add_price_product.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    entry_price_product.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    lbl_add_description_product.grid(row=3,column=0,padx=5,pady=5,sticky=N)
    entry_description_product.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    entry_description_product.config(
        width=30,
        height=5,
        font=("consolas",12),
        padx=15,
        pady=15
    )

    # Linea di spazio separatrice
    add_separator.grid(row=4)

    bottone.config(padx=15,pady=5,bg="green",fg="white")
    bottone.grid(row=5,column=1,sticky=E)

    # Nascondere le altre pagine
    lbl_home.grid_remove()
    lbl_info.grid_remove()
    data_info.grid_remove()

    return True

def Information():
    lbl_info.config(
        fg="white",
        bg="blue",
        font=("Times new romans", 30),
        padx=150,
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
    add_product_frame.grid_remove()

    return True

def saveProduct():
    prodotti.append([
        nomeProdotto.get(),
        prezzoProdotto.get(),
        # Parametri speciali obbligatori per ottenere i dati dal Textarea .get("1.0","end-1c")
        entry_description_product.get("1.0","end-1c") 
    ])
    nomeProdotto.set("")
    prezzoProdotto.set("")
    entry_description_product.delete("1.0",END)

    print(prodotti)
    home()

# Variabili importanti
prodotti = []
nomeProdotto = StringVar()
prezzoProdotto = IntVar()
#descrizione = StringVar()

# Defining fields (Home)
lbl_home = Label(finestra, text="Home")

# Defining fields (addProduct)
lbl_product = Label(finestra, text="Product")

# Campi del form product
add_product_frame = Frame(finestra)

lbl_add_name_product = Label(add_product_frame, text="Name: ")
entry_name_product = Entry(add_product_frame, textvariable=nomeProdotto)

lbl_add_price_product = Label(add_product_frame, text="Prezzo: ")
entry_price_product = Entry(add_product_frame, textvariable=prezzoProdotto)

lbl_add_description_product = Label(add_product_frame, text="Descrizione: ")
entry_description_product = Text(add_product_frame)

add_separator = Label(add_product_frame)
bottone = Button(add_product_frame, text="Invio", command=saveProduct)

# Defining fields (Information)
lbl_info = Label(finestra, text="Information")
data_info = Label(finestra, text="Created by Adrian Medina, 2021")

# Creates toolbar
toolbar = Menu(finestra)

home()

# Defining toolbar
toolbar.add_command(label="Inizio",command=home)
toolbar.add_command(label="Aggiungere",command=addProduct)
toolbar.add_command(label="Informazione",command=Information)
toolbar.add_command(label="Uscire", command=finestra.quit)

# Loads toolbar: Config window to display toolbar
finestra.config(menu=toolbar)

# Load window
finestra.mainloop()