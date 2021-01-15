from tkinter import *
from tkinter import messagebox

class Calcolatrice:

    def __init__(self, alerte):
        self.datoInput1 = StringVar()
        self.datoInput2 = StringVar()
        self.risultato = StringVar()
        self.alerte = alerte

    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            self.alerte.showerror("error","Inserisci i dati correttamente")

        return result

    def somma(self):
        self.risultato.set(self.cFloat(self.datoInput1.get()) + self.cFloat(self.datoInput2.get()))
        self.mostraRisultato()

    def resta(self):
        self.risultato.set(self.cFloat(self.datoInput1.get()) - self.cFloat(self.datoInput2.get()))
        self.mostraRisultato()

    def molt(self):
        self.risultato.set(self.cFloat(self.datoInput1.get()) * self.cFloat(self.datoInput2.get()))
        self.mostraRisultato()

    def div(self):
        self.risultato.set(self.cFloat(self.datoInput1.get()) / self.cFloat(self.datoInput2.get()))
        self.mostraRisultato()

    def mostraRisultato(self):
        self.alerte.showinfo("Risultato", f"Risultato: {self.risultato.get()}")
        self.datoInput1.set("")
        self.datoInput2.set("")

finestra = Tk()
finestra.geometry("500x500")
finestra.title("calcolatrice oop")
finestra.config(bd=25)

frame_maj = Frame(finestra)
frame_maj.config(
    width=350,
    height=250,
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
frame_maj.pack(anchor=N)
frame_maj.pack_propagate(False)

operazione = Calcolatrice(messagebox)

lbl_inserisci=Label(frame_maj, text="Valore:")
lbl_inserisci.pack()
dato = Entry(frame_maj, textvariable=operazione.datoInput1).pack()

lbl_inserisci2=Label(frame_maj, text="Valore:")
lbl_inserisci2.pack()
dato2 = Entry(frame_maj, textvariable=operazione.datoInput2).pack()

Button(frame_maj, text="+", command=operazione.somma).pack(side="left",fill=X,expand=YES)
Button(frame_maj, text="-", command=operazione.resta).pack(side="left",fill=X,expand=YES)
Button(frame_maj, text="*", command=operazione.molt).pack(side="left",fill=X,expand=YES)
Button(frame_maj, text="/", command=operazione.div).pack(side="left",fill=X,expand=YES)

finestra.mainloop()