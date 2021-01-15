from tkinter import *

finestra = Tk()
finestra.geometry("800x300")
finestra.title("Header del form")

header = Label(finestra, text="Header")
header.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
header.pack(anchor=N, side=TOP, fill=X, expand=YES)

finestra.mainloop()