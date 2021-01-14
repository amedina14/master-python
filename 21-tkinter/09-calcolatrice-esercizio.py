"""
Calcolatrice
- Due campi testo
- 4 Bottoni per le operazioni
- Mostra risultato in una alerta
"""
from tkinter import *
from tkinter import messagebox

finestra = Tk()
#finestra.geometry("700x450")
finestra.config(bd="25")
finestra.title("Calcolatrice")

numero1 = StringVar()
numero2 = StringVar()
risultato = StringVar()

"""
frame_superiore = Frame(finestra)
frame_superiore.config(
    #font=("Arial",10),
    bg="dodger blue",
    padx=10,
    pady=10,
    bd=5,
)
frame_superiore.pack(anchor=N, fill=X, expand=YES) #grid(row=0, column=0, columnspan=3, anchor=CENTER)
"""

primo_valore = Label(finestra, text="valore 1: ")
primo_valore.pack()#grid(row=0,column=1)
in_valore1 = Entry(finestra, textvariable=numero1)
in_valore1.pack()#grid(row=0,column=2, padx=5, pady=5)

secondo_valore = Label(finestra, text="valore 2: ")
secondo_valore.pack()#grid(row=0,column=3, padx=5, pady=5)
in_valore2 = Entry(finestra, textvariable=numero2)
in_valore2.pack()#grid(row=0,column=4, padx=5, pady=5)

Label(finestra, text="").pack()

# Bottoni
"""
frame_operazioni = Frame(finestra)
frame_operazioni.config(
    bg="#ADFF2F"
)
frame_operazioni.pack() # grid(row=1,column=0)
"""

Button(finestra, text="Somma").pack(side="left")
Button(finestra, text="Resta").pack(side="left")
Button(finestra, text="Moltiplicazione").pack(side="left")
Button(finestra, text="Divisione").pack(side="left")


# Mostra risultato in una alerta

finestra.mainloop()