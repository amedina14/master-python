cantanti = ["I cani", "Calcutta", "TheGiornalisti", "Frah Quintale"]
numeri = [1, 9, 7, 6, 4, 2, 5, 8]

# Ordinare 
print("\n## sort() ##")
print(numeri)
numeri.sort()
print(numeri)
"""
cantanti.sort()
print(cantanti)
"""

# Aggiungere elementi
print("\n## insert() ##")
cantanti.append("Canova")
cantanti.insert(2, "Coez")
print(cantanti)

# Eliminare elementi
print("\n## pop() ##")
cantanti.pop(1)
print(cantanti)
cantanti.remove("I cani")
print(cantanti)

# Eliminare elementi
print("\n## reverse() ##")
cantanti.reverse()
numeri.reverse()
print(cantanti)

# Cerca dentro di una lista, booleano
print("\n## Cerca elemento dentro una lista ##")
print("Canova" in cantanti) # True

# Contare il numero di elementi di una lista
print("\n## len() ##")
print("Numero di cantanti:", len(cantanti))

# Contare quante volte è presente un elemento 
print("\n## count() ##")
cantanti.append("Coez")
print("#.Coez:",cantanti.count("Coez"))

# Prendere un indice 
print("\n## index() ##")
print(f"{cantanti[0]} sul indice:",cantanti.index("Canova"))

# Unire le liste 
print("\n## extend() ##")
cantanti.extend(numeri)
print(cantanti)