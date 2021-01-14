from tkinter import *

finestra = Tk()
finestra.geometry("700x450")
finestra.config(
    bg="CornflowerBlue", #6495ED
    bd=50,
    #highlightbackground="white"
)


def stampaDato():
    datoRisultante.set(datoRaccolto.get())

    if len(datoRisultante.get()) >= 1:
        dato_stampato.config(
            bg="navy",
            fg="#00FF00"
        )


datoRaccolto = StringVar()
datoRisultante = StringVar()

# Inserisce dato
Label(finestra, text="Inserisci testo: ").pack(anchor=NW)
Entry(finestra, textvariable=datoRaccolto).pack(anchor=NW)

# Mostra dato
Label(finestra, text="Dato inserito").pack(anchor=NW)
dato_stampato = Label(finestra, textvariable=datoRisultante)
dato_stampato.pack(anchor=NW)

# Submit
Label(finestra, background="#6495ED").pack(anchor=NW)
Button(finestra, text="Invia", command=stampaDato).pack(anchor=NW)

finestra.mainloop()