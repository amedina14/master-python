from veicolo import Veicolo

macchina1 = Veicolo("blu","Lamborghini","Murcielago",450,500,2)
macchina2 = Veicolo("rosso","Ferrari","LaFerrari",450,500,2)
macchina3 = Veicolo("giallo","Jeep","Wrangler",280,250,4)
macchina4 = Veicolo("griggio","Ferrari","Roma",450,500,2)

"""
"""
lista_macchine = [
    macchina1,
    macchina2,
    macchina3,
    macchina4
]

#macchina1.setMarca(input("Inserisci marca della macchina 1: "))
#print(macchina1.getMarca())

for macchina in lista_macchine:
    print(f"---------Informazione veicolo {lista_macchine.index(macchina)+1}---------")
    print(lista_macchine[lista_macchine.index(macchina)].getInfo())

#print(macchina1.getInfo())
#print(lista_macchine[0].getInfo())
#print(macchina1.getInfo())


# Verifica tipo oggetto
print("-------------------")
### da rivedere e correggere qui sotto
if type(macchina3) == Veicolo:
    print(isinstance(macchina3, Veicolo))
    print("L'oggetto è una macchina", macchina3.getMarca(), macchina3.getModelo())
else:
    print("L'oggetto non è una macchina")
