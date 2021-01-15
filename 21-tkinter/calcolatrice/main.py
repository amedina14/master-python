"""
Calcolatrice
- Due campi testo
- 4 Bottoni per le operazioni
- Mostra risultato in una alerta
"""
from tkinter import *
from tkinter import messagebox
import numeri

finestra = Tk()
finestra.geometry("700x450")
finestra.config(bd="25")
finestra.title("Calcolatrice")

frame_superiore = Frame(finestra)
frame_superiore.config(
    width=350,
    height=250,
    relief=SOLID,
    padx=10,
    pady=10,
    bd=5,
)
frame_superiore.pack(anchor=N) #grid(row=0, column=0, columnspan=3, anchor=CENTER)
frame_superiore.pack_propagate(False)

operazione = numeri.Numeri(messagebox)

primo_valore = Label(frame_superiore, text="valore 1: ")
primo_valore.pack()#grid(row=0,column=1)
in_valore1 = Entry(frame_superiore, textvariable=operazione.numero1, justify="center")
in_valore1.pack()#grid(row=0,column=2, padx=5, pady=5)


secondo_valore = Label(frame_superiore, text="valore 2: ")
secondo_valore.pack()#grid(row=0,column=3, padx=5, pady=5)
in_valore2 = Entry(frame_superiore, textvariable=operazione.numero2, justify="center")
in_valore2.pack()#grid(row=0,column=4, padx=5, pady=5)

Label(frame_superiore, text="").pack()

# Bottoni

Button(frame_superiore, text="Somma", command=lambda: operazione.somma()).pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Resta", command=lambda: operazione.resta()).pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Moltiplicazione", command=lambda: operazione.molt()).pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Divisione", command=lambda: operazione.div()).pack(side="left", fill=X, expand=YES)


finestra.mainloop()
