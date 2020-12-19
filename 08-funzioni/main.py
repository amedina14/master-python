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