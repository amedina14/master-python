import os
import pathlib

### Eliminare file ###
path_file_copiato = str(pathlib.Path().absolute())+"/14-sistema-di-files/file_di_testo_copiato_rinominato.txt"

os.remove(path_file_copiato)

