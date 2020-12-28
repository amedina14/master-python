### Controllare se esiste file ###
import os.path

print(os.path.abspath("./")) # C:\Users\Utente\corsi-udemy\master-python

controlla_indirizzo =  os.path.abspath("./14-sistema-di-files/file_di_testo.txt") #/file_di_testo_copiato.txt

if os.path.isfile(controlla_indirizzo): 
    print(f"\"file_di_testo.txt\" esiste")
else:
    print("Il file non esiste")