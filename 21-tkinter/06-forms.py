from tkinter import *

"""
Se si usa Grid non si può usare pack sullo stesso elemento/i anche acendo relazione.
"""

finestra = Tk()
finestra.geometry("700x400")
finestra.title("Forms con Tkinter")

# Header
header = Label(finestra, text="Moduli con tkinter: Header")
header.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans",20),
    padx=10,
    pady=10
)
header.grid(row=0, column=0, columnspan=12, sticky=W) # pack(side=LEFT, anchor=NW) # fill=Y, expand=YES

# Label nome
lbl_nome = Label(finestra, text="Nome")
lbl_nome.grid(row=1, column=0, padx=5, pady=5)

# Textbox nome
text_in_nome = Entry(finestra)
text_in_nome.grid(row=1, column=1, sticky=W, padx=5, pady=5)
text_in_nome.config(justify="right", state="normal")

# Label cognome
lbl_cogn = Label(finestra, text="Cognome")
lbl_cogn.grid(row=2, column=0, padx=5, pady=5)

# Textbox cognome
text_in_cognome = Entry(finestra)
text_in_cognome.grid(row=2, column=1, sticky=W, padx=5, pady=5)
text_in_cognome.config(justify="center", state="normal")

# Label DEPOSITO
lbl_dep = Label(finestra, text="Deposito $$")
lbl_dep.grid(row=3, column=0, padx=5, pady=5)

# Textbox DEPOSITO
text_in_deposito = Entry(finestra)
text_in_deposito.grid(row=3, column=1, sticky=W, padx=5, pady=5)
text_in_deposito.config(justify="left", state="disabled")


# Label descrizione
lbl_desc = Label(finestra, text="Descrizione")
lbl_desc.grid(row=4, column=0, sticky=N, padx=5, pady=5)

# Textbox descrizione (TEXTAREA o campo di testo grande)
descrizione = Text(finestra)
descrizione.grid(row=4, column=1, sticky=W, padx=5, pady=5)
descrizione.config(
    width=30,
    height=5,
    font=("Aria",12),
    padx=15,
    pady=15
)

# Bottoni 
Label(finestra).grid(row=5, column=1) # riga di spazio 
bottone1 = Button(finestra, text="Submit")
bottone1.grid(row=6, column=1, sticky=W)
bottone1.config(
    padx=15,
    pady=5,
    fg="orange",
    bg="navy"
)


finestra.mainloop()