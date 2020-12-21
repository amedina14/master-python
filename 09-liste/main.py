"""
Collezioni di dati sotto un unico nome.
Per accedere o manipolare dati al suo intero dobbiamo usare un indice numerico.
"""

# Definire lista
print("\n#### Definire liste ####")
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

# Aggiungere elementi alle liste
print("\n#### Aggiungere elementi ####")
cinemas.append("Cine Rock Star")
cinemas.append("CineStellar")
print(cinemas)

# Scorrere la lista
print("\n#### Scorrere lista ####")
def add_film():
    new_film = ""
    risposta = ""
    risposta = input("Vuoi aggiungere un nuovo film (s/n): ")
    risposta = risposta.lower() #conversione risposta a minuscola
    while risposta == "s":
        new_film = input("Aggiungi nome del film: ")
        films.append(new_film)
        return films

i = 0
for i in films:
    print(f"{films.index(i)+1}. {i}")

add_film()
for i in films:
    print(f"{films.index(i)+1}. {i}")

print("\nLoop per inserire films. Stop con \"exit\"")
film = ""
while film != "exit":
    film = input("Insert film name: ")
    if film != "exit":
        films.append(film)

for i in films:
    print(f"{films.index(i)+1}. {i}")

