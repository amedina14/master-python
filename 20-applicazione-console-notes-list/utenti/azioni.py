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

        print(f"""
            Utente registrato:
            -{regs_nome}
            -{regs_cognome}
            -{regs_email}
        """)

    def login(self):
        print("Login selezionato. Entra nel sistema: ")

        try:
            log_email = input(f"Inserisci email utente:")
            log_pwd = input(f"Inserisci password utente:")
            print()
        except:
            print("Errore: I dati inseriti non sono corretti")

