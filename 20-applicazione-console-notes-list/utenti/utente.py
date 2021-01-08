"""
Connessione a DB e classe utente
"""
import datetime
import hashlib
from utenti import connessione as conn

connect = conn.connettere()
database = connect[0]
cursor = connect[1]

class Utente:

    def __init__(self, nome, cognome, email, password):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = password
    
    def registrare(self):
        data = datetime.datetime.now()

        # Codifica password
        crittografia = hashlib.sha256()
        crittografia.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES (null, %s,%s,%s,%s,%s)"
        user = (self.nome,self.cognome,self.email,crittografia.hexdigest(),data)

        try:
            cursor.execute(sql,user)
            database.commit()
            result = [cursor.rowcount, self] # Ritorna il numero di righe interessate e i dati dell'oggetto utente
        except:
            result = [0, self] # Se errore il numero di righe di registro è pari a 0. (Esempio email ripetuta)

        return result
    
    def autenticare(self):

        # Domanda se esiste l'utente
        sql = "SELECT * FROM users WHERE email=%s AND password=%s"

        # Codifica password
        crittografia = hashlib.sha256()
        crittografia.update(self.password.encode('utf8'))

        # Dati per la domanda
        dati_sql = (self.email, crittografia.hexdigest())

        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", dati_sql)
        dati_utente = cursor.fetchone()

        for dato in dati_utente:
            if dati_utente.index(dato) == 0:
                print(f"Id: {dato}")
            elif dati_utente.index(dato) == 1:
                print(f"Nome: {dato}")
            elif dati_utente.index(dato) == 2:
                print(f"Cognome: {dato}")
            elif dati_utente.index(dato) == 3:
                print(f"Email: {dato}")
            elif dati_utente.index(dato) == 4:
                print(f"Password: {dato}")
            elif dati_utente.index(dato) == 5:
                print(f"Data creazione: {dato}")
        print()
        
        return dati_utente

"""
In questo punto la chiusura della connessione non permetteva di usare il DB
al uscire da questo modulo. Per questo dava errore nel modulo 'azioni' riga 33.
"""
#database.close()