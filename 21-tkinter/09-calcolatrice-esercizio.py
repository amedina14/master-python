"""
Calcolatrice
- Due campi testo
- 4 Bottoni per le operazioni
- Mostra risultato in una alerta
"""
from tkinter import *
from tkinter import messagebox

finestra = Tk()
finestra.geometry("700x450")
finestra.config(bd="25")
finestra.title("Calcolatrice")

numero1 = StringVar()
numero2 = StringVar()
risultato = StringVar()

frame_superiore = Frame(finestra)
frame_superiore.config(
    #font=("Arial",10),
    #bg="dodger blue",
    width=250,
    height=250,
    relief=SOLID,
    padx=10,
    pady=10,
    bd=5,
)
frame_superiore.pack(anchor=N) #grid(row=0, column=0, columnspan=3, anchor=CENTER)
frame_superiore.pack_propagate(False)
"""
"""

primo_valore = Label(frame_superiore, text="valore 1: ")
primo_valore.pack()#grid(row=0,column=1)
in_valore1 = Entry(frame_superiore, textvariable=numero1, justify="center")
in_valore1.pack()#grid(row=0,column=2, padx=5, pady=5)

secondo_valore = Label(frame_superiore, text="valore 2: ")
secondo_valore.pack()#grid(row=0,column=3, padx=5, pady=5)
in_valore2 = Entry(frame_superiore, textvariable=numero2, justify="center")
in_valore2.pack()#grid(row=0,column=4, padx=5, pady=5)

Label(frame_superiore, text="").pack()

# Bottoni
"""
frame_operazioni = Frame(finestra)
frame_operazioni.config(
    bg="#ADFF2F"
)
frame_operazioni.pack() # grid(row=1,column=0)
"""

Button(frame_superiore, text="Somma").pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Resta").pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Moltiplicazione").pack(side="left", fill=X, expand=YES)
Button(frame_superiore, text="Divisione").pack(side="left", fill=X, expand=YES)


# Mostra risultato in una alerta

finestra.mainloop()