from tkinter import *

finestra = Tk()

finestra.title("Frame | Master python")
finestra.geometry("700x700")

# Frame contenitore
major_frame = Frame(finestra, width=250, heigh=250)
major_frame.config(
    bg="gray"
)
major_frame.pack(side=TOP, fill=X, expand=YES, anchor=N)

###### Quadrato rosso ######
frame = Frame(major_frame, width=250, heigh=250)
frame.config(
    bg="red",
    bd=12,
    relief=SOLID
)
frame.pack(side=LEFT, anchor=NW)
frame.pack_propagate(False)

# Testo dentro al quadrato rosso #
testo = Label(frame, text="Prova test text")
testo.pack(side=LEFT,anchor=CENTER)


###### Quadrato verde ######
frame = Frame(major_frame, width=250, heigh=250)
frame.config(
    bg="green",
    bd=12,
    relief=RAISED
)
frame.pack(side=RIGHT, anchor=NE)
frame.pack_propagate(False)

# Testo dentro al quadrato verde #
testo2 = Label(frame, text="test text 2")
testo2.config(
    bg="cyan",
    fg="magenta",
    font=("Consolas",10),
    height=20,
    width=15,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
testo2.pack() # anchor=CENTER,fill=Y,expand=YES



####################### Seconda parte #######################
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
frame.pack_propagate(False)

testo3 = Label(frame, text=" Testo 3")
testo3.config(
    bg="yellow",
    font=("Arial",20),
    bd=3,
    #relief=RAISED,
    anchor=CENTER,
)
testo3.pack(anchor=CENTER,fill=Y,expand=YES)

###### Quadrato blue ######
frame = Frame(major_frame2, width=250, heigh=250)
frame.config(
    bg="blue",
    bd=12,
    relief=FLAT
)
frame.pack(side=RIGHT)

finestra.mainloop()