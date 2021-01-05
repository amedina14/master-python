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
