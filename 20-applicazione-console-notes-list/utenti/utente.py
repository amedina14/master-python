"""
Connessione a DB e classe utente
"""
import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    port = 3308,
    database = "master_python"
)
print(database)
cursor = database.cursor(buffered=True)

class Utente:


    def __init__(self, nome, congome, email, password):
        self.nome = nome
        self.cognome = congome
        self.email = email
        self.password = password
    
    def registrare(self):
        return self.nome
    
    def autenticare(self):
        return self.nome

database.close()