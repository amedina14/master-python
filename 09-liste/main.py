"""
Collezioni di dati sotto un unico nome.
Per accedere o manipolare dati al suo intero dobbiamo usare un indice numerico.
"""

# Definire lista
films = ["Batman","Superman","Lo Hobbit", "Star Wars"]

# Se vogliamo usare il metodo 'list', gli dobbiamo passare una tupla.
cinemas = list(("Cine Center", "Cinemania", "CineCity"))
year = list(range(2010,2020))
mixed = ["One",2,3.0,True,'5']

print(films)
print(cinemas)
print(year)
print(mixed)

# Accedere all'indice
print("\n#### Indici ####")
print(films[3])
print(films[-4])
print(films[1:3])
print(cinemas[1:]) #Prende tutti gli elementi dall'uno in avanti

films[1] = "Gran Torino"
print(films)

