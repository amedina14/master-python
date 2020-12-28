import os, shutil

opt = int(input("Inserisci la tua scelta:"
    "\n-0 per Creare cartella: directory-test"
    "\n-1 per Eliminare cartella: directory-test"
    "\n-2 per Copiare 'directory-test' e Rinominare cartella a: directory-renamed"
    "\n-3 per Elencare files di una cartella: 14-sistema-di-files"
    "\nScelta: "))

if opt == 0:
    ### Creare cartella (create) ###
    if not os.path.isdir("./14-sistema-di-files/directory-test"):
        os.mkdir("./14-sistema-di-files/directory-test")
        print("Cartella creata: directory-test")
    else:
        print("La cartella 'directory-test' esiste già")
elif opt == 1:
    ### Eliminare cartella (delete) ###
    if os.path.isdir("./14-sistema-di-files/directory-test"):
        os.rmdir("./14-sistema-di-files/directory-test")
        print("Cartella eliminata: directory-test")
    else:
        print("La cartella 'directory-test' non esiste")
elif opt == 2:
    ### Copiare e rinominare cartella (update) ###
    indirizzo_originale = "./14-sistema-di-files/directory-test"
    indirizzo_nuovo = "./14-sistema-di-files/directory-renamed"
    if os.path.isdir(indirizzo_nuovo):
        print("Il file esiste già:", indirizzo_nuovo)
    elif os.path.isdir(indirizzo_originale):
        shutil.copytree(indirizzo_originale, indirizzo_nuovo)
        print("Cartella copiata e rinominata:", "\""+indirizzo_nuovo+"\"")
    else:
        print("Non esistono cartelle, devi prima crearle.")
elif opt == 3:
    ### Elencare contenuto di una cartella (read) ###
    print("\n### Elenco files ###")
    contenuto = os.listdir("./14-sistema-di-files")
    for element in contenuto:
        print(element)
