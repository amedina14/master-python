import pathlib
import shutil
import io


#Spostare file
indirizzo_original = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo_copiato.txt"
indirizzo_nuovo = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo_copiato_rinominato.txt"

"""
path = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo_copiato.txt"

file = open(path, "r")
file.close()
"""

shutil.move(indirizzo_original, indirizzo_nuovo)