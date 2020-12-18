"""
Esercizio 6
10 tabelline dal 1 al 10
monstrare il titolo della tabella e poi le moltiplicazioni
"""

i=1

print()
for i in range(1,11):
    print(f"Tabellina del {i}")
    for moltiplicatore in range(1,11):
        print(f"{i} x {moltiplicatore} = {i*moltiplicatore}",end='; ')
    print("\n") # Genera due salti a capo
