from note import nota as modello

class Azione:

    # Il parametro utente serve per passare il dato del ID del utente alla nota
    def crea(self, utente):
        try:
            titolo = input("\nInserisci titolo della nota:")
            contenuto = input("\nInserisci contenuto della nota:\n")

            nota = modello.Nota(utente[0], titolo, contenuto)
            creazione = nota.creareNota()

            if creazione[0] >= 1:
                print(f"E' stata inserita la nota {nota.titolo}")
        except Exception as e:
            print(type(e))
            print(f"{type(e).__name__}: Non è stata inserita alcuna nota.")

    def leggiNote(self, utente):
        try:
            autore_nota = modello.Nota(utente[0])
            note_utente = autore_nota.listaNote()

            print(note_utente)


        except Exception as e:
            print(f"""
            {type(e).__name__}: Non è stata trovata alcuna nota.
            """)

    def cancella(self, utente):        
        try:
            titolo = input("Inserisci nota da cancellare:")

            nota = modello.Nota(utente[0], titolo,'')
            cancellazione = modello.cancella()

            if titolo == cancellazione[3]:
                print(f"""
                Nota '{titolo}' cancellata.
                """)

        except Exception as e:
            print(f"""
            {type(e).__name__}: Non è stata trovata alcuna nota da cancellare.
            """)
