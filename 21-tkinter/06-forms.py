from tkinter import *

"""
Se si usa Grid non si può usare pack sullo stesso elemento/i anche acendo relazione.
"""

finestra = Tk()
finestra.geometry("700x400")
finestra.title("Forms con Tkinter")

# Header
header = Label(finestra, text="Moduli con tkinter: Header")
header.config(
    fg="white",
    bg="darkgrey",
    font=("Open Sans",20),
    padx=10,
    pady=10
)
header.grid(row=0, column=0, columnspan=12) # pack(side=LEFT, anchor=NW) # fill=Y, expand=YES

# Label
lbl_text = Label(finestra, text="Label form example")
lbl_text.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox
text_in = Entry(finestra)
text_in.grid(row=1, column=1, sticky=W, padx=5, pady=5)
text_in.config(justify="right", state="normal")

finestra.mainloop()