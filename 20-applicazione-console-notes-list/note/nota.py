# Implementazione dei metodi
# Prima va elaborata la logica e poi si parte scrivendo il modello.
# Una buona pratica è scrivere l'applicazione verticalmente 
# passando per tutti gli strati possibili anzichè scrivere strato per strato 

from utenti import connessione
#import datetime

connect = connessione.connettere()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, utente_id, titolo, contenuto):
        self.utente_id = utente_id
        self.titolo = titolo
        self.contenuto = contenuto

    def creareNota(self):
        #data = datetime.datetime.now()

        sql = "INSERT INTO notes VALUES (null, %s, %s, %s, NOW())"
        dati = (self.utente_id, self.titolo, self.contenuto)

        try:
            cursor.execute(sql,dati)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0,self]

        return result

    def leggereNota(self):

        sql = "SELECT * FROM notes WHERE titulo = %s"
        dati = (self.titolo,)

        cursor.execute(sql,dati)
        nota = cursor.fetchone()
        for dato in nota:
            print(dato)
            print()
        
        return nota

    def cancellaNota(self):

        sql = "DELETE FROM notes WHERE titolo = %s"
        dati = (self.titolo,)

        try:
            cursor.execute(sql,dati)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result