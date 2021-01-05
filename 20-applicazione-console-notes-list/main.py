"""
Applicazione di console 'Lista appunti' Python e Mysql:
- Apre assistente
- Login o registro
- Se scegliamo registro, crea un utente nel DB
- Se scegliamo login, identifica l'user chiedendo le credenziali
- Crea, legge, e cancella appunti. 
"""
from utenti import azioni

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
"""
scelta = azioni.Azioni()

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
    scelta.registro()

elif azione == "Login":
    scelta.login()

#connessione.close()