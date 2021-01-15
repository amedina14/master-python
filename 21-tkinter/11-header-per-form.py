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
header.grid(row=0,column=0,columnspan=5, sticky=W) #pack(anchor=N, side=TOP, fill=X, expand=YES)

def stampa():
    testo=""

    if web.get():
        testo += "Sviluppatore web"

    if devops.get():
        if mobile.get():
            if web.get():
                testo += ", mobile e DevOps "
            else:
                testo += "Sviluppatore mobile e Devops"            
        elif web.get():
            testo += " e DevOps "
        else:
            testo += "Sviluppatore DevOps "
    elif mobile.get():
        if web.get():
            testo += " e mobile "
        else:
            testo += "Sviluppatore mobile "


    """
    Combinazioni
    ### 2 valori ###
    1. web, 
    2. web-mobile 
    3. mobile

    ### 3 valori ###
    1. web, 
    2. web-mobile, 
    3. web-devops,
    4. web-mobile-devops,
    5. mobile, 
    6. mobile-devops
    7. devops


    """


    """
    # 2 Combinazioni        
    if web.get():
        testo += "Sviluppatore web "

    if mobile.get():
        if web.get():
            testo += "e sviluppatore mobile"
        else:
            testo += "Sviluppatore mobile"
    """

    mostra.config(
        text=testo,
        bg="yellow"
    )

web = IntVar()
mobile = IntVar()
devops = IntVar()

# Bottoni Check
Label(finestra, text="A cosa ti dedichi?").grid(row=1,column=0) #pack(side=TOP, anchor=NW)
Checkbutton(
    finestra, 
    text="web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=stampa
).grid(row=2,column=0)

Checkbutton(
    finestra, 
    text="mobile",
    variable=mobile,
    onvalue=1,
    offvalue=0,
    command=stampa
).grid(row=3,column=0)

Checkbutton(
    finestra, 
    text="DevOps",
    variable=devops,
    onvalue=1,
    offvalue=0,
    command=stampa
).grid(row=4,column=0)

mostra = Label(finestra)
mostra.grid(row=5,column=0) #pack(side=TOP, anchor=NW)

# Radio Buttons


# Option Menu

finestra.mainloop()