from tkinter import *

finestra = Tk()
finestra.geometry("500x500")
finestra.title("Barra di Menu Alt")
barraSuperiore = Menu(finestra)

finestra.config(
    menu=barraSuperiore,
)
barraSuperiore.config(
    bg="green", #696969
    fg="#D3D3D3",
)


menuFile = Menu(barraSuperiore, tearoff=0)
menuFile.add_command(label="New File")
menuFile.add_command(label="New Window")
menuFile.add_separator()
menuFile.add_command(label="Open File")
menuFile.add_command(label="Open Folder")
menuFile.add_separator()
menuFile.add_command(label="Exit", command=finestra.quit)


barraSuperiore.add_cascade(label="File",menu=menuFile)
barraSuperiore.add_command(label="Edit")
barraSuperiore.add_command(label="Selection")


finestra.mainloop()