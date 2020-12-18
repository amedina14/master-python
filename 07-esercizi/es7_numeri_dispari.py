"""
Eserczio 7
Mostrare tutti i numeri dispari tra due numeri inseriti da tastiera
"""
num1 = -1
num2 = -1

while num1 < 0:
    num1 = int(input("Inserisci numero 1: "))
    if num1 < 0:
        print("Num1 non puo essere negativo")

while num1 > num2:
    num2 = int(input("Inserisci numero 2: "))
    if num1 > num2:
        print("Errore: Num1 non puo essere maggiore di num2")

for i in range(num1, num2):
    if i%2 != 0:
        print(i)


