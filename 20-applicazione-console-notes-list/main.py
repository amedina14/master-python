"""
Applicazione di console 'Lista appunti' Python e Mysql:
- Apre assistente
- Login o registro
- Se scegliamo registro, crea un utente nel DB
- Se scegliamo login, identifica l'user chiedendo le credenziali
- Crea, legge, e cancella appunti. 
"""
import mysql.connector

connessione = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    port = 3308,
    database = "master_python"
)

cursor = connessione.cursor()

print("""
Azioni disponibili:
    -Registro
    -Login
""")

try:
    azione = input("Inserisci la tua scelta: ").capitalize()
#print(f"'{azione}'")
except:
    print("Errore: I dati inseriti non sono corretti")

if azione == "Registro":
    print("Registro utente selezionato. ")

    try:
        regs_nome = input(f"Registra nome utente:")
        regs_cognome = input(f"Registra cognome utente:")
        regs_email = input(f"Registra email utente:")
        regs_pwd = input(f"Registra password utente:")
    except:
        print("Errore: I dati inseriti non sono corretti")

    print(f"""
        Utente registrato:
        -{regs_nome}
        -{regs_cognome}
        -{regs_email}
    """)

elif azione == "Login":
    print("Login selezionato. Entra nel sistema: ")

    try:
        log_email = input(f"Inserisci email utente:")
        log_pwd = input(f"Inserisci password utente:")
    except:
        print("Errore: I dati inseriti non sono corretti")


connessione.close()