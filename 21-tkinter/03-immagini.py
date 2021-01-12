from tkinter import *
#from Pillow import *
from PIL import Image, ImageTk


"""
pip install --upgrade Pillow
"""

finestra = Tk()
#finestra.geometry("650x450")

label1 = Label(finestra, text="VENV Inserire immagini dentro del programma:").pack(anchor=W)

immagine = Image.open('21-tkinter\img\logo-tesseract.png')
renderizzare = ImageTk.PhotoImage(immagine)

Label(finestra, image=renderizzare).pack(anchor=E)

finestra.mainloop()