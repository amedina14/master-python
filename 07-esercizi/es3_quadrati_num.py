"""
Esercizio 3
Quadrati dei primi 60 numeri
for e while
"""

for i in range(1,61):
    print(f"{i}: {pow(i,2)}")

print(f"----------------")
i=1
while i<=60:
    print(f"{i}: {pow(i,2)}")
    i+=1
