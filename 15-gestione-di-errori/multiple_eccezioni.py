ripeti = True
while ripeti == True:
    ripeti = False
    try:
        numero = int(input("inserisci un numero per fare il quadrato: "))
        print(f"Il quadrato è {numero*numero}")
    except TypeError:
        print("Errore: il valore è stringa, non può fare il quadrato")
        ripeti = True
    except Exception as e:
        print("C'è stato un errore:", type(e).__name__)
        print(type(e))
        print(e)
    except ValueError:
        print("Il valore inserito non è numerico")
        ripeti = True
    except KeyboardInterrupt:
        print("\nCiao, alla prossima!")

