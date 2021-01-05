"""
Applicazione di console 'Lista appunti' Python e Mysql:
- Apre assistente
- Login o registro
- Se scegliamo registro, crea un utente nel DB
- Se scegliamo login, identifica l'user chiedendo le credenziali
- Crea, legge, e cancella appunti. 
"""


print("""
Azioni disponibili:
    -Registro
    -Login
""")

azione = input("Inserisci la tua scelta: ").capitalize()
#print(f"'{azione}'")

if azione == "Registro":
    print("Registro utente selezionato. ")

elif azione == "Login":
    print("Login selezionato. Entra nel sistema: ")

    #ins_email= input("Inserisci email: ")
    #ins_pwd= input("Inserisci password: ")
