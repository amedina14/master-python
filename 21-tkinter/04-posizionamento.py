from tkinter import *

finestra = Tk()
# finestra.geometry("700x500")

testo = Label(finestra, text="Posizionamento")
testo.config(
    fg="white",
    bg="black",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)
testo.pack()

testo = Label(finestra, text="Testo secondario")
testo.config(
    heigh=1,
    fg="white",
    bg="orange",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="circle" # spider, arrow, etc
)
testo.pack(side=TOP, fill=X, expand=YES)


testo = Label(finestra, text="Basico 1") # Keywords arguments parameters allows any order
testo.config(
    heigh=1,
    fg="white",
    bg="green",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="spider" # spider, circle, etc
)
testo.pack(side=LEFT, fill=X, expand=YES)

testo = Label(finestra, text="Basico 2")
testo.config(
    heigh=1,
    fg="white",
    bg="red",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="spider" # spider, circle, etc
)
testo.pack(side=LEFT, fill=X, expand=YES)

testo = Label(finestra, text="Basico 3")
testo.config(
    heigh=1,
    fg="white",
    bg="pink",
    font=("Consolas",10),
    padx=10,
    pady=20,
    cursor="spider" # spider, circle, etc
)
testo.pack(side=LEFT, fill=X, expand=YES)


finestra.mainloop()