"""
SET è un tipo di dato per raggruppare dati (collezioni), 
ma non hanno ne indice, ne ordine. 
"""

persone = {
    "Adrian",
    "Sofia",
    "Victor"
}
print(type(persone))
print(persone)
persone.add("Galileo")
print(persone)
persone.remove("Adrian")
print(persone)
