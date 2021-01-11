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

testo = Label(finestra, text="Testo del west")
testo.config(
    heigh=1,
    fg="white",
    bg="red",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="spider" # spider, circle, etc
)
testo.pack(ANCHOR=W)

finestra.mainloop()