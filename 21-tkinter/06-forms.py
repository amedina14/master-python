from tkinter import *

finestra = Tk()
finestra.geometry("700x400")
finestra.title("Forms con Tkinter")

header = Label(finestra, text="Moduli con tkinter: Header")
header.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans",20),
    padx=10,
    pady=10
)
header.pack(side=LEFT, anchor=NW)

finestra.mainloop()