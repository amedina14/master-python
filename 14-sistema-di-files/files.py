from io import open
import pathlib # Per prendere il path assoluto
import shutil

path = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo.txt"
print(path)

#Aprire file
file = open(path, "a+")

#Scrivere su file
i=0
flag = True
while flag == True:
    i+=1
    file.write(f"******* Stringa {i} del file ********\n")
    print(f"Riga aggiunta al file: ******* stringa {i} del file ********")
    if i == 10:
        #break
        flag = False
file.write("\n")
#Chiudere file
file.close()

#Aprire file in modo lettura
file_read = open(path, "r")
#leggere file
#contenuto = file_read.read()
#print("Lettura file","\n"+contenuto)
"""
#Stampa lettera per lettera di ciascuna riga
for i in contenuto:
    print(i, end="")
"""

#Leggere contenuto e salvare in lista
lista = file_read.readlines()
file_read.close()
#print(lista)
print("Lettura file")
for riga in lista:
    """
    if not riga.isnumeric():
        print(riga.upper())
    """
    lista_riga = riga.split()
    print(lista_riga)
    print(riga.capitalize().center(50)) #prima lettera della riga in maiuscola
    #print(riga.center(50)) 
    #aggiunge 50 spazzi ai fianchi per centrare
    
#Copiare files
indirizzo_originale = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo.txt"
indirizzo_nuovo = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo_copiato.txt"
#indirizzo_alternativo = str(pathlib.Path().absolute()) + "/13-packages/file_di_testo_copiato.txt"

shutil.copyfile(indirizzo_originale, indirizzo_nuovo)