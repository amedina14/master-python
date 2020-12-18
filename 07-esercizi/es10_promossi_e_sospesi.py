"""
Esercizio 10
Inserire i voti di 15 alunni e mostrare quanti sono promosso e sospesi
"""
from numpy import random
i=1
sospesi =0
promossi =0
while i<16:
    voto = random.randint(100)

    if voto <= 71:
        print(i,"Sospeso", voto)
        sospesi +=1
    else:
        print(i,"Promosso", voto)
        promossi +=1    
    i+=1
print(f"sospesi {sospesi}, promossi {promossi}")