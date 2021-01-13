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
header.grid(row=0, column=0, columnspan=12, sticky=W) # pack(side=LEFT, anchor=NW) # fill=Y, expand=YES

# Label
lbl_text = Label(finestra, text="Label form example")
lbl_text.grid(row=1, column=0, padx=5, pady=5)

# Textbox
text_in = Entry(finestra)
text_in.grid(row=1, column=1, sticky=W, padx=5, pady=5)
text_in.config(justify="right", state="normal")

# Label cognome
lbl_text = Label(finestra, text="Cognome")
lbl_text.grid(row=2, column=0, padx=5, pady=5)

# Textbox cognome
text_in = Entry(finestra)
text_in.grid(row=2, column=1, sticky=W, padx=5, pady=5)
text_in.config(justify="center", state="normal")

# Label DEPOSITO
lbl_text = Label(finestra, text="Deposito $$")
lbl_text.grid(row=3, column=0, padx=5, pady=5)

# Textbox DEPOSITO
text_in = Entry(finestra)
text_in.grid(row=3, column=1, sticky=W, padx=5, pady=5)
text_in.config(justify="left", state="disabled")


finestra.mainloop()