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

lbl_img = Label(finestra, image=renderizzare)
lbl_img.config(
    width=350,
    heigh=350
)
lbl_img.pack(side=BOTTOM,anchor=CENTER)

finestra.mainloop()