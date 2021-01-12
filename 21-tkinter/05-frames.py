from tkinter import *

finestra = Tk()

finestra.title("Frame | Master python")
finestra.geometry("700x700")


major_frame = Frame(finestra, width=250, heigh=250)
major_frame.config(
    bg="gray"
)
major_frame.pack(side=TOP, fill=X, expand=YES, anchor=N)

frame = Frame(major_frame, width=250, heigh=250)
frame.config(
    bg="red",
    bd=12,
    relief=SOLID
)
frame.pack(side=LEFT, anchor=NW)
frame.pack_propagate(False)

testo = Label(frame, text="Prova test text")
testo.pack(side=LEFT,anchor=CENTER)

frame = Frame(major_frame, width=250, heigh=250)
frame.config(
    bg="green",
    bd=12,
    relief=RAISED
)
frame.pack(side=RIGHT, anchor=NE)

## Major Frame sotto ##

major_frame2 = Frame(finestra, width=250, heigh=250)
major_frame2.config(
    bg="gray"
)
major_frame2.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

frame = Frame(major_frame2, width=250, heigh=250)
frame.config(
    bg="yellow",
    bd=12,
    relief=GROOVE
)
frame.pack(side=LEFT)

frame = Frame(major_frame2, width=250, heigh=250)
frame.config(
    bg="blue",
    bd=12,
    relief=FLAT
)
frame.pack(side=RIGHT)

finestra.mainloop()