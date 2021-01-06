"""
Connessione a DB e classe utente
"""
import datetime
import mysql.connector
import hashlib

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    port = 3308,
    database = "master_python"
)
#print(database)
cursor = database.cursor(buffered=True)

class Utente:


    def __init__(self, nome, cognome, email, password):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.password = password
    
    def registrare(self):
        data = datetime.datetime.now()

        # codifica password
        crittografia = hashlib.sha256()
        crittografia.update(self.password.encode('utf-8'))

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
        return self.nome

"""
In questo punto la chiusura della connessione non permetteva di usare il DB
al uscire da questo modulo. Per questo dava errore nel modulo 'azioni' riga 33.
"""
#database.close()