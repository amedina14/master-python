# Esempio 5: parametri opzionali e return

def stampa_saluto(n):
    saluto = f"Ciao {n}"
    return saluto

nome = "Adrian"
print(stampa_saluto(nome))

# Esempio 6: calcolatrice, parametri, opzionali e return
print("##### Esempio 6 #####")

def calcolatrice(num1, num2, basiche = False):

    if basiche != False:
        somma = num1 + num2
        resta = num1 - num2
        return f"somma: {somma}, resta: {resta}"
    else:
        moltiplizacione = num1 * num2
        divisione = num1 / num2
        return f"moltiplizacione: {moltiplizacione}, divisione: {divisione}"

numero1 = int(input("Inserisci numero 1: "))
numero2 = int(input("Inserisci numero 2: "))
basic = bool(input("Vuoi le operazioni basiche (True)?: "))

print(calcolatrice(numero1, numero2, basic))