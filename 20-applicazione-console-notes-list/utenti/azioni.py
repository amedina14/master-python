from utenti import utente as modello
from note import azione

class Azioni:

    def registro(self):
        print("\nRegistro utente selezionato. ")

        try:
            regs_nome = input(f"Registra nome utente: ")
            if type(regs_nome).__name__ == 'str': 
                print("Valore accettato")
                #raise ValueError("Non è string")

            regs_cognome = input(f"\nRegistra cognome utente: ")
            if type(regs_cognome).__name__ == 'str': 
                print("Valore accettato")

            regs_email = input(f"\nRegistra email utente: ")
            if type(regs_email).__name__ == 'str': 
                print("Valore accettato")

            regs_pwd = input(f"\nRegistra password utente: ")
            if type(regs_pwd).__name__ == 'str': 
                print("Valore accettato")
            print()
        except:
            print("Errore: I dati inseriti non sono corretti")

        # Instanziare l'oggetto utente con i suoi dati
        dati_utente = modello.Utente(regs_nome,regs_cognome,regs_email,regs_pwd)

        # Applica il metodo della classe Utente
        registro = dati_utente.registrare() 

        # 'registrare' ritorna una lista[0,1]. L'indice 1 (self) contiene i dati del utente 
        if registro[0] >= 1:
            print(f"""
                Ti sei registrato con successo 
                -Nome: {registro[1].nome}
                -Email: {registro[1].email}
            """)
        else:
            print(f"Non ti sei registrato correttamente, alcuni dati non sono validi.")


    def login(self):
        print("Login selezionato. Entra nel sistema: ")

        try:
            log_email = input(f"Inserisci email utente:")
            log_pwd = input(f"Inserisci password utente:")
            print()

            oggetto_utente = modello.Utente('', '', log_email, log_pwd) # Oggetto del utente loggato
            utente_loggato = oggetto_utente.autenticare() # Ottiene tutti i dati del utente identificato

            if log_email == utente_loggato[3]:
                print(f"Benvenuto {utente_loggato[1]}, ti sei registrato il {utente_loggato[5]}\n")
                self.prossimeAzioni(utente_loggato) # Gli si passa i dati dell'utente

        except Exception as e:
            print(f"""
            {type(e)}
            {type(e).__name__}: Login incorretto. Riprova più tardi
            """)

    def prossimeAzioni(self, dell_utente): # Gli passo l'oggetto
        print("""
            Cosa vuoi fare:
                -Crea nota (creare)
                -Leggi note (leggi)
                -Cancella nota (cancella)
                -Uscire (esci)
        """)

        azione_nota = input("Quale azione vuoi fare? ")
        oggetto_azioneNota = azione.Azione()

        if azione_nota == "creare":
            print("Hai selezionato creare nota:")
            oggetto_azioneNota.crea(dell_utente)
            self.prossimeAzioni(dell_utente)

        elif azione_nota == "leggi":
            print("Hai selezionato leggere nota:")
            self.prossimeAzioni(dell_utente)

        elif azione_nota == "cancella":
            print("Hai selezionato cancella nota:")
            self.prossimeAzioni(dell_utente)

        elif azione_nota == "esci":
            print(f"Okay {dell_utente[1]}. Alla prossima!")
            exit()