"""
Dizionario
Un tipo di collezione che memorizza dati in formato
chiave > valore.
Simile ad un array associativo o ad un oggetto json
La chiave è di tipo testo
"""

persona = {
    "nome": "Adrian",
    "paese": "Ecuador",
    "web": "arandom.000webhostapp.com"
}
print(type(persona))
print(persona)
print("\n# Singolo valore per chiave nome #\n",persona["nome"])

print("\nChiavi:", end="\t ")
for dato in persona:
    print(dato, end="\t ")
print("\nValori:", end="\t ")
for dato in persona:
    print(persona[dato], end="\t ")