import datetime

#Data
print(datetime.date.today())

#Data e tempo
dataCompleta = datetime.datetime.now()
print(dataCompleta)

#Anno
print(dataCompleta.year)
print(dataCompleta.month)
print(dataCompleta.day)

#Data personalizzata
data_personalizzata = dataCompleta.strftime("%d/%m/%Y, %H:%M:%S")
print("Customized data ", data_personalizzata)

#data e tempo formato POSIX
print(datetime.datetime.now().timestamp())

#Return the time part, with tzinfo None.
print(datetime.datetime.now().time())

#Sat Dec 26 11:59:03 2020
print(datetime.datetime.now().ctime())

