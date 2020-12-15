niente = None
stringa = "Ciao sono Adrian Medina"
intero = 100
floating = 3.1456
booleano = False
lista = [10,20,30,100,200]
listaMix = [10,"venti",30,"Cento",200]
tuplaNoCambia = ("master","in","Python")
dizionario = {
    "nombre": "Adrian",
    "cognome": "Medina",
    "corso": "master in python"
}
rango = range(9)
dato_byte = b"provando"

#print variable
print(niente)

#prendere il tipo di dato
print(type(niente))
print(type(stringa))
print(type(intero))
print(type(floating))
print(type(booleano))
print(type(lista))
print(type(listaMix))
print(type(tuplaNoCambia))

print(dizionario)
print(type(dizionario))
print(rango)
print(type(rango))
print(dato_byte)
print(type(dato_byte))

#Convertire dati
testo = "Testo di prova"
numerito = str(776)
print(testo + " " + numerito)
print("tipo dato 'numerito': ",type(numerito))
numerito = int(776)
print("tipo dato 'numerito': ",type(numerito))
#numerito = float(776)
numerito = float(numerito)
print("tipo dato 'numerito': ",type(numerito))