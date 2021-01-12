from tkinter import *

finestra = Tk()
finestra.geometry("700x500")

testo = Label(finestra, text="Primo testo Header")
testo.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
testo.pack()

testo = Label(finestra, text="Testo all'est")
testo.config(
    heigh=1,
    fg="white",
    bg="orange",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="circle" # spider, arrow, etc
)
testo.pack(anchor=E)

def params(name, surname, country):
    return f" Hello {name} {surname} born in {country}"

"""
"""
nome = "Adrian"
cognome = "Medina"
nazione = "Ecuador"
testo = Label(finestra, text=params(surname=cognome, country=nazione, name=nome)) # Keywords arguments parameters allows any order
testo.config(
    heigh=1,
    fg="white",
    bg="green",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="spider" # spider, circle, etc
)
testo.pack(anchor=W)

finestra.mainloop()