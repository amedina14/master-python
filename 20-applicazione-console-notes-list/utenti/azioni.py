class Azioni:

    def registro(self):
        print("Registro utente selezionato. ")

        try:
            regs_nome = input(f"Registra nome utente: ")
            regs_cognome = input(f"Registra cognome utente: ")
            regs_email = input(f"Registra email utente: ")
            regs_pwd = input(f"Registra password utente: ")
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

