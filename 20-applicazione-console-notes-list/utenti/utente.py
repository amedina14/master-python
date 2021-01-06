"""
Connessione a DB e classe utente
"""
import datetime
import mysql.connector

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
        sql = "INSERT INTO users VALUES (null, %s,%s,%s,%s,%s)"
        user = (self.nome,self.cognome,self.email,self.password,data)

        cursor.execute(sql,user)
        database.commit()

        return [cursor.rowcount, self] # Ritorna il numero di righe interessate
    
    def autenticare(self):
        return self.nome

"""
In questo punto la chiusura della connessione non permetteva di usare il DB
al uscire da questo modulo. Per questo dava errore nel modulo 'azioni' riga 33.
"""
#database.close()