"""
Insieme di istruzioni sotto un nome concreto che si possono riutilizare
invocando il suo nome quante volte si voglia
"""

#Esempio 1
print("##### Esempio 1 #####")
def incremento():
    print("Hello")
    print("Ciao")
    print("Hola")
    print("Halo")
    print("Salut")
    print()

# Invocare funzione
incremento()
incremento()
incremento()

#Esempio 2 parametri
print("##### Esempio 2 #####")
def ciclo(parola):
    for i in range(10):
        print(parola,i,end="; ")

ciclo("Iterazione")

def nome_controlla_eta(n,e):
    print(f"Ti chiami {n}")
    if e >= 18:
        print("Sei maggiorenne")

nome = input("\nInserisci nome: ")
eta = int(input("Inserisci eta: "))
nome_controlla_eta(nome,eta)

#Esempio 3 tabellina con parametro
print("\n##### Esempio 3 #####")

def tabellina(n):
    print(f"\n### Tabellina del {n} ###")
    for i in range(1,11):
        print(f"{i} x {n}: {i*n}")

numero = int(input("Vuoi la tabellina del: "))
tabellina(numero)

#Esempio 3.1 tabellina con parametro
for j in range(1,11):
    tabellina(j)

""""
print("\n##### Esempio 3.1 #####")

def tabelline():
    print(f"### 10 Tabelline ###")
    for i in range(1,11):
        for ii in range(1,11):
            print(f"{i} x {ii}: {i*ii}")
        print()
#numero = int(input("Vuoi la tabellina del: "))
tabelline()
"""

"""
def dieci_tabelline():
    for j in range(1,11):
        tabellina(j)
dieci_tabelline()
"""