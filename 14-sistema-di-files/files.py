from io import open
import pathlib # Per prendere il path assoluto

path = str(pathlib.Path().absolute()) + "/14-sistema-di-files/file_di_testo.txt"
print(path)

#Aprire file
file = open(path, "a+")

#Scrivere su file
i=0
flag = True
while flag == True:
    i+=1
    file.write(f"*******Stringa {i} del file********\n")
    print(f"*******Stringa {i} del file********\n")
    if i == 10:
        #break
        flag = False

#Chiudere file
file.close()