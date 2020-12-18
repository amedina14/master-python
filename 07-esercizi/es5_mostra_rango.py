"""
Esercizio 5
Mostra numeri tra due numeri detti dall'utente
"""

num1 = int(input("Da numero 1: "))
num2 = int(input("A numero 2: "))

if num1 < num2:
    for i in range(num1,(num2 + 1)):
        print(i)
else:
    print("Il numero 1 deve essere minore al numero 2")


"""
else:
    print("errore")
"""