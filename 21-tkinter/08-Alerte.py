from tkinter import *
from tkinter import messagebox as MessageBox # messagebox serve per le alerte 

finestra = Tk()
finestra.config(bd=70)

def mostrareAlerta():
    dng = MessageBox.showinfo("Sappi che:","Potresti copiare, incollare e poi modificare codice per ottenere risultati!.")
    MessageBox.showwarning("Attenzione developer", "Non perdere la concentrazione e la passione.")
    MessageBox.showerror("Non ti buttare giù", "Con determinazione e perseveranza puoi risolvere gli errori")
    # return True

# perche il command funzioni correttamente bisogna invocarlo senza parentesi
Button(finestra, text="Mostra alerta!", command=mostrareAlerta).pack() 


# Chiede se uscire
def uscire():
    result = MessageBox.askquestion("Uscire", "Vuoi continuare con il programma?")
    #result = MessageBox.askquestion("Uscire", "Sei sicuro di voler uscire?")

    if result != "yes": # Come configurazione questa funzione accetta 'yes' o 'no'
        finestra.destroy()

Button(finestra, text="Esci", command=uscire).pack() 


finestra.mainloop()