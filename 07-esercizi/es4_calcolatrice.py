"""
Esercizio 4
Calcolatrice: inserire due numeri e fare le operazioni basiche. 
"""
num1 = 0
num2 = 0
# or type(int(num1)) != int
while int(num1) < 1:
    num1 = input("inserisci numero 1 positivo: ")

num1 = int(num1)
num2 = int(input("inserisci numero 2: "))

print(f"Somma: \t{num1} + {num2} = {num1+num2}")
print(f"Resta: \t{num1} - {num2} = {num1-num2}")
print(f"Moltiplicazione: \t{num1} * {num2} = {num1*num2}")
print(f"Divisione: \t{num1} / {num2} = {num1/num2}")
