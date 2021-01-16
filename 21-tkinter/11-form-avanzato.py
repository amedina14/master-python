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
    """
    Combinazioni
    ### 2 valori ###
    # (a+b)^2 = a^2 + 2ab + b^2
    1. web, 
    2. web-mobile 
    3. mobile

    ### 3 valori ###
    # (a+b+c)*2+1 = 7
    1. web, 
    2. web-mobile, 
    3. web-devops,
    4. web-mobile-devops,
    5. mobile, 
    6. mobile-devops
    7. devops

    ### 4 valori ###
    # (a+b+c+d)*4-1 = C=n*k-1, 
    1. web, 
    2. web-mobile, 
    3. web-devops,
    4. web-ML,
    5. web-mobile-devops,
    6. web-mobile-devops-ML,
    7. web-devops-ML,
    8. web-mobile-ML,
    9. mobile, 
   10. mobile-devops,
   11. mobile-ML
   12. mobile-devops-ML,
   13. devops,
   14. devops-ML,
   15. ML

    1. web, 
    9. mobile, 
   13. devops,
   15. ML,
    2. web-mobile, 
    3. web-devops,
    4. web-ML,
   10. mobile-devops,
   11. mobile-ML
   14. devops-ML,
    5. web-mobile-devops,
    7. web-devops-ML,
    8. web-mobile-ML,
   12. mobile-devops-ML,
    6. web-mobile-devops-ML

    w
    wm
    wd
    wml
    wmlm
    wmld
    wdm
    wmmld
    m
    mml
    md
    mmld
    dml
    ml
    d

    """

    testo=""

    # Comabinazoni condizionali con 4 valori
    if web.get():
        testo += "Sviluppatore web"

    if ml.get():
        if devops.get():
            if mobile.get():
                if web.get():
                    testo += ", mobile, DevOps e ML "
                else:
                    testo += "Sviluppatore mobile, Devops e ML"
            elif web.get():
                testo += ", DevOps e ML "
            else:
                testo += "Sviluppatore DevOps e ML "
        elif mobile.get():
            if web.get():
                testo += ", mobile e ML"
            else:
                testo += "Sviluppatore mobile e ML "
        elif web.get():
            testo += " e ML "
        else:
            testo += "Sviluppatore ML "
    elif devops.get():
        if mobile.get():
            if web.get():
                testo += ", mobile e DevOps"
            else:
                testo += "Sviluppatore mobile e DevOps"
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
    # Combinazioni a 3 valori
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

    """
    # Combinazioni a 2 valori
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
ml = IntVar()

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

Checkbutton(
    finestra, 
    text="Machine Learning",
    variable=ml,
    onvalue=1,
    offvalue=0,
    command=stampa
).grid(row=5,column=0)


mostra = Label(finestra)
mostra.grid(row=6,column=0) #pack(side=TOP, anchor=NW)

# Radio Buttons


# Option Menu

finestra.mainloop()